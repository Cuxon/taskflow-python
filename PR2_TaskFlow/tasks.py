from datetime import date, timedelta
from typing import Dict, List


Task = Dict[str, object]


def calculate_priority(importance: int, urgency: int) -> str:
    """Возвращает приоритет задачи по важности и срочности."""
    score = importance + urgency
    if score >= 8:
        return "Высокий"
    if score >= 5:
        return "Средний"
    return "Низкий"


def get_task_status(is_completed: bool, deadline: date) -> str:
    """Возвращает статус задачи с учетом срока выполнения."""
    if is_completed:
        return "Выполнена"
    if deadline < date.today():
        return "Просрочена"
    return "В работе"


def calculate_deadline(start_date: date, duration_days: int) -> date:
    """Рассчитывает дату окончания задачи."""
    if duration_days < 0:
        raise ValueError("Срок не может быть отрицательным.")
    return start_date + timedelta(days=duration_days)


def create_task(
    task_id: int,
    name: str,
    importance: int,
    urgency: int,
    duration_days: int,
) -> Task:
    """Создает словарь с данными учебной задачи."""
    if not name.strip():
        raise ValueError("Название задачи не может быть пустым.")
    if not 1 <= importance <= 5 or not 1 <= urgency <= 5:
        raise ValueError("Важность и срочность должны быть от 1 до 5.")

    start = date.today()
    deadline = calculate_deadline(start, duration_days)
    return {
        "id": task_id,
        "name": name.strip(),
        "importance": importance,
        "urgency": urgency,
        "deadline": deadline.isoformat(),
        "completed": False,
    }


def find_tasks(tasks: List[Task], query: str) -> List[Task]:
    """Ищет задачи по вхождению запроса в название."""
    query = query.strip().lower()
    return [task for task in tasks if query in str(task["name"]).lower()]


def filter_tasks_by_status(tasks: List[Task], status: str) -> List[Task]:
    """Возвращает задачи с указанным статусом."""
    result = []
    for task in tasks:
        deadline = date.fromisoformat(str(task["deadline"]))
        current_status = get_task_status(bool(task["completed"]), deadline)
        if current_status == status:
            result.append(task)
    return result


def sort_tasks_by_priority(tasks: List[Task]) -> List[Task]:
    """Сортирует задачи от высокого приоритета к низкому."""
    order = {"Высокий": 0, "Средний": 1, "Низкий": 2}
    return sorted(
        tasks,
        key=lambda task: order[
            calculate_priority(int(task["importance"]), int(task["urgency"]))
        ],
    )


def mark_task_completed(tasks: List[Task], task_id: int) -> bool:
    """Отмечает задачу выполненной. Возвращает True при успехе."""
    for task in tasks:
        if int(task["id"]) == task_id:
            task["completed"] = True
            return True
    return False
