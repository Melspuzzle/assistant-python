def option1_calculator():
    userinput = input("Enter your calculation\n")
    resultList =[]
    runtime_loop="y"
    while runtime_loop=="y":
        if "+" in userinput:
            interim_result = userinput.split("+")
            if resultList!=[]:
                result= resultList[0]
                result+= float(interim_result[1])
            else:
                result= float(interim_result[0]) + float(interim_result[1])

        elif "-" in userinput:
            interim_result = userinput.split("-")
            if resultList!=[]:
                result= resultList[0]
                result-= float(interim_result[1])
            else:
                result= float(interim_result[0]) - float(interim_result[1])

        elif "*" in userinput:
            interim_result = userinput.split("*")
            if resultList!=[]:
                result= resultList[0]
                result*= float(interim_result[1])
            else:
                result= float(interim_result[0]) * float(interim_result[1])

        elif "/" in userinput:
            interim_result = userinput.split("/")
            if resultList!=[]:
                result= resultList[0]
                result//= float(interim_result[1])
            else:
                result= float(interim_result[0]) // float(interim_result[1])
        else:
            print("Please use an operator for the calculation.")
            return
        

        try:
            print(f"Your result:" + str(result))
            
        except: 
            print("Calculation not possible")

        
        userinput = input(
                "Would you like to continue calculating with the result?\n (y)es or (n)o \n Type X to get back to the menu.\n"
            )
        if userinput =="y":
            if resultList!=[]:
                resultList.clear()
            resultList.append(result)
            print(f"Enter your calculation")
            userinput = input(resultList[0])
            runtime_loop="y"

        elif userinput=="n":
            resultList.clear()
            userinput = input("Enter your calculation\n")
            runtime_loop="y"

        elif userinput =="X" or "x":
            return