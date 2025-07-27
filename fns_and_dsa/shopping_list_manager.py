# shopping_list_manager.py

shopping_list = []

def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def add_item():
    item = input("Enter item to add: ")
    shopping_list.append(item)
    print(f"{item} added to the list.")

def remove_item():
    item = input("Enter item to remove: ")
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} removed from the list.")
    else:
        print(f"{item} not found in the list.")

def view_list():
    if not shopping_list:
        print("Shopping list is empty.")
    else:
        print("Shopping List:")
        for item in shopping_list:
            print(f"- {item}")

def main():
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            add_item()
        elif choice == 2:
            remove_item()
        elif choice == 3:
            view_list()
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
