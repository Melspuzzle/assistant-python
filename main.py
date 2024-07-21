# programm for assistant
# author Melspuzzle
# start 26.03.2023
#last edit: 17.07.2024
from menu import getMenuSelction
from calculator import option1_calculator

def main():
    # Hauptprogrammcode hier
    # Menüstruktur anzeigen
    userAction=0
    # Runtimeloop
    while(userAction!=3):
        userAction= getMenuSelction()
        if userAction == 1: 
            option1_calculator()
        #if userAction ==2:
        


    

    
if __name__ == "__main__":
    main()


# geteilt durch 0, 