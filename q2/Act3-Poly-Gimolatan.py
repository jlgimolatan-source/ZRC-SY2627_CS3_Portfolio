

class Warrior:

    def special_move(self):
        print("Warrior swings a mighty sword!")



class Mage:

    def special_move(self):
        print("Mage casts a powerful spell!")



class Archer:

    def special_move(self):
        print("Archer shoots a precise arrow!")



def perform_move(character):
     character.special_move()


char1 = Warrior()
char2 = Mage()
char3 = Archer()


characters = [char1, char2, char3]

for character in characters:
    perform_move(character)