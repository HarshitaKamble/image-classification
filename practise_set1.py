#To find largest in the list-
'''M-1->
a=[8,6,32,54,43,54]
a.sort()
print(a)
a.pop()
print(f"{a.pop()} the greatest no")'''

#M-2->
a=[]
n=int(input("Enter the number of elements in the list="))
for i in range(0,n):
   b=int(input("Enter the elements="))
   a.append(b)
a.sort()
print("Largest element=",a[n])