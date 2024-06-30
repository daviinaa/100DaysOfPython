import pandas
student_scores = {
    "students": ["angela", "dave", "john"],
    "scores": [84, 90, 95]
}

# for looping through a dict, breaking it down
# for (key, value) in student_scores.items():
#     print(value)

# doing same for pandas dataframe
student_dataframe = pandas.DataFrame(student_scores)
print(student_dataframe)

# loop through a dataframe
# for (key, value) in student_dataframe.items():
#     print(value)

# pandas loop iterrow
for (index, row) in student_dataframe.iterrows():
    # print(row.students)
    if row.scores > 90:
        print(row.students)