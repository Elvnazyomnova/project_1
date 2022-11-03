#Файл для тестов

def make_coffee(size=250, sugar_dose=2):
    if sugar_dose > 5:
        return 'Слишком много сахара'
    else:
        return f'Ваш кофе объемом {size} мл с {sugar_dose} кусочками готов!'
text = make_coffee()

#Далее
def char_cleaner(string):
    '''
    Функция char_cleaner() принимает string 
    возвращает объект str без букв
    '''
    new_s = ''

    for i in s:
        if i.isdigit():
            new_s += i
    return new_s
s = 'Дата заказа: 2022-10-18_xdasa'

#Далее
name = 'Никита'
def greeting():
    global question
    question = 'Как дела,'
    print('Привет,', name, question)

def add_value(param):
    [].append(param)

#Lfktt
def print_them_all(*args):
    print('print them all')
    print('тип args:', type(args))
    print(args)
