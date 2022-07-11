from traceback import print_exc


class SceneBlock():
    def __init__(self, schema, name, text, buttons=None, input=None):
        self.name = name
        self.text = text
        self.schema = schema
        self.buttons = buttons or []
        self.input = input or []

    async def render(self, user_id):
        bot = self.schema.bot
        try:
            await bot.send_message(user_id, self.text)
        except Exception:
            print_exc()
