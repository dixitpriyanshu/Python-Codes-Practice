# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆
max1=0
for score in student_scores:
    if max1<score:
        max1=score
print(f"The highest score in the class is: {max1}")        
#Write your code below this row 👇




