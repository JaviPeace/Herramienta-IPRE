from composite import Picture
from leaf import Circle, Square

pic = Picture()
pic.add(Circle())
pic.add(Square())
print(pic.draw())
