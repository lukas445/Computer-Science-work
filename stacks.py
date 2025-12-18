

def initialise_stack(max_size=int(input("Enter your preferred stack size: "))):
    
    """
    Creates a new stack with specified capacity.
    Returns: stack (list), top (int), max_size (int)
    """

    stack = []
    top = -1 
    return stack, top, max_size

def is_empty(top):
    
    """
    Checks if stack is empty.
    Returns True if empty, False
    otherwise.
    """

    return top == -1

def is_full(top, max_size):
    
    """
    Checks if stack has reached
    capacity.
    Returns True if full, False otherwise.
    """

    return top == max_size - 1

def get_size(top):
    
    """
    Returns current number of
    elements.
    """

    return top + 1

def push(stack, top, max_size, item):
    
    """
    Adds an item to the top of the stack.
    Returns updated top pointer, or raises overflow error.
    """

    if is_full(top, max_size):
        print("OVERFLOW ERROR: Stack is full!")
        print(f"Cannot add '{item}' - capacity reached.")
        return top
    top = top + 1
    stack.append(item)
    print(f"Pushed '{item}' onto the stack.")
    return top

def pop(stack, top):
    
    """
    Removes and returns the top item from the stack.
    Returns: (popped_item, updated_top) or (None, top) if empty.
    """

    if is_empty(top):
        print("UNDERFLOW ERROR: Stack is empty!")
        print("Cannot pop from an empty stack.")
        return None, top
    item = stack[top]
    top = top - 1
    print(f"Popped '{item}' from the stack.")
    return item, top

def peek(stack, top):
    
    """
    Returns the top item without removing it.
    Returns the item or None if stack is empty.
    """

    if is_empty(top):
        print("Stack is empty - nothing to peek.")
        return None

    item = stack[top]
    print(f"Top item is: '{item}'")
    return item

def display_stack(stack, top):
    
    """
    Displays all elements in the stack from top to bottom.
    Shows the stack structure visually.
    """

    if is_empty(top):
        print("\nStack is empty.")
        return

    print("\n--- Current Stack ---")
    print("TOP")
    for i in range(top, -1, -1):
        print(f" [{i}] {stack[i]}")
    print("BOTTOM")
    print(f"Size: {get_size(top)}/{len(stack)}")
    print("-------------------\n")

def display_menu():
    
    """
    Shows available operations to the user.
    """

    print("\n=== STACK OPERATIONS ===")
    print("1. Push (add item)")
    print("2. Pop (remove item)")
    print("3. Peek (view top item)")
    print("4. Display stack")
    print("5. Check if empty")
    print("6. Check if full")
    print("7. Get stack size")
    print("8. Exit")
    print("========================")

def main():
    
    """
    Main programme loop - handles user interaction.
    """

    stack, top, max_size = initialise_stack()
    print(f"Stack initialised with capacity: {max_size}")

    while True:
        display_menu()
        choice = input("\nEnter your choice (1-8): ")

        if choice == '1':
            item = input("Enter item to push: ")
            top = push(stack, top, max_size, item)
        elif choice == '2':
            item, top = pop(stack, top)
        elif choice == '3':
            peek(stack, top)
        elif choice == '4':
            display_stack(stack, top)
        elif choice == '5':
            print("Empty:", is_empty(top))
        elif choice == '6':
            print("Full:", is_full(top, max_size))
        elif choice == '7':
            print("Size:", get_size(top))
        elif choice == '8':
            print("Exiting programme. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1-8.")

if __name__ == "__main__":
    main()
