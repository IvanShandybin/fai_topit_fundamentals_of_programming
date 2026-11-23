sb=[
    ("anna","lab_01",5),
    ("boris","lab_01",4),
    ("anna","lab_02",5),
    ("daria","lab_01",3),
    ("boris","lab_02",5),
    ("anna","lab_01",4),
]

st=set()
lb=set()
sa={}
bs={}
ac={}

def add_sb(r):
    s,l,v=r
    st.add(s)
    lb.add(l)
    if s not in sa:
        sa[s]=[]
    sa[s].append((l,v))
    k=(s,l)
    if k not in bs or v>bs[k]:
        bs[k]=v
    ac[k]=ac.get(k,0)+1

for r in sb:
    add_sb(r)

bt={s for s in st if ("lab_01" in {x[0]for x in sa[s]})and("lab_02" in {x[0]for x in sa[s]})}
print("Сдали обе работы:",bt)

add_sb(("daria","lab_02",4))
bt2={s for s in st if {x[0]for x in sa[s]}>={"lab_01","lab_02"}}
print("После добавления Daria:",bt2)

def run_q(q):
    p=q.split()
    if not p:
        return "Пустой запрос"
    c=p[0]
    if c=="student" and len(p)==2:
        s=p[1]
        if s not in sa:
            return f"Студент {s} не найден"
        return f"Попытки {s}: {sa[s]}"
    elif c=="best" and len(p)==3:
        k=(p[1],p[2])
        if k not in bs:
            return f"Нет данных для {k}"
        return f"Лучший результат {k}: {bs[k]}"
    elif c=="attempts" and len(p)==3:
        k=(p[1],p[2])
        if k not in ac:
            return f"Нет данных для {k}"
        return f"Количество попыток {k}: {ac[k]}"
    elif c=="completed" and len(p)==2:
        l=p[1]
        rs=[s for(s,x)in bs if x==l]
        return f"Сдали {l}: {rs}"
    return "Неизвестная команда или неверные аргументы"

qs=[
    "student anna",
    "best anna lab_01",
    "attempts boris lab_02",
    "completed lab_01",
    "best unknown lab_01",
    "delete all",
]

for q in qs:
    print(f"> {q}\n  {run_q(q)}")