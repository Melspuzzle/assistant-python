#programm for assistant 
# author Melspuzzle
# 26.03.2023

def options_directory():

    userinput=input("Which option dou you want to use? Choose your option by number.\n")
        # das Programm startet mit der Frage, welche Option der User nutzen möchte
        # the program starts with the question which option the user wants to use
    if userinput=="1":
        print("You chose option 1: The calculator starts now")
        # wenn der User "Option 1" schreibt oder "1", dann gibt das Programm die Antwort, dass Option 1 ausgewählt wurde und startet 
        # hat der User "Option 2 " geschrieben oder "2", dann gibt das Programm die Antwort, dass Option 2 ausgewählt wurde und startet
        # if the user types "option 1" or "1" the programm gives the answer, that this option starts now
        # else the user types "option 2" or "2" the programm gives the answer, that this option starts now
    elif userinput=="2":
        print("You chose option 2: The calender starts now")
    else:
        print("This was not an option")

    return

print("This is your assistant. You have following options:\noption 1: calculator\noption 2: calender")

options_directory() 
