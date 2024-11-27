#Q.2)WAP to find maximum among two number
#define class
class largestNumber:
# tack the user input 
    def UserInput(self):
        self.num1=int(input("Enter the Number 1:"))
        self.num2=int(input("Enter the Number 1:"))

    def display(self):
        if self.num1>self.num2: #find the max number 
            print("Num 1 is max number")
        else:
            print("Num 2 is max number")
#create object 
lr=largestNumber()
#call the function 
lr.UserInput()
lr.display()



            

        
