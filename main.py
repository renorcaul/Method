def examination(do):
    while type(do) == str:
        try:
            do = int(input("> "))
        except ValueError:
            print("Вы вводите текст!")
    return int(do)


def choice(objects, page_size=5, message=''):
    if not objects:
        print("Нет списка!")
    else:
        if type(objects) == dict:
            b = []
            for key, value in objects.items:
                b.append(value)
            objects = b
        if message != "":
            print(message)
        count = 0
        count2 = 0
        for index, number in enumerate(objects):
            count += 1
            count2 += 1
            if count <= page_size:
                print(f"{count}. {number}")
                if count == page_size and (index + 1) != len(objects):
                    print("-" * 40)
                    print(f"{count+1}. Перейти на следующую страницу")
                    do = "0"
                    action = examination(do)
                    while action > count + 1 or action <= 0:
                        print("Нет такого действия!")
                        action = examination(do)
                    if action != (count+1):
                        return objects[count2 - (page_size - action) - 1]
                    count = 0
                elif (index + 1) == len(objects):
                    do = "0"
                    action = examination(do)
                    while action > count or action <= 0:
                        print("Нет такого действия!")
                        action = examination(do)
                    return objects[count2 - (page_size - action)]



import uuid
objects = [uuid.uuid4() for _ in range(11)]
page_size = 3
message = 'Выберите идентификатор товара:'
result = choice(objects, page_size, message)
print(result)
