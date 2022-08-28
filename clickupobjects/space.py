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


# this is the desired input for requests
"""
    def in_dev_get_lists(fields=None, params=None):
        from clickupobjects.list import List

        endpoint = "list"
        # self will also be passed in to get the endpoint
        param_types = {"archived": bool}
        field_types = [List.Fields.__dict__.values()]

        request = ClickupRequest(
            node=self["id"],
            method="GET",
            api=self.api,
            target_class=List,
            # api type indicates whether there will paging in this request or not
            # self will be passed in to type checker to get valid fields
            param_checker=TypeChecker(param),
            object_parser=ObjectParser(target_class=List)
        )
        
        if request.error():
            raise request.error()
        return request.execute()

    @classmethod
    def get_endpoint(cls):
        return "space"
"""
