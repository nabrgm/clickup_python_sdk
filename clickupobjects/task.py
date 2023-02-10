from clickup_python_sdk.clickupobjects.abstractobject import AbstractObject


class Task(AbstractObject):
    def __init__(self) -> None:
        super().__init__()

    def add_tag(self, tag=None):
        """
        Args: Tag object
        """
        route = "task/" + self["id"] + "/tag/" + tag["name"] + "/?"
        query = self.api._post(route=route)
        return query

    def update(self, values=None):
        """
        Args: dictionary of key pair values as described by clickups documentation
        """
        route = "task/" + self["id"] + "/"
        query = self.api._put(route=route, values=values)
        return query

    def update_custom_field(self, custom_field_id=None, values=None):
        """
        Args: custom field id is the field id to update (str)
                values is a dictionary of key pair values as described by clickups documentation
        """
        route = "task/" + self["id"] + "/field/" + custom_field_id
        query = self.api._post(route=route, values=values)
        return query

    def delete(self):
        route = "task/" + self["id"] + "/"
        query = self.api._delete(route=route)
        return query
