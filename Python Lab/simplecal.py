class Calculator:
    def add(self, a, b):
            return a+b
        
    def sub(self, a, b):
            return a-b
        
    def multi(self, a, b):
            return a*b
        
    def div(self, a, b):
            return a/b
#creat a Object    
cal=Calculator()

#use for loop
for i in range(1,5):
    print("1.Addition")
    print("2.Substraction")
    print("3.Multiplaction")
    print("4.Divistion")
    

    user_input=int(input("Enter your Choice:"))#Enter the user Choice
    num1=int(input("Enter the 1st Number:"))#tack a user Input
    num2=int(input("Enter the 2nd Number:"))

    if user_input==1:
        print("Addition is",cal.add(num1,num2))
    elif user_input==2:
            print("Substraction is",cal.sub(num1,num2))
    elif user_input==3:
            print("Multiplaction is",cal.multi(num1,num2))
    elif user_input==4:
            print("Divstion is",cal.div(num1,num2))
    else:
        print("Plzz Enter valid Input!!!")
        
    


