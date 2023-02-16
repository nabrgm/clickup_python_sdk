import requests, time, sys, json
from clickup_python_sdk.config import API, VERSION


class ClickupClient(object):
    API = API
    SDK_VERSION = VERSION

    def __init__(self) -> None:
        pass

    @classmethod
    def init(cls, user_token=None):
        assert user_token != None, "Must provide user token"
        cls._set_default_headers(user_token)
        api = cls()
        cls._set_default_api(api)
        return api

    @classmethod
    def _set_default_headers(cls, user_token):
        cls.DEFAULT_HEADERS = {"Authorization": f"{user_token}", "Content-Type": "application/json"}

    @classmethod
    def _set_default_api(cls, api):
        cls.DEFAULT_API = api

    @classmethod
    def get_default_api(cls):
        return cls.DEFAULT_API

    def make_request(self, method, route, params=None, values=None):
        # handle rate limit
        if not params:
            params = {}
        url = self.API + route
        if method in ["GET", "DELETE"]:
            response = requests.request(
                url=url,
                method=method,
                headers=self.DEFAULT_HEADERS,
            )
        elif method == "POST":
            if values is None:
                response = requests.post(url, headers=self.DEFAULT_HEADERS)
            else:
                response = requests.post(url, data=json.dumps(values), headers=self.DEFAULT_HEADERS)
        elif method == "PUT":
            response = requests.put(url, data=json.dumps(values), headers=self.DEFAULT_HEADERS)
        else:
            raise ValueError("Invalid request method")
        try:
            body = response.json()
        except:
            return response
        self._update_rate_limits(response.headers)
        self._verify_response(response)
        return body

    def _verify_response(self, response):
        status_code = response.status_code
        if not 200 <= status_code < 300:
            message = response.json().get("err")
            raise requests.exceptions.RequestException(
                f"Request failed with status code {status_code}. Message: {message}"
            )
        return True

    def _update_rate_limits(self, headers):
        self.RATE_LIMIT_REMAINING = headers.get("X-RateLimit-Remaining")
        self.RATE_RESET = headers.get("X-RateLimit-Reset")
        return

    def _beauty_sleep(self, t):
        """
        Just a pretty way to countdown in the terminal
        t is an interger
        """
        for i in range(t, 0, -1):
            sys.stdout.write(str(i) + " ")
            sys.stdout.flush()
            time.sleep(1)
        print("")
        return

    def get_teams(self, fields=None):
        from clickup_python_sdk.clickupobjects.team import Team

        target_class = Team
        route = "team"
        method = "GET"
        response = self.make_request(method=method, route=route)
        result = []
        for teams in response["teams"]:
            result.append(Team.create_object(data=teams, target_class=target_class))
        return result

    def get_task(self, task_id=None, fields=None):
        if task_id is None:
            raise Exception("Must provide task id.")
        from clickup_python_sdk.clickupobjects.task import Task

        target_class = Task
        route = "task/" + task_id + "/?custom_task_ids=&team_id=&include_subtasks=true"
        method = "GET"
        response = self.make_request(method=method, route=route)
        return Task.create_object(data=response, target_class=target_class)
