import sqlite3
from Task import Task, TaskDiff

con = sqlite3.connect("taskDB")
# con.set_trace_callback(print)
cur = con.cursor()


def SelectAll():
    res = list()

    for row in cur.execute("SELECT * FROM Tasks"):
        res.append(Task(subject=row[1], number=row[2], name=row[3], typee=row[4],
                        deadline=row[5], points=row[6], status=row[7], date=row[8], ref=row[9]))

    return res


def Insert(tasks: list[Task]):

    for task in tasks:
        cur.execute("INSERT INTO Tasks (subject, number, name, type, deadline, points, status, date, ref) "
                    "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                    [task.subject,
                    task.number,
                    task.name,
                    task.type,
                    task.deadline,
                    task.points,
                    task.status,
                    task.date,
                    task.ref])

        con.commit()


def Update(tasks: list[TaskDiff]):

    for task in tasks:
        cur.execute("UPDATE Tasks SET deadline = ?, points = ?, status = ?, date = ?, ref = ?"
                    "WHERE subject = ? AND name = ?",
                    [task.task.deadline, task.task.points, task.task.status, task.task.date, task.task.ref,
                    task.task.subject, task.task.name])

        con.commit()
