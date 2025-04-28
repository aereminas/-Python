while True:
    try:
        age_input = input("Укажите ваш возраст: ")
        person_age = int(age_input)

        if person_age < 0:
            raise ValueError("Возраст не может быть меньше нуля!")

        if person_age >= 18:
            print("Вы достигли совершеннолетия.")
        else:
            print("Вы еще не достигли совершеннолетия.")
        break

    except ValueError:
        print("Ошибочный ввод: Пожалуйста, введите корректный возраст (целое число).")
