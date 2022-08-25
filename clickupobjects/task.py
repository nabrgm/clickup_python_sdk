from clickup_python_sdk.clickupobjects.abstractobject import AbstractObject


class Task(AbstractObject):
    def __init__(self) -> None:
        super().__init__()

    def add_tag(self, tag=None):
        """
        Args: Tag object
        """
        route = "task/" + self["id"] + "/tag/" + tag["name"] + "/?"
        query = self.api.post(route=route)
        return query
