# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
sum=0
count=0
for height in student_heights:
    sum+=height
    count+=1
avg_height = round(sum/count)    
print(avg_height)
#Write your code below this row 👇




