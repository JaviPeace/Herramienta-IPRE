class User:
    def get_name(self):
        return "User"

class TitleDecorator(User):
    def __init__(self, user):
        self.user = user

    def get_name(self):
        return "Mr. " + self.user.get_name()

u = User()
decorated = TitleDecorator(u)
print(decorated.get_name())
