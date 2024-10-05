f= open('file_pr.txt', 'r')
data= f.read()
print(data)

new= data.replace("java", "python")
print(new)

print()
word='learning'
if(new.find(word)!=-1):
    print("found")
else:
    print("not found")