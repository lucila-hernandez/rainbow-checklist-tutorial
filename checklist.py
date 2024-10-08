checklist = list()

# CREATE
def create(item):
    checklist.append(item)

# READ
def read(index):
    if 0 <= index < len(checklist): 
        return checklist[index]
    else:
        return "Index out of range." 
    
# UPDATE
def update(index, item):
    if 0 <= index < len(checklist): 
     checklist[index] = item
    else:
        print("Index out of range.")

# DESTROY
def destroy(index):
    if 0 <= index < len(checklist): 
        checklist.pop(index)
    else:
        print("Index out of range.")

def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1

def mark_completed(index):
    if 0 <= index < len(checklist):  
        checklist[index] = "√ " + checklist[index]  
    else:
        print("Index out of range.")

def user_input(prompt):
    # the input function will display a message in the terminal
    # and wait for user input.
    user_input = input(prompt)
    return user_input

def select(function_code):
    function_code = function_code.upper()
    # Create item
    if function_code == "C":
        input_item = user_input("Input item:")
        create(input_item)
        print("Item added.")

    # Read item
    elif function_code == "R":
        try:
            item_index = int(user_input("Index Number?"))
            print(read(item_index))
        # Remember that item_index must actually exist or our program will crash.
        except ValueError:
            print("Please enter a valid integer.")

    elif function_code == "U":
        try:
            item_index = int(user_input("Index Number?"))
            new_item = user_input("New item:")
            update(item_index, new_item)
            print("Item updated.")
        except ValueError:
            print("Please enter a valid integer.")
    
    elif function_code == "D":
        try:
            item_index = int(user_input("Index Number?"))
            destroy(item_index)
            print("Item destroyed.")
        except ValueError:
            print("Please enter a valid integer.")

    # Print all items
    elif function_code == "P":
        list_all_items()
    
    elif function_code == "Q":
    # This is where we want to stop our loop
        return False

    # Catch all
    else:
        print("Unknown Option")
    return True


def test():
    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")

    destroy(1)

    print(read(0))

    list_all_items()
  
    select("C")
    
    list_all_items()
    
    select("R")
    
    list_all_items()
    
    user_value = user_input("Please Enter a value:")
    print(user_value)
test()

running = True
while running:
    selection = user_input(
        "Press C to add to list, R to Read from list, P to display list, and Q to quit")
    running = select(selection)

