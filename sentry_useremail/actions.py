from __future__ import absolute_import

from django import forms
from django.conf import settings
from django.utils.safestring import mark_safe

from sentry.models import User
from sentry.plugins import plugins
from sentry.rules.actions.base import EventAction
from sentry.utils.email import MessageBuilder, group_id_to_email
from sentry.web.forms.fields import UserField


class EmailUserForm(forms.Form):
    username = UserField()


class EmailUserAction(EventAction):
    form_cls = EmailUserForm
    label = 'Send an email to {username}'

    def after(self, event, state):
        mail_plugin = plugins.get('mail')
        if not mail_plugin.is_enabled(event.project):
            return

        username = self.get_option('username')
        try:
            user = User.objects.get(username=username)
        except:
            return

        project = event.project
        group = event.group

        subject_prefix = mail_plugin.get_option('subject_prefix', project) or settings.EMAIL_SUBJECT_PREFIX

        interface_list = []
        for interface in event.interfaces.itervalues():
            body = interface.to_email_html(event)
            if not body:
                continue
            interface_list.append((interface.get_title(), mark_safe(body)))

        subject = group.get_email_subject()

        link = group.get_absolute_url()

        template = 'sentry/emails/error.txt'
        html_template = 'sentry/emails/error.html'

        context = {
            'group': group,
            'event': event,
            'tags': event.get_tags(),
            'link': link,
            'interfaces': interface_list,
            'rule': None,
            'rule_link': None,
        }

        headers = {
            'X-Sentry-Logger': group.logger,
            'X-Sentry-Logger-Level': group.get_level_display(),
            'X-Sentry-Project': project.name,
            'X-Sentry-Reply-To': group_id_to_email(group.id),
        }

        msg = MessageBuilder(
            subject='%s%s' % (subject_prefix, subject),
            template=template,
            html_template=html_template,
            body=body,
            headers=headers,
            context=context,
            reference=group,
        )


        msg.add_users([user.id], project=project)
        return msg.send()
