# TODO Error handling
# try:
#     file = open("new-file.txt")
#     test_dict = {"house": "duplex"}
#     print(test_dict["house"])
# except FileNotFoundError:
#     file = open("new-file.txt", "w")
#     file.write("something to write")
#     print("whats happening")
# except KeyError as error_message:
#     print(f"notfound: key {error_message} not found")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("file was closed")
# raise TypeError("this is a made up error")

# TODO raising exceptions example

# height = float(input("height: "))
# weight = int(input("weight: "))
# if height > 3:
#     raise ValueError("Average human height shouldnt be above 3 meters")
# bmi = weight / height ** 2
# print(bmi)


# TODO Examples of errors
# # KeyError
# sample_dict = {"key" : "value"}
# print(sample_dict["non"])


# IndexError
# Fruits = ["Apple", "mango", "cherry"]
# print(Fruits[3])

# TypeError
# text = "abc"
# print(text + 45)


# TODO error handling in function
# # ["Apple", "Pear", "Orange"]  the input
# fruits = eval(input())
#
# TODO: Catch the exception and make sure the code runs without crashing.
#
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError:
#         print("Fruit pie")
#     else:
#         print(fruit + " pie")
#
# make_pie(4)

