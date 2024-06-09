'''Write a program in python that converts 
a string into a list of its characters.'''
word=str(input("Enter a Word:"))
l=[]
for i in range(len(word)):
    l.append(word[i])
print(l)
