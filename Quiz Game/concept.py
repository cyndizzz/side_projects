class User:
    # pass # for empty class

    # Add attributes
    def __init__(self, user_id, username):
        # Initiate attributes
        self.id = user_id
        self.username = username
        self.followers = 0  # Default value to be 0.
        self.following = 0

    # Add Method
    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("001", "angela")
user_2 = User("002", "john")
print(user_1.id)

# Add attribute
user_1.id = "002"
print(user_1.id)
print(user_1.followers)

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)