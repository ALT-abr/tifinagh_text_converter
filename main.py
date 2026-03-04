from utils import clear_screen
from tifinagh_converter import to_tifinagh

if __name__ == "__main__":
    clear_screen()
    print("to exit type - Q -")
    while True:
        clear_screen()
        text = input("type your text here:\n").lower()
        if text == "q":
            clear_screen()
            print("Bey!")
            break
        else:
            print(f"\n--> {to_tifinagh(text)}\n")
            input()