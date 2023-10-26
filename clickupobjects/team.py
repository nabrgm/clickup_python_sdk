from clickup_python_sdk.clickupobjects.abstractobject import AbstractObject


class Team(AbstractObject):
    def __init__(self) -> None:
        super().__init__()

    def get_spaces(self, fields=None):
        from clickup_python_sdk.clickupobjects.space import Space

        route = "team/" + self["id"] + "/space?"
        method = "GET"
        response = self.api.make_request(method=method, route=route)

        result = []
        for space in response["spaces"]:
            result.append(Space.create_object(data=space, target_class=Space))
        return result

    def get_task_templates(self, page=0):
        from clickup_python_sdk.clickupobjects.tasktemplate import TaskTemplate

        route = "team/" + self["id"] + "/taskTemplate"
        method = "GET"
        params = {"page": page}
        response = self.api.make_request(method=method, route=route, params=params)
        return response
