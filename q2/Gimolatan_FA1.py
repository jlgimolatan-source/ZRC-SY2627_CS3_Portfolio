
#MAY I HAVE YOUR ATTENTION HERE SIR!!!!
#I have read the criteria and it says i am allowed to add my own twist of creativity in my code.
#THEREFORE, i decided to add "pubtype" which stands for PUBLICATION TYPE
#Basically, the users can input what their text is like :3
#their text could be a general group (Publication)
#or could belong to specific smaller sub groups (books or magazines)
#so i created my code to specifically need the pubtype from the texts
#i hope you understand what i mean sir, and technically this is still a simple code
#i just added a little something to make it FUN



#So this is the parent class which is gonna have two children! congratulations mama bear :3
class Publication:
    
    def __init__(self, pubtype, title, author):
        self.__pubtype = pubtype
        self.__title = title
        self.__author = author

    def get_pubtype(self):
            return self.__pubtype
        

    def get_title(self):
            return self.__title

    def get_author(self):
            return self.__author

    def set_title(self, title):
            self.__title = title

    def set_author(self, author):
            self.__author = author

    def display_info(self):
            print(f"Your {self.__pubtype} has the following details:")
            print(f"Title: {self.__title}")
            print(f"Author: {self.__author}")





#this is the first child class and its parent is Publication    
class Book(Publication):
    
    def __init__(self, pubtype, title, author, number_of_pages):
        super().__init__(pubtype, title, author)
        self.__number_of_pages = 0
        self.set_number_of_pages(number_of_pages)

    def get_number_of_pages(self):
        return self.__number_of_pages

#hi sir, in the class diagram you said number_pages and not number_of_pages, 
# idk why u did that or thats suppose to be on purpose but i used number_of_pages anyways because 
# it makes more sense to me atleast. sorry sir Bon :)
    def set_number_of_pages(self, number_of_pages):
        if number_of_pages <= 0:
            print("Error: Your book can't have negative or zero pages.")
            print("The number of pages will remain the same until you enter a valid value.")
        else:
            self.__number_of_pages = number_of_pages

    def display_info(self):
        super().display_info()
        print(f"Number of pages: {self.__number_of_pages}")






#this is the second child class and its parent is ALSO Publication    
class Magazine(Publication):

    def __init__(self, pubtype, title, author, issue_number):
        super().__init__(pubtype, title, author)
        self.__issue_number = 0
        self.set_issue_number(issue_number)

    def get_issue_number(self):
        return self.__issue_number

    def set_issue_number(self, issue_number):
        if issue_number <= 0:
            print("wow, you know full well your issue number cant be a negative or zero. Try again.")
        else:
            self.__issue_number = issue_number

    def display_info(self):
        super().display_info()
        print(f"Issue Number: {self.__issue_number}")



#Creating the objects for meh classes.
text1 = Publication("Publication", "The amazing world of JANE", "Jane G.")
text2 = Book("Book", "The wings you'll never have", "Alex A.V.", 760)
text3 = Magazine("Magazine", "Victoria's Secret Revealed", "Vouge A.", 505)



#Printing the informations :3
#i removed the extra print command sir cuz it was redundant and my display_info already does that job.
text1.display_info()
print()
text2.set_number_of_pages(-760)
text2.display_info()
print()
text3.display_info()


