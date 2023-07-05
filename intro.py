# from SimpleGraphics import *

# background("white")

# (number) side: left 0, top 1, right 2, bottom 3
# left 0 right 2
def rectBorder(x, y, w, h, fillColor, color, side):
   setColor(fillColor)
   rect(x, y, w, h)
   setOutline(color)

   if side == 0:
      line(x, y, x, y + h)
   
   elif side == 2:
      line(x + w, y, x + w, y + h)

   elif side == 1:
      line(x, y, x + w, y)

   elif side == 3:
      line(x, y + h, x + w, y + h)

   else:
      print("rectBorder input side wrong number")

# rectBorder(100, 100, 20, 20, "red", "black", 1)
# rectBorder(100, 300, 20, 20, "red", "black", 3)

condition = True

counter = 0
while counter < 10:
   counter += 1
