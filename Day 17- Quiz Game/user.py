class User:

    def __init__(self, userid, username) -> None:
        self.id = userid
        self.username = username
        self.followers =0


user_1 = User("001", "Priyanshu")

print(user_1.id)
print(user_1.username)

print(user_1.followers)

user_1.followers = 99

print(user_1.followers)