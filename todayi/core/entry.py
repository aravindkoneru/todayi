from datetime import datetime, timezone


class Entry:
    def __init__(self):
        self._created = datetime.now(timezone.utc)
        self._edited = self._created
        self._tasks = {}

    def _update_edit(func):
        """
        decorator to update _edited timestamp
        """

        def wrap(*args, **kwargs):
            result = func(*args, **kwargs)
            self._edited = datetime.now(timezone.utc)
            return result

    def add(self, task: str) -> None:
        """
        add a task to the entry
        """
        count = self._tasks.get(task, 0) + 1
        self._tasks[task] = count

    @_update_edit
    def remove(self, task: str) -> None:
        """
        remove a task from the entry
        """
        count = self._tasks.get(task, 0) - 1

        if count == 0:
            del self._tasks[task]
        elif count > 0:
            self._tasks[task] = count

    def summary(self) -> str:
        """
        get a text summary of all the tasks for this entry
        """
        msg = []
        [msg.append(f"{task}: x{count}") for task, count in self._tasks]
        return "\n".join(msg)

    @property
    def created(self) -> datetime:
        return self._created

    @property
    def edited(self) -> datetime:
        return self._edited

    def unique_tasks(self) -> int:
        return len(self._tasks)

