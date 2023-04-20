a=input()
c=list(a)
s1=c.index('(')
while (")" in c):
    c.pop(s1)
c="".join(c)
c.strip(" ")
print(c)