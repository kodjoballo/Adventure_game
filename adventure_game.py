import json
NODE_START = 1
valid_endings = {"WIN", "LOSE"}

print("***************************")
print("***** ADVENTURE GAME  *****")
print("***************************")

print(r"""
| 
--------------------------------------------------------
🌄 WELCOME TO THE LAND OF SHADOWS 🌌

You awaken in a dense forest, mist curling at your feet.
A sword lies nearby. In the distance, something stirs...

Will you choose the path of courage? Or fall to fear?

               Type 'A' or 'B' to begin.
--------------------------------------------------------
""")


print("\n Let's get started!!!!!!!")

def play():
    node = NODE_START

    name = input ("Please enter your name to begin the adventure: ")

    try:

        with open("Data\\story.json", "r", encoding="utf-8") as file:

            #or load it from Pycharm directly
            #         with open("Adventure_Game_folder/story.json", "r", encoding="utf-8") as file:
            story = json.load(file)




    except FileNotFoundError:
        print("❌that file was not found")

    except PermissionError:
        print("❌You do not have permission to read that file ")

        # 🔑 convert keys to int
    story = {int(k): v for k, v in story.items()}

    while True:
        current = story[node]
        print("\n",current["text"], sep="")

        # Check for ending

        if current.get("A") in valid_endings and current.get("B") in valid_endings:

            # node itself is a win or lose screen, just break
            print("\n Critical choice: ")




            # otherwise, ask for a decision

        choice = input("Your choice [A/B]: ").strip().upper()
        if choice not in ("A", "B"):
            print(" ❗Please type A or B ")
            continue

        next_node = current[choice]

        # If we hit WIN or LOSE, announce and break

        if next_node == "WIN":
            print(f"\n🎉 ▶️YOU WIN!◀️ 🎉, {name}")
            break
        elif next_node == "LOSE":
            print(f"\n💀 ❌ YOU LOSE. ❌ 💀, {name}")

            print(r"""
               _____                         ____                 
              / ____|                       / __ \                
             | |  __  __ _ _ __ ___   ___  | |  | |_   _____ _ __ 
             | | |_ |/ _` | '_ ` _ \ / _ \ | |  | \ \ / / _ \ '__|
             | |__| | (_| | | | | | |  __/ | |__| |\ V /  __/ |   
              \_____|\__,_|_| |_| |_|\___|  \____/  \_/ \___|_|   

                     💀 GAME OVER 💀
            """)
            break
        else:
            node = int(next_node)  # only convert if it's numeric


        # Otherwise, move on
        node = next_node

        # LAUNCH

if __name__ == "__main__":
    play()










