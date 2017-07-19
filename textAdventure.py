start = '''
You have been stranded on an island.  This island
is uninhabited and you don't know how you got
there.  You have only two options: Stay on the
island and wait for help or leave the island and
search for land.
'''
stay = '''
Now that you've decided to stay you went
searching the island.  On your search you found
some sticks.  You can make a fire with these
sticks or you can make a fishing pole with these
sticks.
'''
leave = '''
Now that you've decided to leave you must figure
out how you want to escape the island.
'''
fire = '''
You've used your sticks to make a fire.  With
this fire you were able to send up smoke signals
or cook a random island animal you've captured.
'''
fishing_pole = '''
You've used your sticks to make a fishing pole.
Once you caught your fish you ate them and they
made you sick.  You died.
'''
swim = '''
You are swimming away from the island now and
you approach a shark.  The shark eats you and
you die. :(
'''
boat = '''
You have decided to build a boat and sailed
away from the island to find help. Now
you must pick a direction to sail in.
'''
east = '''
You sailed east and you ran into a sea storm
and your boat was lost at sea, never to be
found.  Needless to say you died. :(
'''
west = '''
You sailed west and you saw a  cruise ship,
presumably with pleanty of people who can help,
and some more land that might be inhabited.
'''
ship = '''
You sailed to the cruise ship and signaled to
them that you were lost and need help.  The gladly
extended a life raft to pull you in and you were
rescued.  HOORAY!
'''
land = '''
The land you sailed to was another island.  This
island is uninhabited as well.  You must start this
entire process all over again. :(
'''
smoke = '''
You've successfully sent some smoke signals.  Luckily
a helicopter passing by was able to decipher these
signals and send help.  You have been saved and taken
back to civilization.  HOORAY!
'''
cook = '''
You've successfully cooked this animal to perfection.
In a shocking turn of events, a tribe appears because
they smelled the cooking meat.  The tribe beats you
mercilessly for eating a sacred animal and they
imprison you for the rest of your days.
'''
def Begin():
    print(start)

    print("Type 'stay' to go stay on the island or 'leave' to leave the island.")
    user_input = input()
    if user_input == "stay":
        print(stay)
        print("Type 'fire' to make a fire with the sticks you found or 'fishing_pole' to make a fishing pole with the sticks you found.")
        user_input = input()
        if user_input == "fire":
            print(fire)
            print("Type 'smoke' to make a smoke signal or 'cook' to cook the animal.")
            user_input = input()
            if user_input == "smoke":
                print(smoke)
            if user_input == "cook":
                print(cook)
        if user_input == "fishing_pole":
            print(fishing_pole)


    if user_input == "leave":
        print(leave)
        print("Type 'swim' to swim off the island or 'boat' to build a boat and sail away.")
        user_input = input()
        if user_input == "swim":
            print(swim)
        if user_input == "boat":
            print(boat)
            print("Type 'east' to sail east or 'west' to sail west.")
            user_input = input()
            if user_input == "east":
                print(east)
            if user_input == "west":
                print(west)
                print("Type 'ship' to sail to the cruise ship or 'land' to sail to the land.")
                user_input = input()
                if user_input == "ship":
                    print(ship)
                if user_input == "land":
                    print(land)
                    Begin()

Begin()
