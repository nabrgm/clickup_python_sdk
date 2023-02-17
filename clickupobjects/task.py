from clickup_python_sdk.clickupobjects.abstractobject import AbstractObject


class Task(AbstractObject):
    def __init__(self) -> None:
        super().__init__()

    def add_tag(self, tag=None):
        """
        Args: Tag object
        """
        route = "task/" + self["id"] + "/tag/" + tag["name"] + "/?"
        response = self.api.make_request(route=route)
        return response

    def update(self, values=None):
        """
        Args: dictionary of key pair values as described by clickups documentation
        """
        route = "task/" + self["id"] + "/"
        method = "PUT"
        response = self.api.make_request(method=method, route=route, values=values)
        return response

    def update_custom_field(self, custom_field_id=None, value=None):
        """
        Args: custom field id is the field id to update (str)
                values is a dictionary of key pair values as described by clickups documentation
        """
        route = "task/" + self["id"] + "/field/" + custom_field_id
        method = "POST"
        values = {"value": value}
        response = self.api.make_request(method=method, route=route, values=values)
        return response

    def delete(self):
        route = "task/" + self["id"] + "/"
        method = "DELETE"
        response = self.api.make_request(method=method, route=route)
        return response
