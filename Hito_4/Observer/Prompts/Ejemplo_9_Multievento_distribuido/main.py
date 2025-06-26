from subject import EventSource
from observer import ClickLogger, HoverTracker

ui = EventSource()
ui.subscribe("click", ClickLogger())
ui.subscribe("hover", HoverTracker())

ui.notify("click", "(10, 20)")
ui.notify("hover", "Button")
