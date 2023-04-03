
def tudeng_listisse(b:list, t:list):
    #Запрашиваем, сколько пользователей надо добавить, добавляем в списки. 
    #Имена студентов в список "tudengid", баллы в список "ballid".
    #
    
    n=int(input("Mitu sisseastujaid lisame? "))
   
    for j in range(n): # диапазон
        nimi=input("Nimi: ")
        t.append(nimi) #Добавление в конце списка
       
        ball=input("Ballid: ")
        b.append(ball) 

    print(t) 
    print(b)
   
    return b,t #Возвращение списков



def naitame_Tudengid(b:list, t:list):
    #Запрашиваем список поступивших студентов
   
    print("Sisseastujate arv on:", len(t)) #показываем кол-во студентов в списке
     
    n=int(input("Mitu inimesi naitame? ")) #спрашиваем сколько студентов показать

    for j in range(n):
        print(t[j], b[j]) #показываем списки поступивших



def abc_Jarjekord(b:list,t:list):
    #Отображаем в алфавитном порядке список людей и их баллы
    newList=[]
    n = len(t) 
    ind = 0 #счетчик для заполнения нового списка

    for i in range(n):
        unitedList = t[ind] +' '+ b[ind] # склеваем и обьеденяем
        newList.append(unitedList) #записываем в новый обьеденяющий список
        ind+=1 #счетчик, просмотр последующего студента

    newList.sort() #сортировка в алфовитном порядке

    for j in range(n):
        print(newList[j]) #выводим по строчно новый список



def minimaalne_Hinne(b:list, t:list):
    #Показывает студентa с худшими результатами 

    b=list(map(int,b)) #позволяет искать позицию, находит индекс
    minHinne=min(b)

    n=b.index(minHinne) #записываем инфу о индексе мин оценки
 
    print(f"Halvem tulemus: {minHinne}")

    nimi=t[n]
    print(f"Tudeng halvema tulemusega: {nimi}")  #Выводим имя под нужным индексом

   

def keskmineBall(b:list):
    #Находим средний балл поступивших
    summa=0
    for ballid in b:
        summa+=int(ballid)
    summa/=len(b) #делим на длину списка баллов
    print("Keskmine tulemus: ", round(summa,1)) #Выводим и округляем средний балл




def ballide_Jarjekorras(b:list, t:list):
    #Функция выводит список баллов, от большего к меньшему 
       
    pos = 1 

    for x in range(len(b)):
        
        c=list(map(int,b)) # Создаем новый список чисел с INT-ым значением 
        maxHinne=max(c)
        
        n=c.index(maxHinne)
        #(t[n]) - индекс студента в списке

        print(f"{pos}. parim ballide tulemus on: {maxHinne} sisseastuja: {t[n]}") 
       
        b.pop(n) # Удаляет из списка по индексу 
        t.pop(n)
        pos+=1
   





    """
def maksimaalne_Hinne(b:list, t:list):

    #Показывает студентa с лучшими результатами       
    b=list(map(int,b))
    maxHinne=max(b)

    n=b.index(maxHinne)

    j=int(input("Mitu parima tulemusega sisseastujaid näitame? "))
   
    pos=1 

    for n in range(j):
       
        b.sort(reverse=True) #сортирует список с баллами от большего к меньшему
        ball=b[n] #из списка баллов берем самое первое (под индексом 0)
        print(f"{pos}. Parim tulemus: {ball}")
       
        nimi=t[n]        
        print(f"Tudeng parima {pos}. tulemusega: {nimi}")
        n+=1 #переходим к следующему студенту
        pos+=1

    """