#Создание нового контакт теелфонного справочника

file = open('contacts.txt', 'r+')

contakts_bd = {"1":["Сергунов Иван Иванович","657890864","комментарий2"],"2":["Иванов Петр Иванович","5456863","комментарий3"],"3":["Петров Иван Иванович","564355654","комментарий1"]}

def create_bd(bd: dict):
    with open ('contacts.txt', 'w+', encoding="utf-8") as file:
        for key, value in bd.items():
            file.write(f'{key} :\n')
            file.write(f'{str(value)}\n')

create_bd(contakts_bd)

def vse_zapisi(filename):
   with open (filename, 'r+',encoding="utf-8") as file:
      print(file.readlines())

vse_zapisi('contacts.txt')


