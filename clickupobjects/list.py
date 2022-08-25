from clickup_python_sdk.clickupobjects.abstractobject import AbstractObject


class List(AbstractObject):
    def __init__(self) -> None:
        super().__init__()

    def get_tasks(self):
        from clickup_python_sdk.clickupobjects.task import Task

        # this will work for now but I need to eventually include paging
        route = "list/" + self["id"] + "/task?subtask=true&page=0"
        query = self.api.get(route=route)
        result = []
        for space in query["tasks"]:
            result.append(Task.create_object(data=space, target_class=Task))
        return result
