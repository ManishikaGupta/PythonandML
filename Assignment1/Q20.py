l=[]
sum=0
total=int(input("Enter the total number of elements:"))
for i in range(0,total):
    elements=int(input("Enter the Element {}:".format(i+1)))
    sum=sum+elements
    l.append(elements)
print(l)
print("Sum of Elements={}".format(sum))
