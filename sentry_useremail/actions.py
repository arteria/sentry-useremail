from __future__ import absolute_import

from django import forms

from sentry.web.forms.fields import UserField
from sentry.rules import rules
from sentry.rules.actions.base import EventAction


class EmailUserForm(forms.Form):
    user = UserField()


class EmailUserAction(EventAction):
    form_cls = EmailUserForm
    label = 'Send an email to {user}'

    def after(self, event, state):

        pass


rules.add(EmailUserAction)
