import pandas

student_dict = {
    "student" : ["Angela", "James", "Lily"],
    "score" : [56, 76, 98]
}

student_dataframe = pandas.DataFrame(student_dict)
print(student_dataframe)

for (index, row) in student_dataframe.iterrows():
    print(row.student)
    if row.student == "Angela":
        print(row.score)
