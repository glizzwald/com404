

def is_league_united(hero1, hero2):
    if (hero1 == "Superman" and hero2 == "Wonder Woman"):
        return True
    elif (hero1 == "wonder woman" and hero2 == "Superman"):
        return True
    else:
        return False

def decide_plan(hero1, hero2):
    if(is_league_united(hero1, hero2)== True):
        return "time to save the world"

    else:
        return "we must unite the league"

def run():
    print("enter a name for hero1")
    hero1 = input()
    print("enter a name for hero2")
    hero2 = input()

    print("pick league or plan")
    choice = input()

    if (choice == "league"):
        print(is_league_united(hero1, hero2))
    elif (choice == "plan"):
        print(decide_plan(hero1, hero2))
    else:
        print("invalid command.")



run()


