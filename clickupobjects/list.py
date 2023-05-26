from clickup_python_sdk.clickupobjects.abstractobject import AbstractObject


class List(AbstractObject):
    def __init__(self, id=None) -> None:
        super().__init__(id=id)

    def update(self, values=None):
        route = "list/" + self["id"]
        method = "PUT"
        response = self.api.make_request(method=method, route=route, values=values)

        return response

    def get_tasks(self, params=None):
        from clickup_python_sdk.clickupobjects.task import Task

        # this will work for now but I need to eventually include paging at the api instead
        finished_iteration = False
        result = []
        page = 0
        # TODO: run through key value pairs in params and add them to the route

        route = "list/" + self["id"] + "/task?subtasks=true"
        method = "GET"
        if params:
            for key, value in params.items():
                route += "&" + key + "=" + value

        while not finished_iteration:
            response = self.api.make_request(method=method, route=route + f"&page={page}")
            if len(response["tasks"]) == 0:
                finished_iteration = True
                break
            for space in response["tasks"]:
                result.append(Task.create_object(data=space, target_class=Task))
            page += 1
        return result

    def create_task(self, values=None):
        # I will need to refine my documentation later on god
        """
        Args: values is a dictionary with key values defining the task.
            information can be found here "https://clickup.com/api" under task creation
        """
        from clickup_python_sdk.clickupobjects.task import Task

        route = "list/" + self["id"] + "/task"
        method = "POST"

        response = self.api.make_request(method=method, route=route, values=values)
        return Task.create_object(data=response, target_class=Task)

    def get_custom_fields(self):
        from clickup_python_sdk.clickupobjects.customfield import CustomField

        route = "list/" + self["id"] + "/field"
        method = "GET"
        response = self.api.make_request(method=method, route=route)
        result = []
        for space in response["fields"]:
            result.append(CustomField.create_object(data=space, target_class=CustomField))
        return result
