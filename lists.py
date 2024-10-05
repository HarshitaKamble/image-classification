#To find largest in the list-
#M-1->
'''a=[8,6,32,54,43,54]
a.sort()
print(a)
a.pop()
a.pop()
print(f"{a.pop()} the greatest no")'''

#M-2->
'''a=[]
n=int(input("Enter the number of elements in the list="))
for i in range(0,n+1):
   b=int(input("Enter the elements="))
   a.append(b)
a.sort()
print("Largest element=",a[n-1])'''

#to print even and odd numbers in 2 different list-
'''a=[]
n=int(input("Enter the number of elements in the lists="))
for i in range(0,n+1):
    x=int(input("Enter the elements in list a="))
    a.append(x)
print(a)

even=[]
odd=[]
for i in a:
    if(i%2==0):
      even.append(i)
    else:
        odd.append(i)    

    
print("even list= ",even)
print("odd list = ",odd)      '''

#merge two list an sort it-
'''a=[]
n=int(input("Enter the number of elemnts in list="))
for i in range (0,n+1):
    x=int(input("Enter the elements in a="))
    a.append(x)
     
b=[]
for i in range (0,n+1):
    y=int(input("Enter the elements in b="))
    a.append(y)
    
print("The merged list=",a+b)'''

#to find 2nd largest number in list using bubble sort-
'''a=[]
n=int(input("no="))
for i in range(0,n):
  b=int(input("dj="))
  a.append(b)
for i in range(0,n): 
  for j in range (0,n-i-1):
    if (a[j]>a[j+1]):
        temp=a[j]
        a[j]=a[j+1]
        a[j+1]=temp
print(a)
    '''
    
a=int(input('Enter num1='))
b=int(input('num2='))
c=a+b
print(c)