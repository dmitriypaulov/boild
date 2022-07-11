class ConditionBlock():
    def __init__(self, targetScene, message=None, callback=None, code=None, needsConfirmation=False):
        self.targetScene = targetScene
        self.message = message
        self.callback = callback
        self.code = code
        self.needsConfirmation = needsConfirmation
