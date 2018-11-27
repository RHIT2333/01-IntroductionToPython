"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Hanrui Chen.
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################
import rosegraphics as rg
window = rg.TurtleWindow()
ojbk = rg.SimpleTurtle('turtle')
xjbg = rg.SimpleTurtle('turtle')
ojbk.pen = rg.Pen('red', 1)
xjbg.pen = rg.Pen('blue', 1)
ojbk.speed = 20
xjbg.speed = 20

sizek = 385
sizex = 10

for k in range(16):
    ojbk.draw_square(sizek)
    ojbk.pen_up()
    ojbk.right(6)
    ojbk.pen_down()
    sizek = sizek - 25

for j in range(16):
    xjbg.draw_square(sizex)
    xjbg.pen_up()
    xjbg.left(6)
    xjbg.pen_down()
    sizex = sizex + 25

window.close_on_mouse_click()
