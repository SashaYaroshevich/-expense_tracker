expenses = []

def add_expense():
    date = input("Введите дату расхода: ")
    category = input("Введите категорию расхода: ")
    amount = float(input("Введите сумму расхода: "))
    expense = {"Дата": date, "Категория": category, "Сумма": amount}
    expenses.append(expense)
    print("Расход успешно добавлен!")

def show_expenses():
    if len(expenses) == 0:
        print("Нет расходов")
    else:
        for expense in expenses:
            print(f"Дата: {expense['Дата']}, Категория: {expense['Категория']}, Сумма: {expense['Сумма']}")

def calculate_total_expenses():
    total = 0
    for expense in expenses:
        total += expense['Сумма']
    print(f"Общая сумма расходов: {total}")

def filter_expenses():
    filter_category = input("Введите категорию для фильтрации расходов (или нажмите Enter для пропуска): ")
    filter_date = input("Введите дату для фильтрации расходов (или нажмите Enter для пропуска): ")

    filtered_expenses = []
    for expense in expenses:
        if (filter_category == "" or expense['Категория'] == filter_category) and (filter_date == "" or expense['Дата'] == filter_date):
            filtered_expenses.append(expense)

    if len(filtered_expenses) == 0:
        print("Нет расходов, удовлетворяющих заданным условиям")
    else:
        for expense in filtered_expenses:
            print(f"Дата: {expense['Дата']}, Категория: {expense['Категория']}, Сумма: {expense['Сумма']}")

def main():
    while True:
        print("1. Добавить расход")
        print("2. Вывести все расходы")
        print("3. Посчитать общую сумму расходов")
        print("4. Фильтровать расходы")
        print("5. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            show_expenses()
        elif choice == "3":
            calculate_total_expenses()
        elif choice == "4":
            filter_expenses()
        elif choice == "5":
            break
        else:
            print("Неверный выбор. Попробуйте еще раз.")

if __name__ == "__main__":
    main()