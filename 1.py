first_name = input("Как вас зовут? ")
last_name = input("Какая у вас фамилия? ")
person_age = int(input("Сколько вам лет? "))

# Форматирование строки с использованием .format()
info_string_format = "Имя: {im}, Фамилия: {fam}, Возраст: {vozr} лет".format(im=first_name, fam=last_name, vozr=person_age)
print(info_string_format)

# Форматирование строки с использованием f-строки
info_string_fstring = f"Имя: {first_name}, Фамилия: {last_name}, Возраст: {person_age} лет"
print(info_string_fstring)

