import random

class Suspect:
    def __init__(self, name, role, description, alibi):
        self.name = name
        self.role = role
        self.description = description
        self.alibi = alibi
        
        
class Mystery:
    def __init__(self):
      self.suspect1 = Suspect(
      name = "Greg",
      role = "sidequest host",
      description = "tall teenage guy with green eyes and brown hair. wears glasses and loves collecting caps",
      alibi = "he was doing the campfire at the time the murder happened, so he was gone"
    )
      self.suspect2 = Suspect(
      name = "Lorelei",
      role = "victims sister",
      description = "blonde with blue eyes usually very kind and has a 2000s y2k style",
      alibi = "she is the victims sister and she was reading in her tent when it happened she only heard the scream"
    )

      self.suspect3 = Suspect(
      name = "Milo",
      role = "the sunshine in the group",
      description = "always very happy has flowy layers and brown hair and brown eyes, he got a hood with fur",
      alibi = "he claims he wouldnt do such a thing and he was hunting when it happened"
    )    
 
      suspects = [self.suspect1, self.suspect2, self.suspect3]
 
      self.culprit = random.choice(suspects)
    
    def hints(self):
         if self.culprit == self.suspect1:
          print("suspect left behind a cap and a slight cologne scent")
         
         elif self.culprit == self.suspect2:
          print("suspect dropped their bracelet and a y2k bag")
         
         else:
           print("suspect left behind a small piece of fur and a smoking bullet")
   
    def show_suspect(self):
        print ("Suspects")
        print(f"1 {self.suspect1.name}: {self.suspect1.description}")
        print(f"2 {self.suspect2.name}: {self.suspect2.description}")
        print(f"3 {self.suspect3.name}: {self.suspect3.description}")
    
    def get_user(self, choice):
          if choice.strip().lower() == self.culprit.name.lower():
              return "you are right!"
          else:
              return "wrong"
         
game = Mystery()
game.show_suspect()
game.hints()
user_choice = str(input("write your choice. which one do you choose? "))

print(game.get_user(user_choice))