from graphics import Canvas
import math
    
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 300

CLOUD_WIDTH = 120
CLOUD_HEIGHT = 80

TRUNK_HEIGHT = 80
TRUNK_WIDTH = 20
LEAVES_SIZE = 60

TREE_BOTTOM_Y = CANVAS_HEIGHT - 20 

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    draw_cloud(canvas, 140, 10, 'salmon')
    draw_cloud(canvas, 10, 60, "pink")
    draw_cloud(canvas , 270, 25, "purple")


    draw_tree(canvas, 40, 200, "brown" , "green")
    draw_tree(canvas, 150, 200, "purple" , "hotpink")
    draw_tree(canvas, 310, 200, "saddlebrown" , "darkorange")


def draw_tree(canvas, x, y, trunk_color, leaves_color ):
    left_x= x
    top_y= y
    right_x= x + TRUNK_WIDTH 
    bottom_y= y + TRUNK_HEIGHT

    canvas.create_rectangle(
        left_x,
        top_y, 
        right_x,
        bottom_y, 
        trunk_color
        )

    mid_x = x+(TRUNK_WIDTH/2)

    leaf_left_x= mid_x - (LEAVES_SIZE/2)
    leaf_top_y= y - LEAVES_SIZE
    leaf_right_y= mid_x + (LEAVES_SIZE/2)
    leaf_bottom_y= y +1

    canvas.create_oval(
        leaf_left_x,
        leaf_top_y,
        leaf_right_y,
        leaf_bottom_y,
        leaves_color
    )



def draw_cloud(canvas, x, y, color):
    """
    This function draws one cloud. You can call it and pass in 
    different values of x and y (the location of the cloud) and
    color (the color of the cloud). 
    """
    cloud_bottom_start_y = y + (1/3) * CLOUD_HEIGHT
    cloud_bottom_end_y = y + CLOUD_HEIGHT
    cloud_top_start_x = x + (1/4) * CLOUD_WIDTH
    cloud_top_end_x = x + (3/4) * CLOUD_WIDTH
    # Bottom two puffs
    canvas.create_oval(
        x, 
        cloud_bottom_start_y,
        x + (3/4) * CLOUD_WIDTH,
        cloud_bottom_end_y,
        color
    )
    canvas.create_oval(
        x + (1/4) * CLOUD_WIDTH, 
        cloud_bottom_start_y,
        x + CLOUD_WIDTH,
        cloud_bottom_end_y,
        color
    )

    # Top puff
    canvas.create_oval(
        cloud_top_start_x,
        y,
        cloud_top_end_x,
        y + (2/3) * CLOUD_HEIGHT,
        color
    )




if __name__ == '__main__':
    main()