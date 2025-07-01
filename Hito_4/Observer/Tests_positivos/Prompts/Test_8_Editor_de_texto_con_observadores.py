class DocumentObserver:
    def update(self, text):
        pass

class SpellChecker(DocumentObserver):
    def update(self, text):
        print(f"[SpellChecker] Checking '{text}'...")

class AutoSaver(DocumentObserver):
    def update(self, text):
        print(f"[AutoSaver] Saving draft of '{text}'...")

class Document:
    def __init__(self):
        self.text = ""
        self.observers = []

    def attach(self, obs):
        self.observers.append(obs)

    def edit(self, new_text):
        self.text = new_text
        for obs in self.observers:
            obs.update(new_text)

# Uso
doc = Document()
doc.attach(SpellChecker())
doc.attach(AutoSaver())

doc.edit("Hola mundo")
