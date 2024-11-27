# A dictionary representing customer IDs and their corresponding customer names
customer = {
    1001: "Shubh Bhagde",    
    1002: "Aman sul", 
    1003: "Rushi Sathe",    
    1004: "pratik chavan",     
    1005: "Rahul Kale"  
}

# Accessing the customer name using the customer ID
print("The name of customer ID 1003 is:", customer[1003])

# Adding a new customer with their ID and name
customer[1006] = "OM Shaha"

# Printing the updated dictionary
print(customer)
