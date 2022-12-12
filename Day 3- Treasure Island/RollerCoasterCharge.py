print("Wlcome to the Roller Coaster!")
height = int(input("What is your height?\n"))

if height >= 120:
    print("You can ride the Roller Coaster :)")
    age = int(input("What is your age?\n"))
    if age<=12:
        bill=5
        print("Children ticket are 5$")
    elif age<=18:
        bill=7
        print("Youth tickets are 7$")
    elif age>=45 and age<55:
        bill=0
        print("Everything is going to be ok, have a free ride on us :)")        
    else:
        bill=12
        print("Adult tickets are 12$")   
    want_photo_input = input("Do you want a photo taken? Y or N\n")
    if want_photo_input=='Y':
        bill+=3
    print(f"Your final bill is {bill}$")         
else:
    print("Sorry, you have to grow talleer before you can ride :(")    