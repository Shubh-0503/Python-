#Q.3)WAP to check whether person can vote or not using function
#create class 
class UserVote:
    def vote(self):
        self.age=int(input("Enter the age:"))# accept the user input
    def display(self):
        if self.age>=18: #check the condtion
            print("You are eligible to vote.")
        else:
            print("You are not eligible to vote.")
#create object      
vt=UserVote()
vt.vote()
vt.display()#display output

        
