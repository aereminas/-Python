while True:
    try:
        number_input = input("Пожалуйста, введите целое положительное число: ")
        number = int(number_input)

        if number < 0:
            raise ValueError("Введенное число должно быть больше нуля.")

        if number % 2 == 0:
            print(f"Число {number} - парное")
        else:
            print(f"Число {number} - непарное")
        break

    except ValueError:
        print("Упс! Кажется, вы ввели что-то не то. Попробуйте ввести целое число еще раз.")

