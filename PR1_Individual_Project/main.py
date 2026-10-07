from datetime import date, timedelta


def calculate_priority(importance: int, urgency: int) -> str:
    """Определяет приоритет учебной задачи."""
    score = importance + urgency

    if score >= 8:
        return "Высокий"
    elif score >= 5:
        return "Средний"
    return "Низкий"


def get_task_status(is_completed: bool, deadline: date) -> str:
    """Определяет текущий статус задачи."""
    today = date.today()

    if is_completed:
        return "Выполнена"
    elif deadline < today:
        return "Просрочена"
    return "В работе"


def calculate_deadline(start_date: date, duration_text: str) -> date:
    """Преобразует срок из строки в число дней и рассчитывает дату окончания."""
    duration_days = int(duration_text)
    return start_date + timedelta(days=duration_days)


def main() -> None:
    # Исходные данные сценария.
    task_name = "Подготовить отчет по ПР1"
    importance = 5
    urgency = 4
    is_completed = False

    start_date = date.today()
    deadline = calculate_deadline(start_date, "7")
    priority = calculate_priority(importance, urgency)
    status = get_task_status(is_completed, deadline)

    print("=== TaskFlow ===")
    print(f"Задача: {task_name}")
    print(f"Приоритет: {priority}")
    print(f"Срок выполнения: {deadline}")
    print(f"Статус: {status}")


if __name__ == "__main__":
    main()
