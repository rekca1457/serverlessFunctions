import time
import random
import os
os.chdir(f"{os.getcwd()}\Data")
os.system("HelperModule.exe")

while True:
    # Main variables and values
    Health = 100
    Thirst = 100
    BodyTemp = 97.5
    Day = 0
    Temp = 70
    Weather = "Clear"
    Alive = True
    Action = 0
    CM = False
    Game_Items = ["Bandage", "Water Bottle", "KitKat", "Sandwich", "Gasoline", "M1911", "Barbwire Bat", "Multi-Tool", "Canteen", "Camp Stove"]
    weights =    (  10,           30,          20,         20,         30,       5,         5,             30,          30,         25     )
    weights=(10, 30, 20, 20, 30, 5, 5, 30, 30, 25)
    Weather_Types = ["Clear", "Overcast", "Misty", "Thunder", "Rainy", "Foggy"]
    Inventory = ["Bandage", "Water Bottle", "KitKat"]
    Foods = ["Sandwich", "KitKat"]
    Events = ["Scav Camp", "Wild Dog Attack", "Acid Rain", "Abandoned House", "Nothing", "Hit And Run", "Generator", "Bandit Attack", "Hallucination"]
    weights= (    15,             15,             15,            15,             25,          5,            10,              15,             25      )
    Waters = ["Water Bottle", "Canteen"]
    Tools = ["Camp Stove", "Multi-Tool", "Gasoline", "M1911", "Barbwire Bat"]
    TV = ["My Strange Addiction", "SPongBorb", "Paw Patrol", "Law & Order", "My 500 Pound Life", "Fear Factor"]
    Barbwire_Durabilty = 2
    M1911_Durability = 2

    # Setting up main functions
    def Status():
        global Health
        global Thirst
        global Day
        global Weather
        status = f"[Health: {Health} | Thirst: {Thirst} | Day: {Day} | Weather: {Weather}]"
        print(status)
        breaker = []
        for i in range(len(status)):
            breaker.append("-")
        print(*breaker, sep="")

    def Durability(Weapon):
        global Barbwire_Durabilty
        global M1911_Durability
        if Weapon == "Barbwire Bat":
            Barbwire_Durabilty -= 1
            if Barbwire_Durabilty == 0:
                Inventory.remove("Barbwire Bat")
                Barbwire_Durabilty = 2
        if Weapon == "M1911":
            M1911_Durability -= 1
            if M1911_Durability == 0:
                Inventory.remove("M1911")
                M1911_Durability = 2

    def New_Day():
        global Day
        global Health
        global Thirst
        global Inventory
        global Weather
        global Item
        Weather = random.choice(Weather_Types)
        Day += 1
        Thirst -= 5
        if Thirst < 50:
            Health -= 5
        if Thirst < 0:
            Thirst = 0
        Event = random.choices(Events, weights=(15, 15, 15, 15, 25, 5, 10, 15, 25), k=1)
        Event = random.choice(Event)
        if Event == "Scav Camp":
            Status()
            Item = random.choices(Game_Items, weights=(10, 30, 20, 20, 30, 5, 5, 30, 30, 25), k=1)
            Item = random.choice(Item)
            print("You raided a Scav Camp. You found a " + Item + " in one of the tents.")
            Inventory.append(Item)
            print("")
        if Event == "Wild Dog Attack":
            if "Barbwire Bat" in Inventory:
                Durability("Barbwire Bat")
                if "Camp Stove" in Inventory:
                    Health -= 10
                    Status()
                    print("You were attacked by a wild dog. You took 15 damage and killed the dog. You used your Camp Stove and gained back 5 health.")
                else:
                    Health -= 15
                    Status()
                    print("You were attacked by a wild dog. You took 15 damage and killed the dog.")
            else:
                Health -= 20
                Status()
                print("You were mauled by a wild dog for an hour. You took 20 damage and cry... a lot.")  
        if Event == "Acid Rain":
            Health -= 20
            Status()
            print('It begins to rain acid. You took 20 damage.')
        if Event == "Hit And Run":
            Health -= 30
            Status()
            print('You were hit by a car. You lost two items.')
            try:
                One = random.choice(Inventory)
                try:
                    Inventory.remove(One)
                except:
                    pass
            except:
                pass
            try:   
                Two = random.choice(Inventory)
                try:
                    Inventory.remove(Two)
                except:
                    pass
            except:
                pass
        if Event == "Nothing":
            Status()
            print('You wandered around for a day and did nothing.')
        if Event == "Abandoned House":
            Status()
            Item = random.choices(Game_Items, weights=(10, 30, 20, 20, 30, 5, 5, 30, 30, 25), k=1)
            Item2 = random.choices(Game_Items, weights=(10, 30, 20, 20, 30, 5, 5, 30, 30, 25), k=1)
            Item = random.choice(Item)
            Item2 = random.choice(Item2)
            Inventory.append(Item)
            Inventory.append(Item2)
            print(f"You stumble upon an abandoned home. You found {Item} and {Item2}")
            if "Multi-Tool" in Inventory:
                Item3 = random.choices(Game_Items, weights=(10, 30, 20, 20, 30, 5, 5, 30, 30, 25), k=1)
                Item3 = random.choice(Item3)
                Inventory.append(Item3)
                Inventory.remove("Multi-Tool")
                print(f"You used your Multi-Tool and opened a lockbox. You found {Item3}")
        if Event == "Generator":
            if "Gasoline" in Inventory:
                Health += 50
                Thirst += 20
                if Health > 100:
                    Health = 100
                Status()
                print("You found a generator and some gear. You used your gasoline and stayed the night, gaining 50 health.")
                Inventory.remove("Gasoline")
            else:
                Status()
                print("You found a generator and some gear. Unfortunately, you do not have any gasoline.") 
        if Event == "Bandit Attack":
            if "M1911" in Inventory:
                # No Damage
                Item = random.choice(Inventory)
                Inventory.remove(Item)
                Status()
                print(f"You were atatcked by a group of bandits. You used your M1911 and brutally executed each member and lost your {Item}")
            else:
                Health -= 10
                try:
                    Item = random.choice(Inventory)
                    Inventory.remove(Item)
                except:
                    pass
                Status()
                print(f"You were atatcked by a group of bandits. Without your weapon you were scared and curled up unto a ball, taking 10 damage. You lost your {Item}")
        if Event == "Hallucination":
            Status()
            print(f"While wandering, you hallucinated and found a TV in the sand. You sat down and watched {random.choice(TV)} for {random.randint(1,14)} hours.")

    def Bandage():
        global Health
        global Inventory
        Inventory.remove("Bandage")
        Health += 25
        if Health > 100:
            Health = 100

    def Food():
        global Health
        global Inventory
        Inventory.remove(Item)
        Health += 10
        if Health > 100:
            Health = 100

    def Water():
        global Thirst
        global Inventory
        global Health
        if Item == "Water Bottle": 
            try:
                Inventory.remove("Water Bottle")
            except ValueError:
                pass
            Thirst += 25
            Health += 5
        if Item == "Canteen":
            try:
                Inventory.remove("Canteen")
            except ValueError:
                pass
            Thirst += 40
            Health += 10
        if Thirst > 100:
            Thirst = 100
        if Health > 100:
            Health = 100
    def Write_Text(String):
        for char in String:
            print(char, end='')
            time.sleep(.15)

    # Background and Starting Information
    print("""
            Welcome to Ashton, Matt, and Zach's survival game
            
            You are a survivor in Death Valley after an apocolypse
            
    Important Info:
        1. You lose thirst everyday, get below 50 thirst and you lose 5 health a day.
        2. You can only use one item per day (Bandage, Canteen, etc)
        3. Some items are not independently usable, and require an event to be used
        4. You start with a bandage, water bottle, and a KitKat
        5. All weapons have two uses before they break
        6. Each day, a random event takes place
        7. The current game record is: 61 days

    Keybinds:
        _________________________________
        |                                 |
        | [Enter]- Progress to next day   |
        | [Inventory]- Open Inventory     |
        | [E]- Inventory                  |
        |_________________________________|
        
        Note: When inside the inventory, you must type the item name you want (Case Sensitive)
        """)

    # Main running sequence
    while Alive == True:
        if Action == 1:
            New_Day()
            Action = 0
        if Health > 100:
            Health = 100
        if Health <= 0:
            Healh = 0
        if Thirst > 100:
            Thirst = 100
        if Thirst <= 0:
            Thirst = 0
    
    # Main Function for Day Progression
        INPUT = input()
        if INPUT == "":
            New_Day()
    
    # Actions the user can make anytime
        if INPUT == "e" or INPUT == "E":
            print(f"Your items are: {Inventory}")
            Item = input("What item would you like to use? (Press Enter to Skip): ")
            if Item == "Bandage" or Item == "bandage":
                Bandage()
                print(f"Your Health is now at: {Health}")
                print("")
                Action = 1
            if Item in Foods:
                Food()
                print(f"{Item} consumed. Your Health is now at: {Health}")
                print(" ")
                Action = 1
            if Item in Waters:
                Water()
                print(f"{Item} consumed. Your Thirst is now at: {Thirst} \n")
                Action = 1
            if Item == "":
                pass
                
    # Listener for cheat mode
        if INPUT == "CM":
            CM = not(CM)
            print(CM)
        if CM == True:
            if INPUT == "+":
                Health += 25
                print("Your Health is now at: "+ str(Health))
            if INPUT == "-":
                Health -= 25
                print("Your Health is now at: "+ str(Health))
                
    # Death function
        if Health <= 0:
            Alive = False
            print("\n")
            print("------------------------------------")
            print(f"You Died. You survived {Day} days.")
            print("   Press 'Enter' to start again    ")
            print("------------------------------------")
            Day = 0
            break