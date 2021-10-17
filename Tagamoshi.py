import math
import random

hunger = 110
stamina = 90
happyness = 110
day = 1

race = "dog"
state = "live"
playerName = "Player"
name = "placeholder"
activity = "nothing"
cause = "nothing lol"

cat = "cat"
dog = "dog"
fox = "fox"
mice = "mice"
feed = "feed"
play = "play"
sleep = "sleep"

playerName = input("Whats your name " + playerName + " ? ")
name = input("Whats the pet name " + playerName + " ? ")
race = input("Whats " + name + " race? (Cat, Dog, Fox or Mice?)")


def printRace():
    # prints the race selected before
    if(race.lower() == dog.lower()):
        print(" |\---/| ")
        print(" | o_o | ")
        print("  \_^_/ ")
    elif(race.lower() == cat.lower()):
        print("  /\_/\ ")
        print(" ( o.o ) ")
        print("  > ^ < ")
    elif(race.lower() == fox.lower()):
        print("  ^...^ ")
        print(" <_o o_> ")
        print("   \_/  ")
    elif(race.lower() == mice.lower()):
        print(" () - () ")
        print("  \o o/  ")
        print("    ~   ")


def printBasics():
    print("Your pet "+name+" has: ")
    print(str(hunger)+" points of hunger")
    print(str(stamina)+" points of stamina")
    print(str(happyness)+" points of happyness")


while(state != "dead"):

    print("Today is day "+str(day))
    day += 1
    if(hunger >= 70 and stamina <= 90):
        stamina += 10
    if(hunger >= 110):
        hunger == 100
    if(stamina >= 110):
        stamina == 100
    if(happyness >= 110):
        happyness == 100

    happyness -= 10
    hunger -= 10

    if(happyness == 0):
        state = "dead"
        cause = "ran out of happyness"
    if(hunger == 0):
        state = "dead"
        cause = "ran out of hunger"
    if(stamina == 0):
        state + "dead"
        cause = "ran out of stamina"

    printRace()

    printBasics()

    # print(activity)
    activity = input("What you what to do now? (Feed, Play, Sleep) ")
    # print(activity)
    if (activity.lower() == feed.lower()):
        print("feeded")
        hunger += 20
        if(hunger >= 110):
            hunger == 100

    elif (activity.lower() == play.lower()):
        print("played")
        stamina -= 10
        happyness += 20
        if(happyness >= 110):
            happyness == 100

    elif(activity.lower() == sleep.lower()):
        stamina += 10
        if(stamina >= 110):
            stamina == 100

    else:
        print("sorry i didnt understanded what you typed")

    if (state == "dead"):
        print("Your pet died because it " + cause + "...")
        print("and your pet survived " + str(day) + " days")
        break
