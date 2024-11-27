#Q.1)WAP to get factorial of a number using function
#create a class 
class factorial:
    def UserInput(self):
        #tack a user input 
        num=int(input("Enter the number:"))
        self.fact=1
        for i in range(1,num+1):
            self.fact=self.fact*i
    def display(self):
        print("Factorial of given Numbaer is:",self.fact)
#create object 
fc=factorial()
#call the function 
fc.UserInput()
fc.display()
        
            
            
        
