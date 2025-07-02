class Form:
    def submit(self):
        print("Submitting form")

class ValidationDecorator(Form):
    def __init__(self, form):
        self.form = form

    def submit(self):
        print("Validating form")
        self.form.submit()

f = Form()
validated_f = ValidationDecorator(f)
validated_f.submit()
