from clickup_python_sdk.clickupobjects.abstractobject import AbstractObject


class Task(AbstractObject):
    def __init__(self, id=None) -> None:
        super().__init__(id=id)

    def get_endpoint(self):
        assert self["id"] != None, "Must provide task id"
        return "task" + "/" + self["id"]

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

    # file = {"attachment": ("data.csv", open("logs/data.csv", "rb"))}
    # headers = {"Authorization": "pk_54006660_THIJHCCF4NS0DLNHCMFF6NMR88VHV8Z7"}
    # request = requests.post(f"https://api.clickup.com/api/v2/task/8677d5ua1/attachment", files=file, headers=headers)
    # print(request.json())
    def upload_file(self, file):
        import requests

        """
        Args: file is a dictionary of key pair values as described by clickups documentation
        """
        route = "task/" + self["id"] + "/attachment"
        method = "POST"
        response = self.api.make_request(method=method, route=route, file=file)
        return response

    def get_time_in_status(self):
        route = "task/" + self["id"] + "/time_in_status"
        method = "GET"
        response = self.api.make_request(method=method, route=route)
        return response
