from SimpleGraphics import *

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600
resize(CANVAS_WIDTH, CANVAS_HEIGHT)

def main():
   drawBackground()

   print("where should the sun be? (integer)")
   drawSun(get_int("sun x-coord: "), get_int("sun y_coord: "))
   
   print("where should your house be? (integer)")
   house_y = get_int("house y-coord: ")
   drawHouse(get_int("house x-coord: "), house_y, house_y + 20 < CANVAS_HEIGHT/2) # want a gap of 20 

# draw everything except sun and house
def drawBackground():

   background("skyblue")

   setColor("green")
   rect(0, CANVAS_WIDTH/2, CANVAS_WIDTH, CANVAS_HEIGHT/2)

   drawClouds(600, 200)
   drawClouds(400, 50)
   drawClouds(100, 200)

# draw scuffed clouds given upper left corner coords
def drawClouds(left_x, up_y):

   cloud_w = 50
   cloud_h = 50

   # coords for three rows of clouds
   mid_xy = [left_x - cloud_w/2, up_y + cloud_h/2]
   tb_xy = [left_x, up_y]

   setColor("white")

   for i in range(2):
      for t in range(3):
         ellipse(tb_xy[0] + t * cloud_w/2, tb_xy[1] + i * cloud_h, cloud_w, cloud_h)

   for i in range(3):
      ellipse(mid_xy[0] + i * cloud_w, mid_xy[1], cloud_w, cloud_h)

# draws sun given center coords
def drawSun(x, y):
   # sun radius
   r = 50
   setColor("yellow")
   ellipse(x - r, y - r, 2 * r, 2 * r)


# draws house given center coords
# displays text if house is flying
def drawHouse(x, y, is_flying:bool):

   wall_wh = 200
   wall_half = wall_wh/2

   # upper left corner of wall rect
   corner_x = x - wall_half
   corner_y = y - wall_half

   # walls
   setColor("orange")
   rect(corner_x, corner_y, wall_wh, wall_wh)

   # roof
   setColor("red")
   polygon(corner_x, corner_y, corner_x + wall_wh, corner_y, corner_x + wall_half, corner_y - wall_half*0.5)

   # window
   window_d = wall_half*0.6 # diameter
   # upper left corner coords
   window_xy = [corner_x + wall_half*1.3, corner_y + wall_half*0.4]

   setColor("yellow")
   ellipse(window_xy[0], window_xy[1], window_d, window_d)
   setColor("black")
   line(window_xy[0] + window_d/2, window_xy[1], window_xy[0] + window_d/2, window_xy[1] + window_d)
   line(window_xy[0], window_xy[1] + window_d/2, window_xy[0] + window_d, window_xy[1] + window_d/2)

   # door
   setColor("brown")
   rect(corner_x + wall_half*0.5, corner_y + wall_half*0.5, wall_half*0.6, wall_half*1.5)

   # Draw the text
   if is_flying:
      setOutline("black")
      setFont("Times", "24", "bold")
      text(CANVAS_WIDTH*0.5, CANVAS_HEIGHT*0.8, "magic!!! you're flying", "c")


# does input() until .isnumeric() is true for what was entered
# returns int
def get_int(prompt):
   while True:
      inp = input(prompt)
      if inp.isnumeric():
            return int(inp)
      print("that's not an integer :(\n")

if __name__ == "__main__":
   main()




