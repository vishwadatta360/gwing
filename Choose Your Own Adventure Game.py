def start_game():
    print("Welcome to 'The Whispering Woods' Adventure!")
    print("You find yourself at the edge of a dense, ancient forest. A worn path leads deeper inside.")
    print("The air is cool and a strange, faint melody seems to drift from within the trees.")
    print("\nWhat do you do?")
    print("1. Follow the path into the forest.")
    print("2. Look for another way around the forest.")

    choice = input("Enter your choice (1 or 2): ")
    if choice == '1':
        enter_forest()
    elif choice == '2':
        go_around_forest()
    else:
        print("Invalid choice. The forest seems to beckon you anyway...")
        enter_forest() # Default to entering the forest if invalid input

def enter_forest():
    print("\nYou decide to follow the winding path into the Whispering Woods.")
    print("The trees grow taller and closer, their branches forming a shadowy canopy.")
    print("After a while, the path splits into two:")
    print("1. A narrow, overgrown trail leading deeper into the dark.")
    print("2. A wider, slightly less menacing path that seems to curve to the right.")

    choice = input("Enter your choice (1 or 2): ")
    if choice == '1':
        dark_trail()
    elif choice == '2':
        curvy_path()
    else:
        print("Invalid choice. You hesitate, and a strange wind pushes you onto the dark trail.")
        dark_trail()

def go_around_forest():
    print("\nYou decide the forest is too eerie and try to find a way around it.")
    print("After hours of walking, you realize the forest stretches further than you thought.")
    print("You come across a small, abandoned cabin. Smoke seems to be rising from its chimney, though no one is around.")
    print("\nWhat do you do?")
    print("1. Approach the cabin cautiously.")
    print("2. Turn back towards the main path, feeling a chill.")

    choice = input("Enter your choice (1 or 2): ")
    if choice == '1':
        approach_cabin()
    elif choice == '2':
        turn_back_to_path()
    else:
        print("Invalid choice. You are drawn to the cabin despite your hesitation.")
        approach_cabin()

def dark_trail():
    print("\nYou bravely take the narrow, dark trail.")
    print("The whispering intensifies, and you start to feel watched.")
    print("Suddenly, you stumble upon a glowing, ancient rune etched into a mossy stone.")
    print("As you touch it, the rune pulsates, and you hear a voice in your head:")
    print("'Answer truly, or be lost forever. What is the spirit of the woods?'")
    print("1. Nature's embrace.")
    print("2. A lurking predator.")
    print("3. Ancient magic.")

    choice = input("Enter your choice (1, 2, or 3): ")
    if choice == '1':
        print("\n'Indeed,' whispers the voice. 'Harmony is its heart.'")
        print("The rune fades, and a hidden path opens, leading you to a clearing filled with luminous flora.")
        print("You find peace and become a guardian of the woods. (Ending: Guardian of the Woods)")
    elif choice == '2':
        print("\n'A foolish fear,' rumbles the voice, and the ground beneath you crumbles.")
        print("You fall into a dark chasm, never to be seen again. (Ending: Lost Forever)")
    elif choice == '3':
        print("\n'Close, but incomplete,' sighs the voice. 'Magic is merely its breath.'")
        print("The rune sends a jolt through you, transporting you to a distant, unknown land.")
        print("You embark on a new, bewildering journey. (Ending: Unforeseen Journey)")
    else:
        print("\nYour hesitation seals your fate. The rune's light overwhelms you.")
        print("You awaken later, disoriented and unable to remember how you got there. (Ending: Amnesiac Wanderer)")

def curvy_path():
    print("\nYou choose the wider, curving path.")
    print("It leads you to a sparkling, clear stream. On the other side, you see a faint light.")
    print("The stream looks shallow enough to wade through.")
    print("\nWhat do you do?")
    print("1. Wade through the stream towards the light.")
    print("2. Follow the stream downstream to see where it leads.")

    choice = input("Enter your choice (1 or 2): ")
    if choice == '1':
        wade_stream()
    elif choice == '2':
        follow_stream()
    else:
        print("Invalid choice. A sudden current pulls you downstream.")
        follow_stream()

def approach_cabin():
    print("\nYou cautiously approach the old cabin. The door is ajar.")
    print("A faint, sweet smell emanates from inside.")
    print("\nWhat do you do?")
    print("1. Push the door open and enter.")
    print("2. Peer through a dusty window first.")

    choice = input("Enter your choice (1 or 2): ")
    if choice == '1':
        enter_cabin()
    elif choice == '2':
        peer_through_window()
    else:
        print("Invalid choice. Curiosity gets the better of you, and you push the door open.")
        enter_cabin()

