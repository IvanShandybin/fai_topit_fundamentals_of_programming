def arithmetic_mean(vs:list[float])->float:
    if not vs:
        return 0.0
    t=0.0
    for v in vs:
        t+=v
    return t/len(vs)

def normalize_name(nm:str)->str:
    p=nm.strip().split()
    if not p:
        return ""
    return " ".join(x.capitalize()for x in p)

def build_report(
    st:str,
    rs:list[int],
    *,
    precision:int=2,
    prefix:str="Результат",
)->str:
    cn=normalize_name(st)
    if not rs:
        return f"{prefix}: {cn} — нет оценок"
    av=arithmetic_mean([float(x)for x in rs])
    return f"{prefix}: {cn} — средний балл {av:.{precision}f}"

def collect_tags(*tg:str,lowercase:bool=True)->tuple[str,...]:
    sn=set()
    r=[]
    for t in tg:
        c=t.strip()
        if lowercase:
            c=c.lower()
        if c and c not in sn:
            sn.add(c)
            r.append(c)
    return tuple(r)

assert arithmetic_mean([10.0,20.0,30.0])==20.0
assert arithmetic_mean([5.0])==5.0
assert arithmetic_mean([])==0.0

assert normalize_name("  иВАН   иванов ")=="Иван Иванов"
assert normalize_name("анна")=="Анна"
assert normalize_name("   ")==""

assert build_report("пётр",[4,5],precision=1)=="Результат: Пётр — средний балл 4.5"
assert build_report("анна",[],prefix="Итог")=="Итог: Анна — нет оценок"
assert build_report("иван",[5,5,4])=="Результат: Иван — средний балл 4.67"

assert collect_tags("Python"," python ","","API")==("python","api")
assert collect_tags("AI","ai",lowercase=False)==("AI","ai")
assert collect_tags("","   ")==()

rt=["  Web ","Backend","web"]
print(collect_tags(*rt,lowercase=True))

kw={"precision":3,"prefix":"Отчет"}
print(build_report("иван шандыбин",[90,95,100],**kw))

course="Программирование на Python"

def out_sc():
    st="в процессе"
    def in_sc():
        nonlocal st
        st="завершено"
        print("Внутри inner:",course,"|",st)
    print("До inner:",st)
    in_sc()
    print("После inner:",st)

out_sc()
print("Глобальный course:",course)

def add_res(v,rs=None):
    if rs is None:
        rs=[]
    else:
        rs=rs.copy()
    rs.append(v)
    return rs

print("Исправленный add_result:",add_res(5),add_res(4))

def app_res(op,vs):
    return [op(v)for v in vs]

def bns(x):
    return x+5

print("С именованной функцией:",app_res(bns,[70,80]))
print("С lambda:",app_res(lambda x:x*2,[10,20]))

def mk_chk(th):
    def chk(sc):
        return sc>=th
    return chk

p_ex=mk_chk(60)
h_ex=mk_chk(90)
print("Порог 60 для 75:",p_ex(75),"| Порог 90 для 75:",h_ex(75))