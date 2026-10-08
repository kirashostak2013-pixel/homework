#class Book:
    #def __init__(self, title, pages):
      #  self.title = title
     #   self.pages = pages

    #def __str__(self):
   #     return f"title: {self.title}, pages: {self.pages}"
    
  #  def __len__(self):
 #       return self.pages
    
#book = Book("Harry Potter", 350)

#print(book)


class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        
    def show_info(self):
        print(self.name, self.age, self.grade)
        
    def is_adult(self):
        if self.age >= 18:
            return True
        else:
            return False
   
student1 = Student("Максим", 17, 10)

student1.show_info()
print(student1.is_adult())