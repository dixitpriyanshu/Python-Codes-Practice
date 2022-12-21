class User:

    def __init__(self, userid, username) -> None:
        self.id = userid
        self.username = username

user_1 = User("001", "Priyanshu")

print(user_1.id)
print(user_1.username)