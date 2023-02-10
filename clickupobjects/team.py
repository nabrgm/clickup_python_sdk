from clickup_python_sdk.clickupobjects.abstractobject import AbstractObject


class Team(AbstractObject):
    def __init__(self) -> None:
        super().__init__()

    def get_spaces(self, fields=None):
        from clickup_python_sdk.clickupobjects.space import Space

        route = "team/" + self["id"] + "/space?"
        query, headers = self.api._get(route=route)
        result = []
        for space in query["spaces"]:
            result.append(Space.create_object(data=space, target_class=Space, response_headers=headers))
        return result
