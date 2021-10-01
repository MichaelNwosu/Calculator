i = 2

for i in range(10):
    print("Select number to preform operation")
    print("1 = ADD")
    print("2 = SUBTRACT")
    print("3 = DIVIDE")
    print("4 = TRIANGLE AREA")
    print("5 = TRIANGLER PRISM")
    print("6 = RECTANGLE/SQUARE AREA")
    print("7 = RECTANGLER PRISM ")
    print("8 = 3D circle cal")
    print("9 = Cicumference Calcalator")
    print("10 = Ellispe Calcalator")
    print("11 = Area Calcalator")
    print("12 = Cube Calcalator")
    print("13 = JUST SUM RANDOM VAR")
    print("14 = Interest Calculator ")
    print("15 = Grade Calcalator")
    print("16 = Exponnets Cal = Heaven")
    print("E = Exit")


    operation = input()

    if   operation == "1" :
        num1 = input("Enter Your First Number :  ")
        num2 = input("Enter Your Second Number :  ")
        print("The Sum Of Number Is: " + str(int(num1) + int(num2)))
    elif   operation == "2" :
        num1 = input("Enter Your First Number :  ")
        num2 = input("Enter Your Second Number :  ")
        print("The Sum Of Number Is: " + str(int(num1) - int(num2)))
    elif   operation == "3" :
        num1 = input("Enter Your First Number :  ")
        num2 = input("Enter Your Second Number :  ")
        print("The Sum Of Number Is: " + str(int(num1) / int(num2)))
    elif operation == "4" :
        num1= float  (input("Enter The Base = "))
        num2= float  (input("Enter The Height = "))
        Area = (num1*num2)/2
        print('ANSWER =',(round(Area,3)))
    elif operation == "5" :
        num1= float  (input("Enter The Base  = "))
        num2= float  (input("Enter The Height  = "))
        num3= float  (input("Enter The Width = "))
        Area = 0.5*num1*num2*num3
        print('ANSWER =',round(Area,2))
    elif operation == "1b" :
        print("Never going to give you up (not sorry)")
    elif operation == "6"  :
        num1= float(input("Enter Side 1: "))
        num2= float(input("Enter Side 2: "))
        area=num1*num2
        print('Answer:',(round(area,3)))
    elif operation == "7" :
        num1= float  (input("Enter The Base  = "))
        H= float  (input("Enter The Height  = "))
        W= float  (input("Enter The Width = "))
        T=num1*H*W
        print('Answer :',(round(T,3)))
    elif operation == "8" : 
        r= float (input("Enter the radius ="))
        volume = (4/3)*3.14*r**3
        print('ANSWER =',volume)
    elif operation == "9" :
        r= float (input("Enter The Radius: "))
        t= 2*3.14*r
        print('ANSWER =',t)
    elif operation == "10" :
        r1= float  (input("Enter The 1st Radius  = "))
        r2= float  (input("Enter The 2nd Radius  = "))
        t=3.14*r1*r2
        print('Answer =',(round(t,3)))
    elif operation == "11" :
        S1= float(input("Enter Side 1: "))
        S2= float(input("Enter Side 2: "))
        area=S1*S2
        print('Answer:',(round(area,3)))
    elif operation == "12" :
        B= float  (input("Enter The Base  = "))
        H= float  (input("Enter The Height  = "))
        W= float  (input("Enter The Width = "))
        T=B*H*W
        print('Answer :',(round(T,3)))
    elif operation == "13" : 
        sum_of_marks=float  (input("Enter 1st Mark  ="))
        sum_of_marks=sum_of_marks+float  (input("Enter 2nd Mark ="))
        sum_of_marks=sum_of_marks+float  (input("Enter 3rd Mark ="))
        sum_of_marks=sum_of_marks+float  (input("Enter 4nd Mark ="))
        print('Sum Of Marks =',sum_of_marks)
    elif operation == "14" : 
        p= float  (input("Enter The Amount = "))
        r= float  (input("Enter The Rate = "))
        t= float  (input("Enter The Amount Of Time/yrs = "))
        v = p*(r/100)*t
        print('ANSWER =',(round(v,2)))
    elif operation == "15" :
        grade1= float (input("Enter Your 1th Grade: "))
        grade2= float (input("Enter Your 2th Grade: "))
        grade3= float (input("Enter Your 3th Grade: "))
        grade4= float (input("Enter Your 4th Grade: "))
        t= (grade1+grade2+grade3+grade4)/4
        print('ANSWER =',t)
    elif operation == "16" : 
        a= float(input("Enter 1st Value: "))
        b= float(input("Enter 2st Value: "))
        t=a ** b
        print(round(t,3))
    elif operation == "E" :
        exit() 
    else:
        print("Invalid Entry")

