from clickup_python_sdk.clickupobjects.abstractobject import AbstractObject


class Folder(AbstractObject):
    def __init__(self) -> None:
        super().__init__()

    def get_lists(self, params=None):
        from clickup_python_sdk.clickupobjects.list import List

        route = "folder/" + self["id"] + "/list"
        data, headers = self.api._get(route=route)
        return [
            AbstractObject.create_object(data=l, target_class=List, response_headers=headers) for l in data["lists"]
        ]
