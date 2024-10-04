class Task:
    def __init__(self, subject, number, name, typee, deadline, points, status, date, ref):
        self.subject = subject
        self.number = number
        self.name = name
        self.type = typee
        self.deadline = deadline
        self.points = points
        self.ref = ref

        if status is not None and len(status) != 0:
            self.status = status
        else:
            self.status = None
        self.date = date

    def toString(self, sep='|'):
        return f"{self.subject}({self.number}) {sep} " \
               f"{self.name}  ({self.type}) {sep} " \
               f"Deadline: {self.deadline} {sep}" \
               f"Status {self.status} Points: {self.points}" \
               f"\t{self.ref}"

    def print(self, sep='|'):
        print(self.toString(sep))


# TaskDiff.dif -> map
# {
#   "deadline" : bool,
#   "status" : bool,
#   "points" : bool,
#   "date" : bool
# }
class TaskDiff:

    def __init__(self, new_task: Task, old_task: Task):
        self.task = new_task
        self.oldTask = old_task
        self.dif = self.diff(new_task, old_task)

    def diff(self, new_task: Task, old_task: Task) -> dict:

        dif = {
            "deadline": False,
            "status": False,
            "points": False,
            "date": False,
            "hasUpdates": False
        }

        if new_task.status != old_task.status:
            dif["status"] = True
            dif["hasUpdates"] = True

        if new_task.deadline != old_task.deadline:
            dif["deadline"] = True
            dif["hasUpdates"] = True

        if new_task.points != old_task.points:
            dif["points"] = True
            dif["hasUpdates"] = True

        if new_task.date != old_task.date:
            dif["date"] = True
            dif["hasUpdates"] = True

        return dif

    def print(self, sep=" | "):

        print(f"{self.task.subject}({self.task.number}) {sep} "
              f"{self.task.name}  ({self.task.type}) ", end=sep)

        if not self.dif["deadline"]:
            print(f" Deadline: {self.task.deadline} ", end=sep)
        else:
            print(f"!Deadline: {self.oldTask.deadline} -> {self.task.deadline} ", end=sep)

        if not self.dif["status"]:
            print(f"Status {self.task.status} ", end=sep)
        else:
            print(f"!Status: {self.oldTask.status} -> {self.task.status} ", end=sep)

        if not self.dif["points"]:
            print(f" Points: {self.task.points}", end=sep)
        else:
            print(f"!Points: {self.oldTask.points} -> {self.task.points} ", end=sep)

        if not self.dif["date"]:
            print(f"Date: {self.task.date}", end=sep)
        else:
            print(f"!Date: {self.oldTask.date} -> {self.task.date} ", end=sep)

        print(f"{self.task.ref}\n")
