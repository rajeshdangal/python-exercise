#  store grocery items
grocery_list = []

while True:

    print("Would you like to\n(1) Add or\n(2) Remove items or\n(3) Quit?: ", end="")
    choice = input().strip()

    if choice == "1":

        print("What will be added?: ", end="")
        item = input().strip()
        grocery_list.append(item)
    elif choice == "2":

        if len(grocery_list) > 0:
            print(f"There are {len(grocery_list)} items in the list.")
            print("Which item is deleted?: ", end="")
            try:
                index = int(input().strip())
                if 0 <= index < len(grocery_list):
                    grocery_list.pop(index)
                else:
                    print("Incorrect selection.")
            except ValueError:
                print("Incorrect selection.")
        else:
            print("The list is already empty.")
    elif choice == "3":
        print("The following items remain in the list:")
        for item in grocery_list:
            print(item)
        break
    else:
        print("Incorrect selection.")
