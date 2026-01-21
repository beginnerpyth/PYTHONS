name=input("enter a name")
print("hello",(name))

for b in range(11):
    print(b)
c=0

while c>11:
    c=+1
    print(c)

def ram(a,b):
    return a+b
print(ram())

o=["ram","bam","sam","dam"]
print(o[0:])

txt= open("ha.txt","r")
print(txt.read)
txt.close()

try:
    z=int(input("enter a number"))
    b=10/z
    print(b)
except ZeroDivisionError as e:
    print(e)


