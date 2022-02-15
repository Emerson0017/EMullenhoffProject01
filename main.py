
# First, we tell the program to import arcade.

import arcade

# We will be animating an up-close image of an acoustic guistar

# Next, we define the function which animates the image.
def main():
    # We will start by opening the window in parameter dimensions and set a background color
    arcade.open_window(1000, 500, "EMullenhoffProject1: Up-close Acoustic Guitar")
    arcade.set_background_color(arcade.color.LIGHT_BROWN)
    # We will create objects now
    soundhole = arcade.create_ellipse(516, 250, 500, 500, arcade.color.BLACK)
    eString = arcade.create_rectangle(325, 250, 10, 500, arcade.color.LIGHT_GRAY)
    aString = arcade.create_rectangle(400, 250, 10, 500, arcade.color.LIGHT_GRAY)
    dString = arcade.create_rectangle(475, 250, 10, 500, arcade.color.LIGHT_GRAY)
    gString = arcade.create_rectangle(550, 250, 10, 500, arcade.color.LIGHT_GRAY)
    bString = arcade.create_rectangle(625, 250, 10, 500, arcade.color.LIGHT_GRAY)
    eString1 = arcade.create_rectangle(700, 250, 10, 500, arcade.color.LIGHT_GRAY)
    pick = arcade.create_polygon([(125, 25), (50, 150), (200, 150)],
                                 arcade.color.BLACK)

    # Below, we will draw the objects
    arcade.start_render()
    soundhole.draw()
    eString.draw()
    aString.draw()
    dString.draw()
    gString.draw()
    bString.draw()
    eString1.draw()
    pick.draw()
    arcade.draw_text("Fender", 100, 120, arcade.color.WHITE)
    arcade.finish_render()
    arcade.run()



# Finally, we call the function
main()
