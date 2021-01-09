inventory=[]
max_hp=150
hp=150
name=""
hero_class= ""
attack = 6
defense = 6
n_turn = 0
xp=0
lv=1

#Intro
name=input("---- AVANTIA'S ADVENTURE ----\nFor those who love a good adventure\n\nWrite your hero's name to Start\n-")
print("KASSANDRIA: It's a pleasure to meet you finally, {}. My name is Kassandria, Queen of Avantia and I bring you here\nbecause you have the potential to save our reign from the caos.".format(name))
kassa_q1 = input("Will you fight for us?\n\n-")
while not (("yes" in kassa_q1.casefold()) or ("ok" in kassa_q1.casefold())):
    print()
    kassa_q1 = input("KASSANDRIA: Please hero... WE REALLY NEED YOU? Will you help us? Yes or no?\n\n-")
print("KASSANDRIA: Oh {}! A hero has born! In that case let me explain your quest. 3 years ago, Galandrion, the king of the\nEvelonds created a military revolution and killed my husband, King Nefesto...".format(name))
print("*A tear slowly downs Kassandria's cheek.*")
print("Kassandria: {}, if we want to beat Galandrion, we need to collect the 4 crystals of magic.\nAll what I can do is to give you one of the Relics from our family, what do you want?\n\n*There are three objects in front of you:*\n-An Ancient book.\n-A Gold Sword.\n-A flute\n".format(name))
object = input("-")
object_rec = None
while object_rec == None:
    if "book" in object.casefold():
        print("KASSANDRIA: Oh... Looks like you're a powerful mage!\n")
        object_rec = 1
        hero_class="Mage"
        attack+=5
        max_hp=150
        inventory.append("Ancient Book")
    elif "sword" in object.casefold():
        print("KASSANDRIA: A brave warrior is in front of me!\n")
        object_rec = 1
        hero_class="Warrior"
        attack+=3
        defense+=2
        max_hp=200
        inventory.append("Gold Sword")
    elif "flute" in object.casefold():
        print("KASSANDRIA: The music of this bard will save Avantia!\n")
        object_rec = 1
        hero_class="Bard"
        attack+=1
        defense+=4
        max_hp=150
        inventory.append("Flute")
    else:
        object = input("KASSANDRIA: I don't have that, please choose and object:\n-")
print("{0} - {1} lv {2}\nHP: {3}\nAttack: {4}\nDefense: {5}\n".format(name,hero_class,lv,max_hp,attack,defense))
print("KASSANDRIA: Enter this portal to go to the Noiseless Woods and start looking for the first Avantia's Crystal\n *A portal is created in front of you by Kassandria*\nKASSANDRIA: Good luck, {}.\n".format(name))

#Instructions
tutorial = input("DO YOU WANT TO SEE THE TUTORIAL?\n-")
if "y" in tutorial.casefold():
    print(input("HOW TO PLAY AVANTIA'S ADVENTURE\nIn this game you need to write what you want to do. Use 'Inspect' to check or see something,\n'Walk' or 'Go' to move, 'Talk' to interact with people, etc!\nPRESS ENTER TO END THE TUTORIAL"))

