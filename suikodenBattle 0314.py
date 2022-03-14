
""""
2 armees a qui ont demandera de donner un pseudo
Bataille suikoden 1

Regles
1000 hommes chacun

Archerie plus fort que Magie 
Magie plus fort que charge
Charge plus fort que Archerie

Avance : 
Charge Vs Archerie : 10% perte face a archerie
Possibilite de checker la prochaine attaque de l'ennemi 
 - voleur (50% chance efficace)
 - ninja (100%)
 - Stratege (boost force charge (+25% sur deux tours))
 - Armee dragon (une fois, perd face a fleche)

Celui qui perd tous ses hommes a perdu
"""
# coding : utf-8

from random import choice,randrange

attack_type = ["C", "M", "B"]

class Army :
    def __init__ (self,name= 'Player',number_of_soldier = 1000, level = 1):
        
        if name == "" :
            self.name = input("Enter player army name : \n")
        else :
            self.name = name 
        
        self.name = self.name.capitalize()
        self.number_of_soldier = int(number_of_soldier)
        self.level = level


    def attack (self,attack):
        attack = input ("Choose your move : \n Charge attack (c)\n Magic attack (m)\n Bow attack (b) \n")
        if attack == "c" or attack == "C":
            print("{} attacks : Charge attack (c) ".format(self.name))
        elif attack == "m" or attack == "M":
            print("{} attacks : Magic attack (m) ".format(self.name))
        elif attack == "b" or attack == "B":
            print("{} attacks : Bow attack (b) ".format(self.name))
        return attack.capitalize()


    def attackAuto (self,attack):
        attack = choice(attack_type)
        
        if attack == "C":
            print("{} attacks : Charge attack (c) ".format(self.name))
        elif attack == "M":
            print("{} attacks : Magic attack (m) ".format(self.name))
        elif attack == "B":
            print("{} attacks : Bow attack (b) ".format(self.name))

        return attack


print("****************** SUIKODEN EPIC BATTLE ******************")


army1=Army("Ennemy",number_of_soldier=1000,level=1)

if army1.level == 1 :
    army1.name ="Kwanda Rossman"
    army1.number_of_soldier=1500
    attack_type = ["C", "C", "C", "B"]

    
elif army1.level== 2 :
    army1.name ="Milich Openheimer"
    army1.number_of_soldier=1700   
    attack_type = ["M", "M", "M", "B"]

army2=Army("")
print("The player army name is {} , level {}, has {} men.".format(army2.name,army2.level,army2.number_of_soldier))
print("You are facing {}'s army , level {}, has {} men.".format(army1.name,army1.level,army1.number_of_soldier))

print("{} VS {}".format(army1.name,army2.name))

nb1 = army1.number_of_soldier
nb2 = army2.number_of_soldier


while True : 

    a = army2.attack("")
    b = army1.attackAuto("")
    looserLoss = randrange(80,120)
    winnerLoss = randrange(0, int(looserLoss * 10/100))
    drawLoss = randrange(60,100)

    if nb1 <= drawLoss or nb1 <= looserLoss or nb1 <= winnerLoss:
        nb1 = 0
    elif nb2 <= drawLoss or nb2 <= looserLoss or nb2 <= winnerLoss:
        nb2 = 0
    else :
        if a == b :
            print("This is a draw")

            nb1 = nb1 - drawLoss
            nb2 = nb2 - drawLoss
            
            print("{} has lost {} soldiers, remaining {}".format(army1.name,drawLoss,nb1))
            print("{} has lost {} soldiers, remaining {}".format(army2.name,drawLoss,nb2))
    

# case when player wins (army2 : a)
        elif (a == "B" and b == "M") or (a == "M" and b == "C") :
            nb1 = nb1 - looserLoss
            print("{} wins!".format(army2.name)) 
            print("{} has lost {} soldiers, remaining {}".format(army1.name,looserLoss,nb1))
        
        elif (a == "C" and b == "B"):
            nb1 = nb1 - looserLoss
            nb2 = nb2 - winnerLoss
            print("{} wins!".format(army2.name)) 
            print("{} has lost {} soldiers, remaining {}".format(army1.name,looserLoss,nb1)) 
            print("{} has lost {} soldiers, remaining {}".format(army2.name,winnerLoss,nb2))



# case when computer wins (army1 : b)

        elif (b == "C" and a == "B"):
            nb2 = nb2 - looserLoss
            nb1 = nb1 - winnerLoss
            print("{} wins!".format(army1.name)) 
            print("{} has lost {} soldiers, remaining {}".format(army2.name,looserLoss,nb2)) 
            print("{} has lost {} soldiers, remaining {}".format(army1.name,winnerLoss,nb1))


        elif (b == "B" and a == "M") or (b == "M" and a == "C") :
            nb2 = nb2 - looserLoss
            print("{} wins!".format(army1.name)) 
            print("{} has lost {} soldiers, remaining {}".format(army2.name,looserLoss,nb2))

        else :
            print("Please select a valid action")
            
    if nb2 <= 0 :
        print("{} wins with {} soldier(s) left".format(army1.name,nb1))
        break

    elif nb1<= 0 :
        print("{} wins with {} soldier(s) left".format(army2.name,nb2))
        break