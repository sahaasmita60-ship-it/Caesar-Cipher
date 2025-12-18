o=(input("Enter the word you want to shift: "))
f=o.lower()
a=list(f)
c=list("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz")
n=int(input("Enter the shift number: "))
z=[]
x=0
j=0
p=""
dec=input("Enter encode or decode: ")
if dec=="encode":
 for i in range(0,len(a)):
     for j in range (0,26):
      if a[i]==c[j]:
         x=j
         z.append(c[j+n])
   
      else:
         continue
else:
  for i in range(0,len(a)):
     for j in range (0,26):
      if a[i]==c[j]:
         x=j
         z.append(c[j-n])

p="".join(z)
print(p)
