import csv


def read_entries(filename: str) -> list[dict[str, str]]:
    """
    Функция для чтения записей из файла.
    """
    entries = []
    try:
        with open(filename, 'r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                entries.append(row)
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
    except Exception as e:
        print(f"Произошла ошибка при чтении файла: {e}")
    return entries


def write_entries(filename: str, entries: list[dict[str, str]]) -> None:
    """
    Функция для записи контактов в файл.
    """
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            fieldnames = entries[0].keys() if entries else []
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(entries)
    except Exception as e:
        print(f"Произошла ошибка при записи файла: {e}")


def validate_entry(entry: dict[str, str]) -> bool:
    """
    Проверка на минимальное заполнение формы для сохранения контакта.
    """
    phone_fields = ['телефон рабочий', 'телефон личный(сотовый)']
    other_fields = ['фамилия', 'имя', 'отчество', 'название организации']
    has_phone = any(entry[field] for field in phone_fields)
    has_other = any(entry[field] for field in other_fields)
    return has_phone and has_other


def add_entry(entries: list[dict[str, str]]) -> None:
    """
    Функция для добавления нового контакта.
    """
    fields = ['фамилия', 'имя', 'отчество', 'название организации', 'телефон рабочий', 'телефон личный(сотовый)']
    entry = {}
    print("\n| Добавление контакта |\n")
    for field in fields:
        entry[field] = input(f"Введите значение для поля \033[92m{field}\033[0m: ")

    if validate_entry(entry):
        entries.append(entry)  # Добавляем новую запись в список
        entries.sort(key=lambda x: (x['фамилия'].lower(), x['имя'].lower(), x['отчество'].lower()))  #сортируем список
        print("\n< \033[92mЗапись добавлена\033[0m >")
    else:
        print("\nОшибка: Должен быть номер телефона и хотя бы одно другое поле.")


def edit_entry(entries: list[dict[str, str]], index: int) -> None:
    """
    Функция для редактирования записи.
    """
    entry = entries[index]
    print("\n| Режим редактирования |\n")
    for key in entry.keys():
        entry[key] = input(f"{key}: {entry[key]}\nВведите новое значение {key}: ")
    print("\n< \033[92mЗапись успешно изменена\033[0m >")


def search_entries(entries: list[dict[str, str]], search_criteria: dict[str, str]) -> list[int]:
    """
    Функция для поиска контактов по одному или нескольким полям.
    """
    indices = []
    for index, entry in enumerate(entries):
        if all(value.lower() in entry[key].lower() for key, value in search_criteria.items()):
            indices.append(index)
    return indices


def delete_entry(entries: list[dict[str, str]], index: int) -> None:
    """
    Функция для удаления записи.
    """
    choice = input('\nДля подтверждения нажмите "\033[92m1\033[0m" или любую клавишу для отмены')
    if choice == '1':
        del entries[index]
        print("\n< \033[92mЗапись успешно удалена\033[0m >")
