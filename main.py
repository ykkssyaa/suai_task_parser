import parser, repository
from Task import Task, TaskDiff

# TODO: Просмотр текущих заданий, фильтрация


def difference(tasks: list[Task], savedTasks: list[Task]):
    updated = list()
    created = list()

    for task in tasks:
        flag = False

        for i in range(len(savedTasks)):
            sTask = savedTasks[i]

            # Задание уже было сохранено
            if task.name == sTask.name and task.subject == sTask.subject and task.ref == sTask.ref:
                flag = True

                dif = TaskDiff(task, sTask)

                # Если есть изменения в задании
                if dif.dif["hasUpdates"]:
                    updated.append(dif)

                # Больше это задание не просматриваем
                savedTasks.pop(i)
                break

        if not flag:  # Если задание не было сохранено
            created.append(task)

    return updated, created


def logChanges(updated: list[TaskDiff], created: list[Task]):

    n = 10
    i = [print("\n") for i in range(n)]

    print(f"Новых заданий: {len(created)}, изменений в заданиях: {len(updated)}")

    if len(created) != 0:
        print("Новые:\n\n")
        for task in created:
            task.print("\n")
            print("\n")

    n = 4
    i = [print("\n") for i in range(n)]

    if len(updated) != 0:
        print("Изменения:")
        for task in updated:
            task.print("\n")
            print("\n")


def main():
    print("Parsing tasks from pro.guap.ru...")
    tasks = parser.tasks()

    print("Parsing saved tasks from DB...")
    savedTasks = repository.SelectAll()

    print("Comparing...")
    updated, created = difference(tasks, savedTasks)

    logChanges(updated, created)

    print("Update new data...")
    if len(created) != 0:
        repository.Insert(created)

    if len(updated) != 0:
        repository.Update(updated)


if __name__ == '__main__':
    main()
