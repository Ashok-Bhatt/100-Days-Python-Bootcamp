class User:
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.follower = 0
        self.following = 0
    
    def unfollow(self, user):
        user.follower = user.follower - 1
        self.following = self.following - 1

    def follow(self, user_list):
        for user in user_list:
            user.follower = user.follower + 1
        self.following = self.following + len(user_list)

    def puri_Kundli(self):
        print(f"Name:{self.name}    Age:{self.age}    Follower:{self.follower}     Following:{self.following}")
    
ashok = User("Ashok", 18)
irfan = User("Irfan", 19)
chetan = User("Chetan", 19)
ankit = User("Ankit", 18)
tushar = User("Tushar", 18)

ashok.follow([irfan,chetan])
irfan.follow([ashok,ankit,tushar,irfan])
chetan.follow([ashok,tushar,ankit])
ankit.follow([ashok,chetan,irfan])
tushar.follow([ankit,ashok])

ashok.puri_Kundli()
irfan.puri_Kundli()
chetan.puri_Kundli()
ankit.puri_Kundli()
tushar.puri_Kundli()

irfan.unfollow(irfan)
irfan.puri_Kundli()