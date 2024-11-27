#Q.1)Create dynamic list where you will ask user to enter 5 elements in it and perform insert new element and delete an element operation on it.
#Create an empty list
dynamic_list = []

#Ask the user to enter 5 elements
print("Enter 5 elements:")
for i in range(5):
    # Get input and convert it to integer
    element = int(input(f"Enter Element {i+1}: "))
    dynamic_list.append(element)

#Display the list after entering 5 elements
print("\nList after entering 5 elements:", dynamic_list)

#Insert a new element at a specific position
insert_position = int(input("\nEnter the position insert an element: "))
insert_value = int(input("Enter the value to insert: "))

#Insert the value at the specified position
dynamic_list.insert(insert_position, insert_value)
print("\nAfter inserting the element:", dynamic_list)

#Delete an element by value
delete_element = int(input("\nEnter the element you want to delete: "))

#Check if the element exists in the list before deleting
if delete_element in dynamic_list:
    dynamic_list.remove(delete_element)
    print(f"\nThe element '{delete_element}' has been deleted.")
else:
    print(f"\nThe element '{delete_element}' was not found in the list and was not deleted.")

#Display the list after deletion
print("\nAfter deleting the element:", dynamic_list)
