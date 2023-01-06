import re
import csv


# Creates a formatted contact list from a dictionary
def create_phonebook(dict_person):
    phonebook = list()
    phonebook.append(['lastname', 'firstname', 'surname', 'organization',
                      'position', 'phone', 'email'])
    for key in dict_person:
        person = list()
        person.append(dict_person[key]['lastname'])
        person.append(dict_person[key]['firstname'])
        person.append(dict_person[key]['surname'])
        person.append(dict_person[key]['organization'])
        person.append(dict_person[key]['position'])
        person.append(dict_person[key]['phone'])
        person.append(dict_person[key]['email'])
        phonebook.append(person)
    
    return phonebook


# Converts the phone number to the required format
def format_phone(phone_number):
    pattern = r'(\+7|8)\s*\(*(d{3}|\d{3})\)*(-|\s)*(\d+)(-|\s)*(\d{2})(-|\s)*'
    pattern += '(\d{2})\s*\(*(доб.)*\s*(\d*)\)*'
    pattern_res = r'+7(\2)\4-\6-\8 \9\10'
    phone = re.sub(pattern, pattern_res, phone_number).strip()
    
    return phone


# Formats a list of contacts, concatenates duplicates and returns a dictionary
def format_contacts(contacts_list):
    phone_book = dict()
    
    for i in range(1, len(contacts_list)):
        full_name = contacts_list[i][0] + ' ' + contacts_list[i][1] + ' ' + \
                    contacts_list[i][2]
        full_name = full_name.strip().split(' ')
        check_name = full_name[0] + ' ' + full_name[1]
        
        if contacts_list[i][5]:
            phone = format_phone(contacts_list[i][5])
        else:
            phone = ''
        
        if check_name not in phone_book:
            if len(full_name) == 3:
                phone_book[check_name] = {
                                        'lastname': full_name[0],
                                        'firstname': full_name[1],
                                        'surname': full_name[2],
                                        'organization': contacts_list[i][3],
                                        'position': contacts_list[i][4],
                                        'phone': phone,
                                        'email': contacts_list[i][6]
                                        }
            elif len(full_name) == 2:
                phone_book[check_name] = {
                                        'lastname': full_name[0],
                                        'firstname': full_name[1],
                                        'surname': '',
                                        'organization': contacts_list[i][3],
                                        'position': contacts_list[i][4],
                                        'phone': phone,
                                        'email': contacts_list[i][6]
                                        }
        else:
            if not phone_book[check_name]['surname']:
                if len(full_name) == 3:
                    phone_book[check_name]['surname'] = full_name[3]
            if not phone_book[check_name]['organization']:
                phone_book[check_name]['organization'] = contacts_list[i][3]
            if not phone_book[check_name]['position']:
                phone_book[check_name]['position'] = contacts_list[i][4]
            if not phone_book[check_name]['phone']:
                phone_book[check_name]['phone'] = phone
            if not phone_book[check_name]['email']:
                phone_book[check_name]['email'] = contacts_list[i][6]
    
    return create_phonebook(phone_book)


def main():
    with open("phonebook_raw.csv", encoding='utf-8') as f:
      rows = csv.reader(f, delimiter=",")
      contacts_list = list(rows)
    
    phonebook = format_contacts(contacts_list)
    
    with open("phonebook.csv", "w", newline='', encoding='utf-8') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(phonebook)


if __name__ == '__main__':
    main()