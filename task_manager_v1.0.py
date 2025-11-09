
from datetime import datetime

# Начальные задачи (уже выполненные)
tasks = [
    {
        "description": "Создать программу на языке Python",
        "completed": True,
        "created_date": "09.11.2025",
        "completed_date": "10.11.2025"
    },
    {
        "description": "Выложить программу в репозиторий GitHub", 
        "completed": True,
        "created_date": "09.11.2025",
        "completed_date": "11.11.2025"
    },
    {
        "description": "Выложить программу в репозиторий GitFlic",
        "completed": True, 
        "created_date": "09.11.2025",
        "completed_date": "12.11.2025"
    }
]

def get_current_date():
    """Возвращает текущую дату в формате ДД.ММ.ГГГГ"""
    return datetime.now().strftime("%d.%m.%Y")

def show_menu():
    print("\n" + "="*45)
    print("           🎯 МЕНЕДЖЕР ЗАДАЧ С ДАТАМИ")
    print("="*45)
    print("1. 📋 Показать все задачи")
    print("2. ➕ Добавить задачу")
    print("3. ❌ Удалить задачу") 
    print("4. ✅ Отметить выполненной")
    print("5. 🚪 Выйти")
    print("="*45)

def show_tasks():
    print("\n📋 ВАШИ ЗАДАЧИ:")
    if not tasks:
        print("   📭 Список пуст")
    else:
        for i, task in enumerate(tasks, 1):
            status = "✅" if task["completed"] else "⏳"
            created = task["created_date"]
            
            if task["completed"]:
                completed = task.get("completed_date", "Не указана")
                print(f"   {i}. [{status}] {task['description']}")
                print(f"      📅 Создана: {created} | ✅ Выполнена: {completed}")
            else:
                print(f"   {i}. [{status}] {task['description']}")
                print(f"      📅 Создана: {created} | ⏳ В процессе")
            print()

def add_task():
    print("\n➕ ДОБАВЛЕНИЕ ЗАДАЧИ")
    print("Доступные быстрые задачи:")
    print("1. Изучить Python")
    print("2. Сделать новый проект")
    print("3. Написать документацию")
    print("4. Своя задача")
    
    choice = input("Выберите вариант (1-4): ")
    
    if choice == '1':
        task_text = "Изучить Python"
    elif choice == '2':
        task_text = "Сделать новый проект"
    elif choice == '3':
        task_text = "Написать документацию"
    elif choice == '4':
        task_text = input("Введите свою задачу: ")
    else:
        print("❌ Неверный выбор")
        return
    
    if task_text.strip():
        new_task = {
            "description": task_text,
            "completed": False,
            "created_date": get_current_date(),
            "completed_date": None
        }
        tasks.append(new_task)
        print(f"✅ Добавлено: {task_text}")
        print(f"📅 Дата создания: {new_task['created_date']}")
    else:
        print("❌ Задача не может быть пустой")

def delete_task():
    if not tasks:
        print("\n📭 Нечего удалять!")
        return
    
    show_tasks()
    try:
        task_num = int(input("\nВведите номер задачи для удаления: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            print(f"❌ Удалено: {removed['description']}")
        else:
            print("❌ Неверный номер!")
    except:
        print("❌ Ошибка ввода!")

def complete_task():
    if not tasks:
        print("\n📭 Нечего отмечать!")
        return
    
    show_tasks()
    try:
        task_num = int(input("\nВведите номер задачи для отметки: "))
        if 1 <= task_num <= len(tasks):
            task = tasks[task_num - 1]
            
            if task["completed"]:
                print("ℹ️ Эта задача уже выполнена!")
                return
            
            # Спрашиваем дату выполнения
            print("\n📅 Укажите дату выполнения:")
            print("1. Сегодня (" + get_current_date() + ")")
            print("2. Другая дата")
            print("3. Без даты")
            
            date_choice = input("Выберите (1-3): ")
            
            if date_choice == '1':
                completed_date = get_current_date()
            elif date_choice == '2':
                completed_date = input("Введите дату (ДД.ММ.ГГГГ): ")
                # Простая проверка формата даты
                if len(completed_date) != 10 or completed_date[2] != '.' or completed_date[5] != '.':
                    print("⚠️  Используйте формат ДД.ММ.ГГГГ, установлена сегодняшняя дата")
                    completed_date = get_current_date()
            else:
                completed_date = "Не указана"
            
            task["completed"] = True
            task["completed_date"] = completed_date
            
            print(f"✅ Выполнено: {task['description']}")
            print(f"📅 Дата выполнения: {completed_date}")
        else:
            print("❌ Неверный номер!")
    except:
        print("❌ Ошибка ввода!")

# ОСНОВНАЯ ПРОГРАММА
print("🎉 ДОБРО ПОЖАЛОВАТЬ В МЕНЕДЖЕР ЗАДАЧ С ДАТАМИ!")
print("💡 Уже добавлены 3 выполненные задачи с разными датами")
print("💡 Используйте цифры 1-5 для навигации")

# Главный цикл
while True:
    show_menu()
    show_tasks()  # Всегда показываем текущие задачи
    
    choice = input("\n👉 Ваш выбор (1-5): ")
    
    if choice == '1':
        show_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        delete_task()
    elif choice == '4':
        complete_task()
    elif choice == '5':
        print("\n👋 До свидания! Ваши задачи:")
        show_tasks()
        break
    else:
        print("❌ Неверный выбор! Используйте 1-5")

print("\n✨ Программа завершена!")
