from clickup_python_sdk.clickupobjects.abstractobject import AbstractObject


class List(AbstractObject):
    def __init__(self) -> None:
        super().__init__()

    def get_tasks(self, params=None):
        from clickup_python_sdk.clickupobjects.task import Task

        # this will work for now but I need to eventually include paging at the api instead
        finished_iteration = False
        result = []
        page = 0
        # TODO: run through key value pairs in params and add them to the route

        route = "list/" + self["id"] + "/task?subtasks=true"
        if params:
            for key, value in params.items():
                route += "&" + key + "=" + value

        while not finished_iteration:
            query = self.api.get(route=route + f"&page={page}")
            if len(query["tasks"]) == 0:
                finished_iteration = True
                break
            for space in query["tasks"]:
                result.append(Task.create_object(data=space, target_class=Task))
            page += 1
        return result

    def create_task(self, values=None):
        # I will need to refine my documentation later on god
        """
        Args: values is a dictionary with key values defining the task.
                information can be found here "https://clickup.com/api" under task creation
        """
        route = "list/" + self["id"] + "/task"
        from clickup_python_sdk.clickupobjects.task import Task

        query = self.api.post(route=route, values=values)
        return Task.create_object(data=query, target_class=Task)

    def get_custom_fields(self):
        from clickup_python_sdk.clickupobjects.customfield import CustomField

        route = "list/" + self["id"] + "/field"
        # this will work for now but I need to eventually include paging
        # will need to check task count
        route = "list/" + self["id"] + "/task?subtasks=True&page=0"
        query = self.api.get(route=route)
        result = []
        for space in query["fields"]:
            result.append(CustomField.create_object(data=space, target_class=CustomField))
        return result


"""
  {
    "name": "New Task Name",
    "description": "New Task Description",
    "assignees": [
      183
    ],
    "tags": [
      "tag name 1"
    ],
    "status": "Open",
    "priority": 3,
    "due_date": 1508369194377,
    "due_date_time": false,
    "time_estimate": 8640000,
    "start_date": 1567780450202,
    "start_date_time": false,
    "notify_all": true,
    "parent": null,
    "links_to": null,
    "check_required_custom_fields": true,
    "custom_fields": [
      {
        "id": "0a52c486-5f05-403b-b4fd-c512ff05131c",
        "value": 23
      },
      {
        "id": "03efda77-c7a0-42d3-8afd-fd546353c2f5",
        "value": "Text field input"
      }
    ]
  }
"""
