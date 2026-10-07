from models import Task, User
from storage import load_tasks, load_users, save_tasks, save_users
from tasks import create_task, find_tasks, sort_by_priority
from users import create_user, find_user

TASKS_FILE = "data/tasks.json"
USERS_FILE = "data/users.json"


def show_tasks(tasks: list[Task]) -> None:
    if not tasks:
        print("Задач нет.")
        return
    for task in tasks:
        print(task)


def main() -> None:
    tasks = load_tasks(TASKS_FILE)
    users = load_users(USERS_FILE)

    while True:
        print("\n=== TaskFlow ===")
        print("1. Показать задачи")
        print("2. Создать задачу")
        print("3. Найти задачу")
        print("4. Показать задачи по приоритету")
        print("5. Показать пользователей")
        print("6. Создать пользователя")
        print("7. Найти пользователя")
        print("0. Выход")

        choice = input("Выберите действие: ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            title = input("Название: ").strip()
            description = input("Описание: ").strip()
            priority = input("Приоритет (низкий/средний/высокий): ").strip()
            due_date = input("Срок YYYY-MM-DD или Enter: ").strip() or None
            task = create_task(tasks, title, description, priority, due_date)
            save_tasks(TASKS_FILE, tasks)
            print(f"Создана задача: {task}")
        elif choice == "3":
            show_tasks(find_tasks(tasks, input("Поиск: ")))
        elif choice == "4":
            show_tasks(sort_by_priority(tasks))
        elif choice == "5":
            for user in users:
                print(user)
        elif choice == "6":
            user = create_user(users, input("Имя: "), input("Email: "))
            save_users(USERS_FILE, users)
            print(f"Создан пользователь: {user}")
        elif choice == "7":
            for user in find_user(users, input("Поиск: ")):
                print(user)
        elif choice == "0":
            break
        else:
            print("Неизвестная команда.")


if __name__ == "__main__":
    main()
