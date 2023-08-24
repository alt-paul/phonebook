import data
import interface

def main() -> None:
    """
    Основная функция.
    """
    entries = data.read_entries("phonebook.csv")

    while True:
        try:
            choice = interface.display_menu()

            if choice == '1':
                interface.action_with_contact(entries, 0)
            elif choice == '2':
                data.add_entry(entries)
            elif choice == '3':
                search_param = interface.get_search_criteria()
                search_results = data.search_entries(entries, search_param)
                interface.show_search_results(entries, search_results)
            elif choice == '4':
                data.write_entries("phonebook.csv", entries)
                print("\n< \033[92mПрограмма завершена\033[0m >")
                break
            else:
                print("Неверный выбор. Пожалуйста, выберите корректный номер действия.")
        except Exception as e:
            print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()
