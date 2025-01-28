#List of email addresses
emails=[
    'raj.doe@example.com',
    'om.smith@company.org',
    'shubh.johnson@workplace.net',
    'Shree.brown@school.edu'
    ]
#Extracting the domain part from each email address
domains=[email.split('@')[1] for email in emails]

#Output the result
print(domains)
