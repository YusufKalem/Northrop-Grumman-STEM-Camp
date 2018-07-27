import arcade
#draw a smiley face

#set window dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

#open a window and set the title/dimensions
arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT,"Smiley Face")
arcade.set_background_color(arcade.color.WHITE)

#start the render process
arcade.start_render()
#draw functions here
#make head of smiley
x=300
y=300
radius=200
arcade.draw_circle_filled(x, y, radius, arcade.color.YELLOW)
#Make right eye
x=400
y=350
radius=27
arcade.draw_circle_filled(x, y, radius, arcade.color.BLACK)
#Make left eye
x=200
y=350
radius=27
arcade.draw_circle_filled(x, y, radius, arcade.color.BLACK)
#A MOUTH
x=300
y=225
radius=75
arcade.draw_circle_filled(x, y, radius, arcade.color.BRICK_RED)

arcade.finish_render()
arcade.run()


