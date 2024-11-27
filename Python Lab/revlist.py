#Q.2)WAP to reverse the element in List
# Create an empty list
my_list = []

#user to input elements
num_elements = int(input("How many elements do you want to enter"))

print(f"Enter {num_elements} elements:")
for i in range(num_elements):
    element = input(f"Enter element {i+1}: ")
    my_list.append(element)

#Display the original list
print("\nOriginal List:", my_list)

#Reverse the list using list slicing
reversed_list = my_list[::-1]

#Display the reversed list
print("Reversed List:", reversed_list)
