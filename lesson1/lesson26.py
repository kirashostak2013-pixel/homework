#class User:
 #   def __init__(self, name):
 #       self.name = name
        
#user = User("Kira")

#print(user.name)


class User:
    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        return f"user: {self.name}"
        
        
user = User("Kira")
print(user)


class Team:
    def __init__(self, members):
        self.members = members
        
    def __len__(self):
        return len(self.members)
    
team = Team(["Anna", "Oleh", "Kira"])
print(len(team))