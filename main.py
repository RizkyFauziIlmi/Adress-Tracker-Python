import functions

exit = False
attempt = 1

while (exit == False):
    
    functions.print_menu()
    command = functions.ask()

    if int(command) == 1:
        functions.clear()
        functions.get_location()
        close = functions.ask_closed()
        if (close):
            exit = True
    elif int(command) == 2:
        functions.clear()
        exit = True
    else:
        print("Invalid Input!")


print("Program Clossed!")