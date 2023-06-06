class NotInvertibleError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class IncompatibleFieldError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)