from clickup_python_sdk.clickupobjects.abstractobject import AbstractObject


class Space(AbstractObject):
    def __init__(self) -> None:
        super().__init__()

    def get_lists(self, fields=None):
        from clickup_python_sdk.clickupobjects.list import List

        route = "space/" + self["id"] + "/list?"
        method = "GET"
        response = self.api.make_request(method=method, route=route)
        result = []
        for space in response["lists"]:
            result.append(List.create_object(data=space, target_class=List))
        return result

    def get_tags(self):
        from clickup_python_sdk.clickupobjects.tags import Tag

        route = "space/" + self["id"] + "/tag"
        method = "GET"
        response = self.api.maek_request(method=method, route=route)
        result = []
        for space in response["tags"]:
            result.append(Tag.create_object(data=space, target_class=Tag))
        return result

    def create_tag(self, name):
        values = {"tag": {"name": name}}
        route = "space/" + self["id"] + "/tag"
        method = "POST"
        data = self.api.make_request(method=method, route=route, values=values)
        return data

    def get_folders(self, params=None):
        from clickup_python_sdk.clickupobjects.folder import Folder

        route = "space/" + self["id"] + "/folder"
        method = "GET"
        query = self.api.make_request(method=method, route=route)
        return [AbstractObject.create_object(data=folder, target_class=Folder) for folder in query["folders"]]
