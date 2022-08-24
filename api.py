import requests, time, sys, json
from config import API, VERSION


class ClickupClient(object):
    API = API
    SDK_VERSION = VERSION

    def __init__(self) -> None:
        pass

    @classmethod
    def init(cls, user_token=None):
        assert user_token != None, "Must provide user token"
        cls.set_default_headers(user_token)
        api = cls()
        cls.set_default_api(api)
        return api

    @classmethod
    def set_default_headers(cls, user_token):
        cls.DEFAULT_HEADERS = {"Authorization": f"{user_token}", "Content-Type": "application/json"}

    @classmethod
    def set_default_api(cls, api):
        cls.DEFAULT_API = api

    @classmethod
    def get_default_api(cls):
        return cls.DEFAULT_API

    def get(self, route, params=None):
        # Plan on creating a type checker and params verify
        if not params:
            params = {}
        url = self.API + route
        response = requests.get(url, headers=self.DEFAULT_HEADERS)
        body = json.loads(response.text)
        if self.rate_limited(body):
            self.beauty_sleep(60)
            return requests.get(url, headers=self.DEFAULT_HEADERS)
        self.verify_response(body)
        return body

    def post(self, route, values):
        url = self.API + route
        response = requests.post(url, data=json.dumps(values), headers=self.DEFAULT_HEADERS)
        body = json.loads(response.text)
        if self.rate_limited(body):
            self.beauty_sleep(60)
            return requests.post(url, data=json.dumps(values), headers=self.DEFAULT_HEADERS)
        self.verify_response(body)
        return body

    def put(self, route, values):
        url = self.API + route
        response = requests.put(url, data=json.dumps(values), headers=self.DEFAULT_HEADERS)
        body = response.text
        if self.rate_limited(body):
            self.beauty_sleep(60)
            return requests.put(url, data=json.dumps(values), headers=self.DEFAULT_HEADERS)
        self.verify_response(body)
        return body

    def rate_limited(self, response):
        if "err" in response.keys() and response["err"] == "Rate limit reached":
            print("Rate limit reached. Pausing for a minute.")
            return True
        else:
            return False

    def verify_response(self, response):
        if "err" in response.keys() and response["err"] != "Rate limit reached":
            raise ValueError(response["err"])
        return True

    def beauty_sleep(t):
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
        from clickupobjects.team import Team

        target_class = Team
        route = "team"
        query = self.get(route=route)

        result = []
        for teams in query["teams"]:
            result.append(Team.create_object(data=teams, target_class=target_class))
        return result
