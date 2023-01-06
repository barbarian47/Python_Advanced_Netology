documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]
directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


def people(doc_num):
    for document in documents:
        if document['number'] == doc_num:
            return f"\nВладелец документа №{doc_num} - {document['name']}.\n"
    return f"\nДокумента №{doc_num} не существует.\n"


def shelf(doc_num):
    for directorie in directories:
        for number in directories[directorie]:
            if number == doc_num:
                return f"\nДокумент №{doc_num} находится на полке №{directorie}.\n"
    return f"\nДокумента №{doc_num} не существует.\n"


def current_doc(document):
    doc = f'{document["type"]} "{document["number"]}" "{document["name"]}"'

    return doc


def list_doc(documents):
    for document in documents:
        print(current_doc(document))

    return None


def add_doc(doc_num, doc_type, doc_name, doc_dir):
    directories[doc_dir].append(doc_num)
    new_doc = {"type": doc_type, "number": doc_num, "name": doc_name}
    documents.append(new_doc)
    return f"\nДокумент №{doc_num} добавлен на полку №{doc_dir}.\n"


def finder_doc(doc_num):
    for document in documents:
        if document["number"] == doc_num:
            return True
    return False


def del_doc(doc_num):
    for key in directories:
        if doc_num in directories[key]:
            directories[key].remove(doc_num)

    for document in documents:
        if document["number"] == doc_num:
            documents.remove(document)
    return f"\nДокумент №{doc_num} удалён.\n"


def move_doc(doc_num, doc_dir):
    for key in directories:
        if doc_num in directories[key]:
            directories[key].remove(doc_num)
            directories[doc_dir].append(doc_num)
            return (f"\nДокумент №{doc_num} перемещён с полки №{key} "
                    f"на полку №{doc_dir}\n")


def add_shelf(doc_dir):
    directories[doc_dir] = list()
    return f"\nПолка №{doc_dir} добавлена.\n"


def help_doc():
    help = """
Список доступных команд:
p - узнать имя владельца документа
s - узнать местонахождение документа
l - список всех документов
a - добавить документ
d - удалить документ
m - переместить документ
as - добавить полку
h - список команд
q - завершить программу
"""
    return help


def main():
    while True:
        prompt = "h - список команд\tq - завершить"
        prompt += "\nВведите команду: "
        command = input(prompt)
        if command == 'p':
            doc_num = input('Введите номер документа: ')
            print(people(doc_num))
        elif command == 's':
            doc_num = input('Введите номер документа: ')
            print(shelf(doc_num))
        elif command == 'l':
            print()
            list_doc(documents)
            print()
        elif command == 'a':
            doc_num = input("Введите номер документа: ")
            doc_type = input("Введите тип документа: ")
            doc_name = input("Введите имя владельца документа: ")
            doc_dir = input("Введите № полки: ")
            if doc_dir not in directories:
                print(f"\nПолки №{doc_dir} не существует.\n")
            else:
                print(add_doc(doc_num, doc_type, doc_name, doc_dir))
        elif command == 'd':
            doc_num = input("Введите номер документа: ")
            if finder_doc(doc_num):
                print(del_doc(doc_num))
            else:
                print(f"\nДокумента №{doc_num} не существует.\n")
        elif command == 'm':
            doc_num = input("Введите номер документа: ")
            if finder_doc(doc_num):
                doc_dir = input("Введите № полки: ")
                if doc_dir in directories:
                    print(move_doc(doc_num, doc_dir))
                else:
                    print(f"\nПолки №{doc_dir} не существует.\n")
            else:
                print(f"\nДокумента №{doc_num} не существует.\n")
        elif command == 'as':
            doc_dir = input("Введите № полки: ")
            if doc_dir not in directories:
                print(add_shelf(doc_dir))
            else:
                print(f"\nПолка №{doc_dir} уже существует.\n")
        elif command == 'h':
            print(help_doc())
        elif command == 'q':
            print("\nПРОГРАММА ЗАВЕРШЕНА")
            break
        else:
            print(f"\nКоманды '{command}' не существует.\n")


if __name__ == '__main__':
    main()