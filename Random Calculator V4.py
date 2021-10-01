print("Select number to preform operation")
print("1 = ADD")
print("2 = SUBTRACT")
print("3 = DIVIDE")
print("4 = TRIANGLE AREA")

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
else:
    print("Invalid Entry")