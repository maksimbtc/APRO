BASE_HEADER = {
    "accept": "application/json",
    "X-COUNTRY-CODE": "FR",
    "Content-Type": "application/json",
    "X-CSRF-TOKEN": None
}


class Header:

    def __init__(self, token=None):
        self.headers = BASE_HEADER
        if token is not None:
            self.headers["Authorization"] = token

    def get_header(self):
        return self.headers
