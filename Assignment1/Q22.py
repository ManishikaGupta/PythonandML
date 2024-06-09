'''/Write a python program that returns the 
minimum and maximum values in a list of numbers.'''
l=[]
sum=0
total=int(input("Enter the total number of elements:"))
for i in range(0,total):
    elements=int(input("Enter the Element {}:".format(i+1)))
    l.append(elements)
    maxelement=max(l)
    minelement=min(l)
print(l)
print("Maximum in List={}".format(maxelement))
print("Minimum in List={}".format(minelement))
