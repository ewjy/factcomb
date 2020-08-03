import random
a=0
b=0
c=0
time=0
#求a,b,c可用函式，會比較精簡
while a==b or b==c or c==a:
    num=random.randint(100,999)
    a=num//100
    b=num//10-10*a
    c=num%10
    s=[a,b,c]
ans=0
A=0
B=0
while ans!=num:
    ans=eval(input('猜'))
    ansa=ans//100
    ansb=ans//10-ansa*10
    ansc=ans%10
    k=[ansa,ansb,ansc]
    for i in range(3):
        for j in range(3):
            if s[i]==k[j]:
                if i==j:
                    A=A+1
                else:
                    B=B+1
    print(A,'A',B,'B',sep='')
    time=time+1
    A=0
    B=0
print('答對了!!')
print('共猜了',time,'次')
