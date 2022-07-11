class InputBlock():
    def __init__(self, field=None, fields=None, code=None):
        self.fields = fields or [field]
        self.code = code
        if not any((field, fields)):
            raise ValueError(
                "InputBlock object needs one of parameters: field or fields.")
