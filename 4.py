while True:
    user_input = input("Ввод: ")

    if user_input.lower() == "выход":
        print("Завершение работы...")
        break

    if user_input.lstrip('-').isdigit():
        digit_count = len(user_input.lstrip('-'))
        print(f"В введенном значении {digit_count} цифр.")
    else:
        print("Ошибка: это не числовое значение.")

