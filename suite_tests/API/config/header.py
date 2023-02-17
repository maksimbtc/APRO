class Header:

    def __init__(self, token=None):
        if token is None:
            self.headers = {
                "accept": "application/json",
                "X-COUNTRY-CODE": "FR",
                "Content-Type": "application/json",
                "X-CSRF-TOKEN": None
            }
        else:
            self.headers = {
                "accept": "application/json",
                "X-COUNTRY-CODE": "FR",
                "Content-Type": "application/json",
                "X-CSRF-TOKEN": None
            }

    def get_header(self):
        return self.headers
