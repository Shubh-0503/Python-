#Q.3)WAP to find second smallest element in the list
num=[23,45,88,90,54]
print("find the Second Larget number:")
for i in range(0,5):
    for j in range(i+1,5):
        if num[j]>num[i]:
            temp=num[i]
            num[i]=num[j]
            num[j]=temp
print(num)
print("The second largest number is:",num[1])

