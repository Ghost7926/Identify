import os

def print_bars(counts, dice_type):
    max_count = max(counts.values())
    print(f"Dice Roll Distribution ({dice_type}-sided dice):")
    for i in range(1, dice_type + 1):
        count = counts.get(i, 0)
        bar_length = int(count / max_count * 40) if max_count != 0 else 0
        print(f"{i}: {'#' * bar_length} ({count})")

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Choose the dice type to track:")
        print("1. d4")
        print("2. d6")
        print("3. d8")
        print("4. d10")
        print("5. d12")
        print("6. d20")
        print("7. Quit")
        choice = input("Enter your choice: ")
        if choice == '1':
            dice_type = 4
            break
        elif choice == '2':
            dice_type = 6
            break
        elif choice == '3':
            dice_type = 8
            break
        elif choice == '4':
            dice_type = 10
            break
        elif choice == '5':
            dice_type = 12
            break
        elif choice == '6':
            dice_type = 20
            break
        elif choice == '7':
            return
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")
            input("Press Enter to continue...")

    counts = {i: 0 for i in range(1, dice_type + 1)}
    total_rolls = 0

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print_bars(counts, dice_type)
        roll = input(f"Enter the result of the {dice_type}-sided dice roll, or 'q' to quit: ")
        if roll.lower() == 'q':
            break
        try:
            roll = int(roll)
            if roll < 1 or roll > dice_type:
                print(f"Invalid input. Roll must be between 1 and {dice_type}.")
                continue
            counts[roll] += 1
            total_rolls += 1
        except ValueError:
            print(f"Invalid input. Please enter a number between 1 and {dice_type} or 'q' to quit.")
            continue
    
    if total_rolls == 0:
        print("No rolls recorded.")
    else:
        print("Results after {} rolls:".format(total_rolls))
        for side, count in counts.items():
            print("Side {}: {} occurrences, {}%".format(side, count, (count/total_rolls)*100))

if __name__ == "__main__":
    main()
