# задание по первому уроку
"""
print('hello')
print('Привет программист')
print(2+2)
print('10/3')

#задание по уроку "переменные"

name='Яков'
print(name)

#задание по уроку "простые типы данных"

a=2
b=0.5
print(a+b)

name='Яков'
print(f'Привет, {name}')

print(int(input('Введите число от 1 до 10:'))+10)

name=input('Введите ваше имя: ')
print(f'Привет, {name}. Как дела?')

print(f"float('1') - 1.00, int('2.5') - typeError, bool(1) - True, bool('') - False, bool(0) - False")

# задание по уроку "комплексные типы данных"

# списки 

s=[3, 5, 7, 9, 10.5]
print(s)
s.append("Python")  
print(len(s))
print(s[0],s[-1],*s[:5])
s.remove("Python")
 
#словари 
d={"city": "Москва", "temperature": "20"}
print(d["city"])
d["temperature"]=int(d["temperature"])-5
print(d)
print(d.get('country'))
print(d.get('country','Россия'))
d['date']="27.05.2019"
print(len(d))
"""
# функции

def get_summ(one, two, delimiter='&'):
    return str(one)+delimiter+str(two)
    

l_p=get_summ("Learn","python")
print(l_p.upper())

def format_price(price):
    return f'цена {int(price)} руб.'

n = format_price(56.24)
print(n)


