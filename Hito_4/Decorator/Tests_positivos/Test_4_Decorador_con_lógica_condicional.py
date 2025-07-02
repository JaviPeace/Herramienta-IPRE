# Decorador que restringe acceso

class Page:
    def render(self):
        print("Rendering page")

class AuthDecorator(Page):
    def __init__(self, page, user_logged_in):
        self._page = page
        self._user_logged_in = user_logged_in

    def render(self):
        if self._user_logged_in:
            self._page.render()
        else:
            print("Access Denied")

# Uso
page = Page()
secure_page = AuthDecorator(page, user_logged_in=False)
secure_page.render()
