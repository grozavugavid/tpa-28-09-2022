import math
x=int(input('Introduceti numarul: '))
y=int(input('Introduceti numarul: '))
z=int(input('Introduceti numarul: '))
q=[x,y,z]

divizori=[]
def max_div(x, y, z):
    n=0
    for i in range(1, min(x, y, z)+1):
        if x%i==y%i==z%i==0:
            n+=1
            divizori.append(i)
        return n

print("Toti divizorii comuni:",*divizori,sep=' ')

def m3(q):
    v=[]
    for k in range(1, (x*y*z+1)**3):
        if k%x==0 and k%y==0 and k%z==0:
            v.append(k)
    return v
print(m3(q)[0],m3(q)[1],m3(q)[2])

def w(q):
    o=0
    u=0
    if x+y>z and x+z>y and y+z>x:
        o=math.sqrt((sum(q)/2)*(sum(q)/2-x)*(sum(q)/2-y)*(sum(q)/2-z))
        u=sum(q)
    return o,u
print(w(q))