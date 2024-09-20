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

def select(function_code):
    # Create item
    if function_code == "C":
        input_item = user_input("Input item:")
        create(input_item)

    # Read item
    elif function_code == "R":
        item_index = user_input("Index Number?")

        # Remember that item_index must actually exist or our program will crash.
        read(item_index)

    # Print all items
    elif function_code == "P":
        list_all_items()

    # Catch all
    else:
        print("Unknown Option")

def user_input(prompt):
    # the input function will display a message in the terminal
    # and wait for user input.
    user_input = input(prompt)
    return user_input





def test():
    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")

    destroy(1)

    print(read(0))
#print(read(1))
    list_all_items()
    # Call your new function with the appropriate value
    select("C")
    # View the results
    list_all_items()
    # Call function with new value
    select("R")
    # View results
    list_all_items()
    # Continue until all code is run
    user_value = user_input("Please Enter a value:")
    print(user_value)
test()



#checklist = ['Blue', 'Orange']
#checklist[1] = 'Cats'
#print(checklist)