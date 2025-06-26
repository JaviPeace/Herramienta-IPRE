from component import Notifier
from decorators import SMSDecorator, SlackDecorator

notifier = Notifier()
sms = SMSDecorator(notifier)
slack_sms = SlackDecorator(sms)

slack_sms.send()
