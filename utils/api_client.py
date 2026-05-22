import requests
from config.settings import BASE_URL, TIMEOUT

class APIClient:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({"Content-Type": "application/json"})

    def _build_url(self, path):
        return f"{BASE_URL}{path}"

    def get(self, path, params=None, **kwargs):
        kwargs.setdefault("timeout", TIMEOUT)
        return self.session.get(self._build_url(path), params=params, **kwargs)

    def post(self, path, json=None, **kwargs):
        kwargs.setdefault("timeout", TIMEOUT)
        return self.session.post(self._build_url(path), json=json, **kwargs)

    def put(self, path, json=None, **kwargs):
        kwargs.setdefault("timeout", TIMEOUT)
        return self.session.put(self._build_url(path), json=json, **kwargs)

    def patch(self, path, json=None, **kwargs):
        kwargs.setdefault("timeout", TIMEOUT)
        return self.session.patch(self._build_url(path), json=json, **kwargs)

    def delete(self, path, **kwargs):
        kwargs.setdefault("timeout", TIMEOUT)
        return self.session.delete(self._build_url(path), **kwargs)

    def close(self):
        self.session.close()