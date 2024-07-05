#programm for assistant 
# author Melspuzzle
# 26.03.2023

def options_directory():

    userinput=input("This is your assistant. You have following options:\noption 1: calculator\noption 2: calender\nWhich option do you want to use? Choose your option by number.\n")
        # das Programm startet mit der Frage, welche Option der User nutzen möchte
        # the program starts with the question which option the user wants to use
    if userinput=="1":
        print("You chose option 1: The calculator starts now")
        # wenn der User "Option 1" schreibt oder "1", dann gibt das Programm die Antwort, dass Option 1 ausgewählt wurde und startet 
        # hat der User "Option 2 " geschrieben oder "2", dann gibt das Programm die Antwort, dass Option 2 ausgewählt wurde und startet
        # if the user types "option 1" or "1" the programm gives the answer, that this option starts now
        # else the user types "option 2" or "2" the programm gives the answer, that this option starts now
        option1_calculator()
        #open subfunction, öffnet Unterfunktion
    elif userinput=="2":
        print("You chose option 2: The calender starts now")
        option2_calender()
    else:
        print("This was not an option")

    return

def repetition():
    userinput=input("Do you want to return to the directory? Type 'y' to go back, otherwise the programme will end.\n")
    while userinput=="y":
        options_directory()
        userinput=input("Do you want to return to the directory? Type 'y' to go back, otherwise the programme will end.\n")


def option1_calculator():
    userinput=input("Enter your calculation\n")
    #erkennen des Operators, aufsplitten des Strings am Operator in einzelne Elemente, erkennen der Elemente als Zahl 
    # und Berechnung und Ausgabe des Ergebnis
    if "+" in userinput: 
        interim_result=userinput.split("+")
        result = int(interim_result[0])+int(interim_result[1])
        print(f"Your result:"+str(result))
    elif "-" in userinput:
        interim_result=userinput.split("-")
        result = int(interim_result[0])-int(interim_result[1])
        print(f"Your result:"+str(result))
    elif "*" in userinput:
        interim_result=userinput.split("*")
        result = int(interim_result[0])*int(interim_result[1])
        print(f"Your result:"+str(result))
    elif "/" in userinput:
        interim_result=userinput.split("/")
        result = int(interim_result[0])//int(interim_result[1])
        print(f"Your result:"+str(result))
    else: 
        print("Please use an operator for the calculation.")

    userinput=input("Would you like to continue calculating with the result?Type 1 for yes and 0 for no.\n")
    while userinput=="1":
        userinput=input("Enter your calculation\n"+str(result))
        if "+" in userinput: 
            interim_result=userinput.split("+")
            result += int(interim_result[1])
            print(f"Your result:"+str(result))
        elif "-" in userinput:
            interim_result=userinput.split("-")
            result -=int(interim_result[1])
            print(f"Your result:"+str(result))
        elif "*" in userinput:
            interim_result=userinput.split("*")
            result*=int(interim_result[1])
            print(f"Your result:"+str(result))
        elif "/" in userinput:
            interim_result=userinput.split("/")
            result //=int(interim_result[1])
            print(f"Your result:"+str(result))
        else: 
            print("Please use an operator for the calculation.")
        userinput=input("Would you like to continue calculating with the result?Type 1 for yes and 0 for no.\n")
    


def option2_calender():
    userinput=input(".\n")


options_directory() 

repetition()
