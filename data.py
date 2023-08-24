import data


def display_menu() -> str:
    """
    Функция для отображения главного меню и возврата выбора пользователя.
    """
    print("\n| Главное меню |\n")
    print("1. Просмотр контактов")
    print("2. Добавить новый контакт")
    print("3. Поиск контактов")
    print("4. Выйти")
    return input("Введите номер действия: ")


def show_contact(entry: dict[str, str]) -> None:
    """
    Функция для отображения одного контакта.
    """
    print()
    for key, value in entry.items():
        print(f"{key}: {value}")


def display_actions() -> str:
    """
    Функция для отображения меню действий с контактом и возврата выбора пользователя.
    """
    while True:
        print("\n| Выберите действие |\n")
        print("1. Редактировать контакт")
        print("2. Удалить контакт")
        print("3. Следующий контакт")
        print("4. Вернуться в главное меню")
        ans = input("Введите номер действия: ")
        if ans in ('1', '2', '3', '4'):
            return ans
        else:
            print("\n< Неверный выбор. Пожалуйста, выберите корректный номер действия. >")


def short_display_actions() -> str:
    """
    Функция для отображения короткого меню действий с контактом и возврата выбора пользователя.
    """
    while True:
        print("\n| Выберите действие |\n")
        print("1. Редактировать контакт")
        print("2. Удалить контакт")
        print("3. Вернуться в главное меню")
        ans = input("Введите номер действия: ")
        if ans in ('1', '2', '3'):
            return ans
        else:
            print("\n< Неверный выбор. Пожалуйста, выберите корректный номер действия. >")


def action_with_contact(entries: list[dict[str, str]], index: int) -> None:
    """
    Функция для действий с контактом.
    """
    while True:
        if not entries:
            print("\n< Список контактов пуст >")
            return
        print(f'\n| {index+1}/{len(entries)} |')
        show_contact(entries[index])
        choice = display_actions()
        if choice == '1':
            data.edit_entry(entries, index)
        elif choice == '2':
            data.delete_entry(entries, index)
        elif choice == '3':
            index = (index + 1) % len(entries)
        elif choice == '4':
            break
        else:
            print("Что-то пошло не так...")


def get_search_criteria() -> dict[str, str]:
    """
    Функция для получения от пользователя данных для поиска.
    """
    search_criteria = {}
    search_params = ['фамилия', 'имя', 'отчество', 'название организации', 'телефон рабочий', 'телефон личный(сотовый)']
    while True:
        print('\n| поиск |\n')
        for param in search_params:
            value = input(f"Введите значение для параметра '\033[92m{param}\033[0m' или клавишу '\033[92mEnter\033[0m' для пропуска: ")
            if value:
                search_criteria[param] = value
        if search_criteria:
            return search_criteria
        else:
            print("Нет значений для поиска. Введите хотя бы одно значение.")


def show_search_results(entries: list[dict[str, str]], results: list[int]) -> None:
    """
    Функция для работы с результатами поиска.
    """
    if not results:
        print("\n\033[92mКонтакты не найдены.\033[0m")
        return
    amount, num = len(results), 0
    print(f"\n\033[92mНайдено контактов: {amount}\033[0m")

    while amount > 1:
        num += 1
        amount -= 1
        print(f"\n< результат {num}/{len(results)} >")
        show_contact(entries[results[num-1]])
        choice = display_actions()
        if choice == '1':
            data.edit_entry(entries, results[num-1])
        elif choice == '2':
            data.delete_entry(entries, results[num-1])
            results = list(i - 1 for i in results)
        elif choice == '3':
            continue
        elif choice == '4':
            return
        else:
            print("Что-то пошло не так...")
    print(f"\n< результат {len(results)}/{len(results)} >")
    show_contact(entries[results[-1]])
    choice = short_display_actions()
    if choice == '1':
        data.edit_entry(entries, results[-1])
    elif choice == '2':
        data.delete_entry(entries, results[-1])
