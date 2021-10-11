class Trainer:
    def __init__(self, username="", name="", current_designation=""):
        self._username = username
        self._name = name
        self._current_designation = current_designation

    def get_username(self):
        return self._username

    def get_name(self):
        return self._name

    def get_current_designation(self):
        return self._current_designation
