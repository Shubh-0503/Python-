# List of employee records 
employees = [
    {'name': 'Raj', 'department': 'Sales', 'salary': 50000},
    {'name': 'Shyam', 'department': 'Marketing', 'salary': 55000},
    {'name': 'Kishor', 'department': 'Sales', 'salary': 48000},
    {'name': 'Sumit', 'department': 'HR', 'salary': 45000},
    {'name': 'Aman', 'department': 'Sales', 'salary': 52000}
]

#Create a new list with names of employees in the Sales department all in uppercase
sales_employees_uppercase = [employee['name'].upper() for employee in employees if employee['department'] == 'Sales']

# Output the result
print(sales_employees_uppercase)
