class Message:
    def show(self):
        return "Hello"

class EmojiDecorator(Message):
    def __init__(self, message):
        self.message = message

    def show(self):
        return self.message.show() + " 😊"

m = Message()
emoji_m = EmojiDecorator(m)
print(emoji_m.show())
