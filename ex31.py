print("""You enter a dark room with two doors.
Do you go through door #1 or door #2?""")

door = input("> ")

if door == "1":
    print("There's a smaller door.")
    print("What do you do?")
    print("1. Open it.")
    print("2. Close the bigger door.")

    door = input("> ")

    if door == "1":
        print("A dwarf punches you in the face and closes the door. Nailed it!")
    elif door == "2":
        print("A dwarf bites your ear and can't take it off you. Good luck!")
    else:
        print(f"Well, doing {door} is probably better.")
        print("Did you see a dwarf walking around? Nevermind...")

elif door == "2":
    print("Innsmouth there, what do you do?")
    print("1. Investigate the town.")
    print("2. Walk around.")
    print("3. Get the hell out of there.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("You get massacrated, stranger!")
        print("Game over.")
    else:
        print("While running, a dwarf suddenly appears and kicks you in the nuts.")
        print("Ouch!")
else:
    print("You're suddenly naked, how f***** are you?")
