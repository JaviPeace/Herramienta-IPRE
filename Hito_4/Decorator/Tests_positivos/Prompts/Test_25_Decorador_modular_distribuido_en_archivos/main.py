from component import Message
from decorators import EncryptionDecorator, LoggingDecorator

m = Message()
encrypted_m = EncryptionDecorator(m)
logged_encrypted_m = LoggingDecorator(encrypted_m)
logged_encrypted_m.send()
