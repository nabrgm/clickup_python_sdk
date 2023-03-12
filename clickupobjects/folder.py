from clickup_python_sdk.clickupobjects.abstractobject import AbstractObject


class Folder(AbstractObject):
    def __init__(self, id=None) -> None:
        super().__init__(id=id)

    def get_lists(self, params=None):
        from clickup_python_sdk.clickupobjects.list import List

        route = "folder/" + self["id"] + "/list"
        method = "GET"
        response = self.api.make_request(method=method, route=route)
        return [AbstractObject.create_object(data=l, target_class=List) for l in response["lists"]]
