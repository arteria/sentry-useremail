import sentry_useremail
from sentry_useremail.actions import EmailUserAction
from sentry.plugins.bases.notify import NotifyPlugin
from sentry.rules import rules


class UserEmailPlugin(NotifyPlugin):
    author = 'Dave McLain'
    author_url = 'https://github.com/dmclain/sentry-useremail'
    version = sentry_useremail.VERSION
    description = "Individual emails for rules."
    resource_links = [
        ('Issues', 'https://github.com/dmclain/sentry-useremail/issues'),
        ('Source', 'https://github.com/dmclain/sentry-useremail'),
    ]
    slug = 'useremail'
    title = 'User email'
    conf_title = title
    conf_key = 'useremail'

rules.add(EmailUserAction)