def turn_back_to_path():
    print("\nFeeling uneasy, you decide to turn back towards the main path.")
    print("The walk is long and uneventful. You eventually emerge from the forest, tired but safe.")
    print("You decide to never go near the Whispering Woods again. (Ending: Safe but Unadventurous)")

def wade_stream():
    print("\nYou carefully wade through the cool stream. The light on the other side grows brighter.")
    print("As you reach the bank, you find yourself in a hidden glade, illuminated by countless fireflies.")
    print("In the center stands a wise old hermit, who offers you ancient knowledge.")
    print("You spend your days learning profound secrets. (Ending: Seeker of Wisdom)")

def follow_stream():
    print("\nYou follow the stream downstream. It widens and becomes a small river.")
    print("Eventually, you discover a small, mossy boat tied to a tree.")
    print("\nWhat do you do?")
    print("1. Untie the boat and paddle downstream.")
    print("2. Continue walking along the riverbank.")

    choice = input("Enter your choice (1 or 2): ")
    if choice == '1':
        paddle_downstream()
    elif choice == '2':
        walk_riverbank()
    else:
        print("Invalid choice. The boat seems to invite you, and you climb in.")
        paddle_downstream()

def enter_cabin():
    print("\nYou push the door open. Inside, the cabin is surprisingly cozy, but empty.")
    print("On a table, there's a half-eaten meal and a note that reads: 'Be back soon. Don't touch the glowing orb.'")
    print("In the corner, a small, pulsating orb sits on a pedestal.")
    print("\nWhat do you do?")
    print("1. Wait patiently for the owner to return.")
    print("2. Touch the glowing orb.")

    choice = input("Enter your choice (1 or 2): ")
    if choice == '1':
        wait_for_owner()
    elif choice == '2':
        touch_orb()
    else:
        print("Invalid choice. You decide to wait, but your eyes keep drifting to the orb.")
        wait_for_owner()

def peer_through_window():
    print("\nYou peer through a grimy window. Inside, you see a small, simple room.")
    print("There's a fire crackling in the hearth, but no one is visible.")
    print("As you watch, a shadowy figure quickly passes by the back window, carrying a large sack.")
    print("\nWhat do you do?")
    print("1. Knock on the door and try to introduce yourself.")
    print("2. Decide it's best to leave and continue avoiding the forest.")

    choice = input("Enter your choice (1 or 2): ")
    if choice == '1':
        knock_on_door()
    elif choice == '2':
        turn_back_from_cabin()
    else:
        print("Invalid choice. You knock hesitantly.")
        knock_on_door()

def paddle_downstream():
    print("\nYou untie the boat and gently push off. The current carries you swiftly.")
    print("After a thrilling ride, the river opens into a vast, shimmering lake.")
    print("A mystical creature emerges from the water, greeting you as a chosen one.")
    print("You embark on a grand quest across the lake. (Ending: The Chosen One)")

def walk_riverbank():
    print("\nYou decide to walk along the riverbank, enjoying the peaceful sounds.")
    print("Eventually, the river leads you to a bustling port town on the coast.")
    print("You decide to start a new life as a sailor. (Ending: Life at Sea)")

def wait_for_owner():
    print("\nYou wait patiently. After some time, an old, kind-faced woman returns.")
    print("She thanks you for your honesty and shares a warm meal and stories.")
    print("You find a new friend and a cozy home. (Ending: A Warm Welcome)")

def touch_orb():
    print("\nDespite the warning, you touch the glowing orb.")
    print("A blinding flash engulfs you, and you feel a strange power surge through your body.")
    print("When the light subsides, you realize you can now understand animals.")
    print("You become a whisperer of the wild. (Ending: Animal Communicator)")

def knock_on_door():
    print("\nYou knock on the cabin door. After a moment, it creaks open.")
    print("A gruff, but not unkind, woodsman peers out.")
    print("He invites you in for tea and warns you about the true dangers of the forest.")
    print("You gain valuable wisdom and a new ally. (Ending: Forest Ally)")

def turn_back_from_cabin():
    print("\nSeeing the shadowy figure, you decide the cabin is too suspicious.")
    print("You quickly and quietly retreat, feeling relieved to have avoided potential trouble.")
    print("You eventually find your way out of the forest and return to civilization, shaken but safe. (Ending: Narrow Escape)")


# Start the game
if __name__ == "__main__":
    start_game()
    print("\nThank you for playing 'The Whispering Woods' Adventure!")
