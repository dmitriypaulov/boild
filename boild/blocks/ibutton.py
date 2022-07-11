class IButton():
    def __init__(self, text, data=None, targetScene=None):
        self.text = text
        self.data = data
        self.targetScene = targetScene
        if not any((data, targetScene)):
            raise ValueError(
                "iButton object needs one of parameters: data or targetScene.")
