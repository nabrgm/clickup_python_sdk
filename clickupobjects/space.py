from clickupobjects.abstractobject import AbstractObject


class Space(AbstractObject):
    def __init__(self) -> None:
        super().__init__()

    def get_lists(self, fields=None):
        from clickupobjects.list import List

        route = "space/" + self["id"] + "/list?"
        query = self.api.get(route=route)
        result = []
        for space in query["lists"]:
            result.append(List.create_object(data=space, target_class=List))
        return result
