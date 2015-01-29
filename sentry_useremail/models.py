from sentry_useremail.actions import EmailUserAction
from sentry.rules import rules

rules.add(EmailUserAction)
