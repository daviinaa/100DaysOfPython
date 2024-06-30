# starting off with tkinter
from tkinter import *


def convert():
    final_result = float(something.get()) * 1.6
    converted_km.config(text=f"{final_result}")


window = Tk()
window.title("Mile to KM converter")
window.minsize(width=300, height=150)
window.config(padx=100, pady=50)


# Label 1
is_equal_to = Label(text="is equal to", font=("Arial", 24, "normal"))
is_equal_to.grid(column=0, row=1)

# Label 2
converted_km = Label(text=0, font=("Arial", 20, "normal"))
converted_km.grid(column=1, row=1)

# Label 3
miles = Label(text="Miles", font=("Arial", 18, "normal"))
miles.grid(column=2, row=0)

# Label 4
km = Label(text="Km", font=("Arial", 18, "normal"))
km.grid(column=2, row=1)

# button 1
button = Button(text="Calculate", command=convert)
button.grid(column=1, row=2)

# entry
something = Entry(width=12)
something.grid(column=1, row=0)

window.mainloop()


# function that can take any number of parameters/arguments
# def add(*args):
#     print(args[4])
#     sum = 0
#     for n in args:
#         sum += n
#     return sum
#
#
# print(add(6, 8, 9, 90, 43, 4, 4, 7))

# keyword arguments


# def calculate(n, **kwargs):
#     print(kwargs)
#     # for (key, value) in kwargs.items():
#     n *= kwargs["jump"]
#     n += kwargs["swim"]
#     print(n)
#         # print(key)
#         # print(value)
#
#
# calculate(2, jump=4, swim=8)

#
# class Car:
#     def __init__(self, **kw):
#         self.move = kw.get("move")
#         self.model = kw.get("model")
#
#
# my_car = Car(move="foward", model="nissan")
#
# print(my_car.move)
