class Message:
    def get(self):
        return "msg"

class Wrapper:
    def __init__(self, obj):
        self.obj = obj

    def show(self):
        return f"Wrapped: {self.obj.get()}"