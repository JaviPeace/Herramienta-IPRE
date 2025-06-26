class UIObserver:
    def update(self, event, data):
        pass

class ClickLogger(UIObserver):
    def update(self, event, data):
        if event == "click":
            print(f"[ClickLogger] Clicked at {data}")

class HoverTracker(UIObserver):
    def update(self, event, data):
        if event == "hover":
            print(f"[HoverTracker] Hovered over {data}")
