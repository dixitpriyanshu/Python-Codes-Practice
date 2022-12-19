################### Scope ####################

# enemies = 1

# def increase_enemies():
#   enemies = 2
#   print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")

#####   Local Scope

# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)

# drink_potion()

# print(potion_strength)   "Throws error"

### Global Scope

# player_health = 10
# def drink_potion():
#     potion_strength = 2
#     print(player_health)

# drink_potion()


#### There is Block Scope

# if 3>2:
#     a_variable = 10   " Its has same refernce in global scope"

game_level = 3
def create_enemy():
    enemies = ["Skeleton","Zombie","Alien"]
    if game_level<5:
        new_enemy = enemies[0]
# even though new enemy is inside if statement it is perfectly valid
# but after embedding it inside the create_enemy function it can't be accesed by print statement  if it's not in the function
    print(new_enemy)


#### Modifying Global Scope

enemies = 1

# def increase_enemies():
#     global enemies
#     enemies + 1
#     print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")    


# Same functionality without accessing global variable inside funtion
def increase_enemies():
    print(f"enemies inside function: {enemies}")
    return enemies+1

enemies = increase_enemies()
print(f"enemies outside function: {enemies}")

# Global Constants

PI = 3.1428
URL = "www.google.co.in"
TWITTER = "@priyanshu"