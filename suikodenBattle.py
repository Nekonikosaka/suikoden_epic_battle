
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

from random import choice

class Army :
    def __init__ (self,name,number_of_soldier = 1000, level = 1):
        self.name = input("Enter player army name : \n")
        self.name = self.name.capitalize()
        self.number_of_soldier = int(number_of_soldier)
        self.level = level
        print("The player army name is {} , level {}, has {} men.".format(self.name,self.level,self.number_of_soldier))

    def attack (self,attack):
        attack = input ("Choose your move : \n Charge attack (c)\n Magic attack (m)\n Bow attack (b) \n")
        if attack == "c" or attack == "C":
            print("{} attacks : Charge attack (c) ".format(self.name))
        elif attack == "m" or attack == "M":
            print("{} attacks : Magic attack (m) ".format(self.name))
        elif attack == "b" or attack == "B":
            print("{} attacks : Bow attack (b) ".format(self.name))
        return attack.capitalize()


class Ennemy :
    def __init__ (self,name="Kwanda Rossman army",number_of_soldier = 1500, level = 1):
        self.name = name
        self.number_of_soldier = int(number_of_soldier)
        self.level = level
        print("You are fighting {} , level {}, {} men.".format(self.name,self.level,self.number_of_soldier))

    def attack (self,attack):
        attack_type = ["C", "M", "B"]
        attack = choice(attack_type)
        
        if attack == "C":
            print("{} attacks : Charge attack (c) ".format(self.name))
        elif attack == "M":
            print("{} attacks : Magic attack (m) ".format(self.name))
        elif attack == "B":
            print("{} attacks : Bow attack (b) ".format(self.name))

        return attack



print("****************** SUIKODEN EPIC BATTLE ******************")

army2=Army("")
army1=Ennemy()
print("{} VS {}".format(army1.name,army2.name))

nb1 = army1.number_of_soldier
nb2 = army2.number_of_soldier


while True : 

    a = army2.attack("")
    b = army1.attack("")
    
    if a == b :
        print("This is a draw")

# case when player wins (army2 : a)
    elif (a == "B" and b == "M") or (a == "M" and b == "C") :
        nb1 = nb1 - 100
        print("{} wins!".format(army2.name)) 
        print("{} has lost 100 soldiers, remaining {}".format(army1.name,nb1))

# case when computer wins (army1 : b)
    else :
        nb2= nb2 - 100
        print("{} wins!".format(army1.name)) 
        print("{} has lost 100 soldiers, remaining {}".format(army2.name,nb2))
        
    if nb2 <= 0 :
        print("{} wins!!!".format(army1.name))
        break

    elif nb1<= 0 :
        print("{} wins!!!".format(army2.name))
        break