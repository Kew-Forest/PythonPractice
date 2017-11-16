"""
 You are an Elfin warrior:
Life: 80	Strength: 76	Speed: 85	Gold: 0

You are in a dungeon and come to a fork. You can go right or left.

If you go left you come to a room with a pot of 200 gold and a magic bracelet which increases your Strength by 10. Then you must go back to the fork and choose again.
   
If you go right, you are attacked by a Gorgon: 
Life: 50	Strength: 85	Speed: 10	Gold: 500	

You can choose to fight or flee:
 Flee: 
If your speed is greater than the Gorgon’s, you retreat back to the fork
If not, you lose 50 life and choose again

Fight:
If your Strength is greater, and your Life is greater: you win collect the gold and move on
Your strength is less and your life is more or strength is more, life is less: you lose 20 life points and choose again
Your strength is less and your life is less: you lose 50 life points and choose again

If your life goes below 0 you die.

Test for Winning
left - our str and gold increases
right
fight
win passes test

Test for death
right
fight - lose 20 li
fight - lose 20 li
fight - lose 50 life and die
death passes test

Test for just going around not winning or dying
right
flee
left
right
flee
right
flee
right
not dyting or winning passes test


"""

elf = {"li":80,"str":76,"sp":85,"g":0}
gorgon = {"li":50,"str":85,"sp":10,"g":500}
goldpot = 200
bracelet = 10


def fork():
    """ the fork """
    choice = input("You are at a fork. Do you go right or left?")
    if choice == "left":
        goldroom()
    elif choice == "right":
        gorgonroom()
    else:
        print("Please enter 'right' or 'left'")
        fork()

def goldroom():
    global goldpot
    global bracelet
    elf["g"] += goldpot
    elf["str"] += bracelet
    
    
    print("You have gianed",goldpot,"in gold. and now you go back to the fork.")
    goldpot = 0
    bracelet = 0
    fork()
    
def gorgonroom():
    """gorgon"""
    choice = input("you are attacked by a Gorgon, do you fight or flee?")
    if choice == "flee":
        if elf["sp"] > gorgon["sp"]:
            print("You have fled the gorgon")
            fork()
        else:
            print("the gorgon got you! you lose 50 life!")
            elf["li"] -= 50
            gorgonroom()
    elif choice == "fight":
        if elf["str"] > gorgon["str"] and elf["li"] > gorgon["li"]:
            print("you win! collect 500 gold and move on")
            elf["g"] += gorgon["g"]
            gorgon["g"] = 0
            gorgon["li"] = 0
            gorgon["str"] = 0
        elif (elf["str"] > gorgon["str"] and elf["li"] < gorgon["li"]) or (elf["str"] < gorgon["str"] and elf["li"] > gorgon["li"] ):
             print("you lose 20 life!")
             elf["li"] -= 20
             if checkdeath(elf["li"]):
                 return
             gorgonroom()
        else:
            print("you lose 50 life!")
            elf["li"] -= 50
            if checkdeath(elf["li"]):
                 return
            gorgonroom()
    else:
        print("please enter 'fight' or 'flee'")
        gorgonroom()
    
    
def checkdeath(life):
    if life > 0:
        print("You are injured but alive. You have "+str(life)+" left")
        return False
    else:
        print("you are dead. Game over.")
        return True
  
    
    
    
    
fork()    