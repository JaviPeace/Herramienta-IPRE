from leaf import Text
from composite import Document

doc = Document()
doc.add(Text("Hello"))
doc.add(Text("World"))
print(doc.render())
