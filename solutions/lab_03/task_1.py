def cls(sc,wt,ab):
    if not(0<=sc<=100)or not(0<=ab<=5):
        return None,"Ошибка: некорректные входные данные"
    lv=["отличный","хороший","удовлетворительный","недостаточный"]
    if sc>=90:
        i=0
    elif sc>=75:
        i=1
    elif sc>=60:
        i=2
    else:
        i=3
    if ab>3 and i<3:
        i+=1
    r=lv[i]
    match wt:
        case "exam":
            d="экзаменационная работа"
        case "project":
            d="проектная работа"
        case "practice":
            d="практическая работа"
        case _:
            d="неизвестный тип работы"
    return r,f"Балл: {sc}, Тип: {d}, Пропуски: {ab} -> Уровень: {r}"

tc=[
    (0,"exam",0),
    (59,"practice",2),
    (60,"project",1),
    (74,"exam",4),
    (75,"practice",0),
    (89,"project",5),
    (90,"exam",3),
    (100,"practice",4),
    (105,"exam",1),
    (80,"seminar",-1),
]

for sc,wt,ab in tc:
    _,m=cls(sc,wt,ab)
    print(m)

print()

rc=[
    (95,"exam",1),
    (88,"project",4),
    (62,"practice",0),
    (55,"exam",2),
    (75,"project",3),
    (90,"practice",5),
    (74,"exam",1),
    (100,"project",0),
    (60,"practice",4),
    (40,"exam",5),
]

sm={
    "отличный":0,
    "хороший":0,
    "удовлетворительный":0,
    "недостаточный":0,
}

for sc,wt,ab in rc:
    l,m=cls(sc,wt,ab)
    print(m)
    if l in sm:
        sm[l]+=1

print("Итоговая сводка:",sm)