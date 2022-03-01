# coding : utf-8
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


from random import choice

attack_type = ["Charge attack (c)", "Magic attack (m)", "Bow attack (b)" ]

class Army :
    def __init__(self,name,number_of_soldier = 1000, level = 1):
        self.name = input("Enter player army name : \n")
        self.name = self.name.capitalize()
        self.number_of_soldier = number_of_soldier
        self.level = level
        print("The player army name is {} , level {}, has {} men.".format(self.name,self.level,self.number_of_soldier))

    def attack (self, hand):
        self.attack = input ("Choose your move : \n Charge attack (c)\n Magic attack (m)\n Bow attack (b)")
        if self.attack == "c" or self.attack == "C":
            self.hand = 0
        elif self.attack == "m" or self.hand == "M":
            self.hand = 1
        elif self.attack == "b" or self.hand == "B":
            self.hand = 2
#        return self.hand
        




def game_start ():
    print("****************** SUIKODEN EPIC BATTLE ******************")
    army1=Army()
    army2=Army()
    print("{} VS {}".format(army1.name,army2.name))
    
    army2.attack()
    army1.self.hand = choice(attack_type)
    
    print("{} attacks : {} ".format(army1.name, army1.attack))
    print("{} attacks : {} ".format(army2.name, army2.attack))

    if army1.hand == army2.hand :
        print("This is a draw")
    elif army2.hand - army1.hand >= 0 or army1.hand - army2.hand == -2 :
        print("{} wins!".format(army2.name)) 
    else :
        print("{} wins!".format(army1.name)) 

game_start()

"""
charge < magic < arrow
arrow < charge
0 < 1 < 2
2 < 1
si b=a => draw (25% / 25%)
si b - a > 0 or b-a = -1 => a wins
sinon b wins
"""




