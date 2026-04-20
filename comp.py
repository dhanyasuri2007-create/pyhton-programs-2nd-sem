a=[1,2,3,4,5,6,7,2,3]
l=[i for i in a if i%2==0]
s={i*i for i in a}
d={i:i*i for i in a}
gen=(x*x for x in range(6))
print(l)
print(s)
print(d)
for value in gen:
    print(value)