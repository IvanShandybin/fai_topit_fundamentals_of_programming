def mean(vs:list[int|float])->float:
    if not vs:
        return 0.0
    t=0.0
    for v in vs:
        t+=v
    return t/len(vs)

def minimum(vs:list[int|float])->int|float|None:
    if not vs:
        return None
    r=vs[0]
    for v in vs[1:]:
        if v<r:
            r=v
    return r

def maximum(vs:list[int|float])->int|float|None:
    if not vs:
        return None
    r=vs[0]
    for v in vs[1:]:
        if v>r:
            r=v
    return r

def classify(sc:float)->str:
    if sc>=90:
        return "отличный"
    elif sc>=75:
        return "хороший"
    elif sc>=60:
        return "удовлетворительный"
    return "недостаточный"

def student_summary(nm:str,rs:list[int])->dict:
    if not rs:
        return {
            "name":nm,
            "mean":0.0,
            "min":None,
            "max":None,
            "category":"нет оценок",
            "has_results":False,
        }
    av=mean(rs)
    return {
        "name":nm,
        "mean":round(av,2),
        "min":minimum(rs),
        "max":maximum(rs),
        "category":classify(av),
        "has_results":True,
    }

def find_top_students(st:dict[str,list[int]])->list[str]:
    tp=[]
    ba=-1.0
    for nm,rs in st.items():
        if not rs:
            continue
        av=mean(rs)
        if av>ba:
            ba=av
            tp=[nm]
        elif av==ba:
            tp.append(nm)
    return tp

def group_summary(st:dict[str,list[int]])->dict:
    ct={
        "отличный":0,
        "хороший":0,
        "удовлетворительный":0,
        "недостаточный":0,
        "нет оценок":0,
    }
    vm=[]
    sm=[]
    for nm,rs in st.items():
        s=student_summary(nm,rs)
        sm.append(s)
        ct[s["category"]]+=1
        if s["has_results"]:
            vm.append(s["mean"])
    ga=round(mean(vm),2)if vm else 0.0
    tp=find_top_students(st)
    rk=sm.copy()
    n=len(rk)
    for i in range(n):
        mi=i
        for j in range(i+1,n):
            if rk[j]["mean"]>rk[mi]["mean"]:
                mi=j
        rk[i],rk[mi]=rk[mi],rk[i]
    return {
        "group_mean":ga,
        "categories":ct,
        "top_students":tp,
        "ranking":[r["name"]for r in rk],
    }

def format_report(sd:list[dict],gd:dict)->str:
    ln=["=== ОТЧЕТ ПО ГРУППЕ ==="]
    for s in sd:
        if s["has_results"]:
            ln.append(
                f"{s['name']}: среднее={s['mean']}, мин={s['min']}, макс={s['max']}, уровень={s['category']}"
            )
        else:
            ln.append(f"{s['name']}: нет результатов (уровень={s['category']})")
    ln.append(f"Средний балл группы: {gd['group_mean']}")
    ln.append(f"Лидеры: {', '.join(gd['top_students'])if gd['top_students']else 'нет'}")
    ln.append(f"Рейтинг: {', '.join(gd['ranking'])if gd['ranking']else 'пусто'}")
    ln.append(f"Распределение по категориям: {gd['categories']}")
    return "\n".join(ln)

sc_all={
    "1. Обычный набор":{
        "Анна":[78,91,84,88],
        "Борис":[60,72,68],
        "Дарья":[95,93,97,90],
        "Илья":[55,61],
    },
    "2. Один студент":{"Олег":[82,86]},
    "3. Несколько лидеров":{"Анна":[90,90],"Иван":[85,95],"Макс":[70,80]},
    "4. Пустая группа":{},
    "5. Студент без результатов":{"Анна":[80,90],"Петр":[]},
    "6. Граничные значения":{"А":[90],"Б":[75],"В":[60],"Г":[59]},
}

for tl,gr in sc_all.items():
    print(f"\n--- {tl} ---")
    sd=[student_summary(nm,rs)for nm,rs in gr.items()]
    gd=group_summary(gr)
    print(format_report(sd,gd))