#Forest
print("---- NOISELESS FOREST ----\n*After crossing the portal, the warm room turns into a cold forest full of trees,\nnear you, there's nothing more than a girl crying on the ground*\n")
forest_done = False
jenna_heal=False
import random
hp = max_hp
while forest_done== False:

    d1=input("You're in the middle of the clearing of Noiseless Forest\n-")
    if ("inspect" in d1.casefold()) and ("girl" in d1.casefold()):
        print("*The girl looks really tired and worried for something... would be a good idea to talk with her.*")
    elif (("area" in d1.casefold()) or ("around" in d1.casefold()) or ("place" in d1.casefold())) and ("inspect" in d1.casefold()):
        print("*There are 3 possible ways:\n-A way to the West full of an extrange fog.\n-On the North, the girl is on a path who goes to a dangerous pass.\nThere's a swamp on the East.\n")
    elif (("woman" in d1.casefold()) or ("girl" in d1.casefold()) or ("jenna" in d1.casefold())) and ("talk" in d1.casefold()) and (jenna_heal==True) and ("Jenna's Necklace" in inventory) and ("Boots" in inventory):
        print("JENNA: Good luck with your hourney, hero! Let me help you...")
        print("*Your life is now {}.*".format(hp))
        hp = max_hp
    elif (("woman" in d1.casefold()) or ("girl" in d1.casefold()) or ("jenna" in d1.casefold())) and ("talk" in d1.casefold()) and (jenna_heal==True) and ("Jenna's Necklace" in inventory):
        print("JENNA: My necklace! Thanks hero! As a reward, take my boots, you'll be able to take the East path with them")
        print("*You've received a pair of boots!*")
        inventory.append("Boots")
        hp = max_hp

    elif (("woman" in d1.casefold()) or ("girl" in d1.casefold()) or ("jenna" in d1.casefold())) and ("talk" in d1.casefold()) and (jenna_heal==True):
        print("JENNA: Let me heal your wounds... That necklace was a present from my parent, please, help me!")
        hp = max_hp
        print("*Your life is now {}.*".format(hp))
    elif (("woman" in d1.casefold()) or ("girl" in d1.casefold())) and ("talk" in d1.casefold()):
        print("JENNA: Who... Snif... Who are you? Snif... {}? A group of goblins attacked me and have stolen my necklace,\nthey took that path to the north... Please hero, bring it back to me!")
        jenna_heal=True
    elif (("go" in d1.casefold()) or ("walk" in d1.casefold())) and ("north" in d1.casefold()):
        print("*You go to the north*")
        f1=input("The pass looks dangerous and probably someone attacks you, do you want to continue?\n")
        if "yes" in f1.casefold():
            n_goblins=random.randint(1,3)
            hp_goblins=(n_goblins*15)
            if n_goblins == 1:
                print("A Goblin attacks you!")
                plur=""
            else:
                print("{0} Goblins attack you!".format(n_goblins))
                plur="s"
            con1=input("Press Enter to start fighting. (On combat, use 'Attack' to fight, or 'Run' to escape.)")
            print()
            while ((hp>0) and (hp_goblins>0)):
                print("{0}: {1} HP\n{2} Goblin{3}: {4} HP\n".format(name,hp,n_goblins,plur,hp_goblins))
                n_turn += 1
                turn=input("Turn {}\n".format(n_turn))
                if "run" in turn.casefold():
                    percentage_to_run=random.randint(1,20)
                    if percentage_to_run>5:
                        print("You runaway from the combat!")
                        n_turn=0
                        break
                    else:
                        print("You can't escape from here!\nYou receive{} of damage.".format(5*n_goblins))
                        hp-=5*n_goblins
                elif "attack" in turn.casefold():
                    ata1=attack+(random.randint(0,attack))
                    hp_goblins-=ata1
                    print("You make {} of damage!".format(ata1))
                    for i in range(0,n_goblins):
                        dmg1=5+random.randint(0,5)
                        hp-=dmg1
                        print("You receive {0} damage from Goblin {1}".format(dmg1,i+1))
            if hp<=0:
                print("\nYou lose...")
                n_turn=0
            elif hp_goblins<=0:
                lootv=random.randint(1,20)
                loot=n_goblins*lootv
                print()
                if loot > 15:
                    print("You've received the Jenna's Necklace!")
                    inventory.append("Jenna's Necklace")
                xp+= 10*n_goblins
                print("You won! {0} received {1} exp.".format(name,10*n_goblins))
                n_turn=0
                if xp >=50:
                    lv+=1
                    attack+=1
                    defense+1
                    max_hp+=50
                    xp=0
                    print("{0} is now level {1}".format(name,lv))
        else:
            continue
    elif (("go" in d1.casefold()) or ("walk" in d1.casefold())) and ("south" in d1.casefold()):
        print("*You go to the south*")
    elif (("go" in d1.casefold()) or ("walk" in d1.casefold())) and ("east" in d1.casefold()):
        print("*You go to the east*")
    elif (("go" in d1.casefold()) or ("walk" in d1.casefold())) and ("west" in d1.casefold()):
        print("*You go to the west*")
