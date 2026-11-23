import random

ms=[12,15,11,18,18,9,21,15,7,18]

s=0
mn=ms[0]
mx=ms[0]
ev=0

for x in ms:
    s+=x
    if x<mn:
        mn=x
    if x>mx:
        mx=x
    if x%2==0:
        ev+=1

av=s/len(ms)
ab=0
for x in ms:
    if x>av:
        ab+=1

print(f"Сумма: {s}, Мин: {mn}, Макс: {mx}, Четных: {ev}, Выше среднего ({av}): {ab}")

def lin_s(a,t):
    c=0
    for i in range(len(a)):
        c+=1
        if a[i]==t:
            return i,c
    return -1,c

u=int(input("Введите число для поиска: "))
ix,_=lin_s(ms,u)
print("Индекс:",ix)

def is_pr(n):
    if n<2:
        return False
    d=2
    while d*d<=n:
        if n%d==0:
            return False
        d+=1
    return True

print("Проверка простоты (17, 18, 1):",is_pr(17),is_pr(18),is_pr(1))

def sel_srt(a):
    r=a.copy()
    n=len(r)
    for i in range(n):
        mi=i
        for j in range(i+1,n):
            if r[j]<r[mi]:
                mi=j
        r[i],r[mi]=r[mi],r[i]
    return r

def bin_s(a,t):
    l=0
    r=len(a)-1
    c=0
    while l<=r:
        m=(l+r)//2
        c+=1
        if a[m]==t:
            return m,c
        c+=1
        if a[m]<t:
            l=m+1
        else:
            r=m-1
    return -1,c

print("\nРазмер | Линейный (сравнений) | Бинарный (сравнений)")
for sz in [10,100,1000]:
    dt=[random.randint(1,sz*5)for _ in range(sz)]
    sd=sel_srt(dt)
    tg=sd[-1]
    _,lc=lin_s(sd,tg)
    _,bc=bin_s(sd,tg)
    print(f"{sz:<6} | {lc:<20} | {bc:<20}")