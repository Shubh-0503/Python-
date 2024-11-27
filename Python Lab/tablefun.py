#Q.4)WAP to get table of a number using function
#create class
class table:
    def UserInput(self):
        self.num=int(input("Enter the Number:"))#user input
    def display(self):
        for i in range(1,11):
            self.ans=self.num*i
            print(self.ans)
#create object
tb=table()
tb.UserInput()#call the function
tb.display()#call the function


