class IButtonSmart():
    def __init__(self, _for, _as, text, data, columns=1):
        self._for = _for
        self._as = _as
        self.text = text
        self.data = data
        self.columns = columns
