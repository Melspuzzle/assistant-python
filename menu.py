
def getMenuSelction():
    userinput = input(
        "This is your assistant. You have following options:\n"
        "option 1: calculator\n"
        "option 2: calender\n"
        "option 3: exit\n"
        "Which option do you want to use? Choose your option by number.\n"
        )
        # das Programm startet mit der Frage, welche Option der User nutzen möchte
        # the program starts with the question which option the user wants to use
    if userinput == "1":
        print("You chose option 1: The calculator starts now")
        # wenn der User "Option 1" schreibt oder "1", dann gibt das Programm die Antwort, dass Option 1 ausgewählt wurde und startet
        # hat der User "Option 2 " geschrieben oder "2", dann gibt das Programm die Antwort, dass Option 2 ausgewählt wurde und startet
        # if the user types "option 1" or "1" the programm gives the answer, that this option starts now
        # else the user types "option 2" or "2" the programm gives the answer, that this option starts now
    
    elif userinput == "2":
        print("You chose option 2: The calender starts now")
    
    elif userinput == "3":
        print("You chose option 3: exit programm")
 
    else:
        print("This was not an option. Try again.")
        

    return int(userinput)