import re
import csv
from pprint import pprint


def data_processing():
    phone_regex = r'(\+7|8)\s?\(?(\d{3})\)?(\s|-?)(\d{3})(\s|-)?(\d{4}|\d{2})(\s|-)?(\d{2})\s?\(?(доб.\s\d{4})?\)?'
    with open("phonebook_raw.csv", encoding="utf-8") as f:
        rows = csv.DictReader(f, delimiter=',')
        correct_data = []
        counter = 0
        for employee in rows:
            people_info = {}

            # Обработка ФИО
            last_name = employee['lastname'].split(' ')
            first_name = employee['firstname'].split(' ')
            surname = employee['surname']
            if len(last_name) == 2:
                people_info['lastname'] = last_name[0]
                people_info['firstname'] = last_name[1]
                if len(first_name) == 1:
                    people_info['surname'] = first_name[0]
            elif len(last_name) == 3:
                people_info['lastname'] = last_name[0]
                people_info['firstname'] = last_name[1]
                people_info['surname'] = last_name[2]
            else:
                people_info['lastname'] = last_name[0]
                if len(first_name) == 2:
                    people_info['firstname'] = first_name[0]
                    people_info['surname'] = first_name[1]
                else:
                    people_info['firstname'] = first_name[0]
                    people_info['surname'] = surname
            people_info['organization'] = employee['organization']
            people_info['position'] = employee['position']
            phone = re.search(phone_regex, employee['phone'])
            # Привидение номера телефона к указанному формату, если он есть.
            if phone is not None:
                if not phone.group(9):
                    phone = re.sub(phone_regex, r"+7(\2)\4-\6-\8", employee['phone'])
                else:
                    phone = re.sub(phone_regex, r"+7(\2)\4-\6-\8 \9", employee['phone'])
                people_info['phone'] = phone
            people_info['email'] = employee['email']
            flag = True
            # Исключение повторяющихся записей по Фамилии-Имени
            # путем добавления новой информации в уже существующую запись.
            for people in correct_data:
                if people['firstname'] == people_info['firstname'] and people['lastname'] == people_info['lastname']:
                    for key in people_info:
                        if people_info[key] != '':
                            people[key] = people_info[key]
                    flag = False
            # Если запись не была найдена, добавляем ее
            if flag:
                correct_data.append(people_info)
            counter += 1

        return correct_data

def file_recording(data):
    with open("phonebook.csv", 'w', newline='') as f:
        datawriter = csv.DictWriter(f,fieldnames=['lastname', 'firstname', 'surname', 'organization', 'position', 'phone', 'email'])
        datawriter.writeheader()
        print('\n[ЗАПИСИ]\n')
        for info in data:
            pprint(f'{info}')
            print()
            datawriter.writerow({'lastname': info['lastname'],
                                 'firstname': info['firstname'],
                                 'surname': info['surname'],
                                 'organization' : info['organization'],
                                 'position': info['position'],
                                 'phone': info['phone'],
                                 'email': info['email']})
        print('-' * 60)