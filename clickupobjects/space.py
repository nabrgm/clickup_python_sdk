from clickup_python_sdk.clickupobjects.abstractobject import AbstractObject


class Space(AbstractObject):
    def __init__(self) -> None:
        super().__init__()

    def get_lists(self, fields=None):
        from clickup_python_sdk.clickupobjects.list import List

        route = "space/" + self["id"] + "/list?"
        query = self.api.get(route=route)
        result = []
        for space in query["lists"]:
            result.append(List.create_object(data=space, target_class=List))
        return result

    def get_tags(self):
        from clickup_python_sdk.clickupobjects.tags import Tag

        route = "space/" + self["id"] + "/tag"
        query = self.api.get(route=route)
        result = []
        for space in query["tags"]:
            result.append(Tag.create_object(data=space, target_class=Tag))
        return result

    def create_tag(self, name):
        values = {"tag": {"name": name}}
        route = "space/" + self["id"] + "/tag"
        query = self.api.post(route=route, values=values)
        return query
