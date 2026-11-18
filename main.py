from data import GAME_STATE
from random import randint

START_KEY = "start"

ll_duty = ["duty_phone_yes", "duty_phone_no"]

def run_quest():
    current_key = START_KEY

    print("\n" + "=" * (11+6*2))
    print("      FIND JAMIE!")
    print("=" * (11+6*2))

    while True:
        state = GAME_STATE[current_key]

        print(f"\n--- {state['title']} ---")
        print(state["prompt"])

        status = state["status"]

        if status in ("victory", "game_over"):
            if status == "victory":
                print("\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⢠⡿⣷⣦⠀⠀⠀⠀⠀⢸⣿⣶⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠈⣿⣿⠇⠀⠀⠀⠀⠀⠈⢿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n\n⠀⠀⠀⠀⠀⠀⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⡇⡻⣧⠀⠀⠀⠀⠀⢰⣴⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠺⡾⣯⣧⠀⠀⠀⠀⣸⣟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠫⡿⣿⣅⣀⡠⢔⣿⡷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⢿⣿⡿⡷⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
                print("\n[ STATUS: VICTORY, YOU FOUND JAMIE ]")
            else:
                print("\n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n\n⠀⠀⠀⠀⠀⠀⠀⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⢠⡿⣷⣦⠀⠀⠀⠀⠀⢸⣿⣶⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠈⣿⣿⠇⠀⠀⠀⠀⠀⠈⢿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠧⣹⠀⠀⠀⠀⠀⠀⠀⠀⠀\n\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⣴⡾⣳⡯⣟⣛⣻⠿⣽⣦⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⢀⣾⢃⡿⠋⠀⠀⠀⠈⠙⣟⢿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⣿⣗⡾⠀⠀⠀⠀⠀⠀⠀⠘⢎⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⢐⣿⣯⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⢸⠙⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠽⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀\n")
                
                print("\n[ STATUS: GAME OVER, you could NOT find JAMIE]")
            break

        else:
            choices = state["choices"]

            print("\nOptions:")
            for idx, option in enumerate(choices, start=1):
                print(f"  {idx}. {option["text"]}")

            choice = int(input(f"\nSelect an option (1-{len(choices)}): ").strip())
            so = randint(0,5)
            if ("alter_state" in choices[choice-1] and so == 0):
                current_key = choices[choice - 1]["alter_state"]
                continue
            
            current_key = choices[choice - 1]["next_state"]


if __name__ == "__main__":
    run_quest()
