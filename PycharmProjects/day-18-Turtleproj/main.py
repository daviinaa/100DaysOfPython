import random
import turtle as turt
from turtle import  Screen
# import colorgram
#
# # extract colors from image using colorgram
# color_in_images = colorgram.extract('images.jpg', 30)
#
# rgb_colors = []
# for color in color_in_images:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

color_list = [(188, 151, 176), (166, 73, 29), (38, 97, 176), (22, 94, 14), (219, 213, 207), (51, 118, 45), (146, 72, 102), (11, 72, 7), (149, 24, 8), (194, 141, 26), (222, 200, 211), (76, 82, 13), (93, 13, 29), (15, 60, 141), (88, 154, 81), (219, 197, 137), (181, 186, 212), (220, 177, 171), (20, 43, 81)]
timmyturtle = turt.Turtle()


print(round(timmyturtle.xcor(), 5))
print(round(timmyturtle.ycor(), 5))


timmyturtle.speed("fastest")
turt.colormode(255)
timmyturtle.pu()
timmyturtle.hideturtle()
timmyturtle.setheading(225)
timmyturtle.fd(300)
timmyturtle.setheading(0)
num_of_dots = 100

for dot_count in range(1, num_of_dots +1):
    timmyturtle.dot(20, random.choice(color_list))
    timmyturtle.fd(50)

    if dot_count % 10 == 0:
        timmyturtle.setheading(90)
        timmyturtle.fd(50)
        timmyturtle.setheading(180)
        timmyturtle.fd(500)
        timmyturtle.setheading(0)

# start_x = 0
# start_y = 0
#
# timmyturtle.color(random.choice(color_list))
# timmyturtle.goto(start_x, start_y)
# for _ in range(10):
#     for n in range(10):
#         timmyturtle.setheading(90)
#         timmyturtle.dot(20, random.choice(color_list))
#         timmyturtle.pu()
#         timmyturtle.fd(50)
#     start_y += 35
#     timmyturtle.goto((start_x, start_y))
#
# print(round(timmyturtle.xcor(), 5))
# print(round(timmyturtle.ycor(), 5))





print(timmyturtle)


screen = Screen()
screen.exitonclick()


# timmyturtle = Turtle()
# # timmyturtle.color("blue")
# timmyturtle.shape("turtle")
# turtle.colormode(255)
#
#
# def colors():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_color = (r, g, b)
#     return random_color
#
#
# timmyturtle.pensize(1)
# # random_on = True
# # directions = [0, 90, 180, 270]
#
# timmyturtle.speed("fastest")

#
# def draw_spyrograpgh(gap_size):
#     for _ in range(int(360/gap_size)):
#         timmyturtle.circle(80)
#         timmyturtle.color(colors())
#         timmyturtle.setheading(timmyturtle.heading() + 10)
#
#
# draw_spyrograpgh(5)

# for _ in range(100):
#     timmyturtle.fd(10)
#     timmyturtle.setheading(random.choice(directions))
#     timmyturtle.color(colors())
#     timmyturtle.speed("fast")












# challenge for drawing different shapes
# define a function called draw shape and pass in the number of sides as the parameter
# def drawshape(num_of_sides):
#     angle = 360/num_of_sides
#     for n in range(num_of_sides):
#         timmyturtle.left(angle)
#         timmyturtle.fd(100)

# shapes sides is also the number of the types of shapes we want to draw represented by 3 - 10
# call the drawshape() function and pass in the for loop as the iterator


# for shapes_sides in range(3, 11):
#     drawshape(shapes_sides)
#     timmyturtle.color(random.choice(colors))