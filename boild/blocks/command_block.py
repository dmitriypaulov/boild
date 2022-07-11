class CommandBlock():
    def __init__(self, command, targetScene):
        self.command = command
        self.targetScene = targetScene

    def get_handler(self, schema):
        async def handler(m):
            user_id = m.chat.id
            if self.targetScene:
                return await schema.scenes_registry[
                    self.targetScene].render(user_id)
        return handler
