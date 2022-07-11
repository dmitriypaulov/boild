import json
import asyncio
from boild.blocks import i18nBlock, CommandBlock
from boild.blocks import ConfigBlock, SceneBlock
from aiogram import Bot, Dispatcher


class Schema():
    def __init__(self, path, raw):

        self.bot = None
        self.dp = None

        self.path = path
        self.raw = raw
        self.blocks = []
        self.handlers = []
        self.scenes_registry = {}
        self.i18n = {}
        self.process_raw()

    def extend_commands(self, block):
        handler = block.get_handler(self)
        self.handlers.append(handler)

    def extend_scenes(self, block):
        self.scenes_registry[block.name] = block

    def extend_i18n_terms(self, block):
        terms = block.get()
        for key, value in terms.items():
            if key not in self.i18n:
                self.i18n[key] = {}
            self.i18n[key].update(value)

    def process_raw(self):
        for obj in self.raw:
            _type = obj["type"]
            block = False

            if _type == "I18nBlock":
                block = i18nBlock(
                    obj["path"],
                    obj["language"],
                    obj["language_verbal"])
                self.extend_i18n_terms(block)

            elif _type == "ConfigBlock":
                block = ConfigBlock(
                    obj["params"])
                if "token" in block.params:
                    token = block.params["token"]
                    self.bot = Bot(token, parse_mode="HTML")
                    self.dp = Dispatcher(self.bot)

            elif _type == "CommandBlock":
                block = CommandBlock(
                    obj["command"],
                    obj["targetScene"])
                self.extend_commands(block)
                self.dp.register_message_handler(
                    block.get_handler(self),
                    commands=[block.command])

            elif _type == "SceneBlock":
                block = SceneBlock(
                    self,
                    obj["name"],
                    obj["text"],
                    obj.get("buttons", []),
                    obj.get("input", {}))
                self.extend_scenes(block)

            if block:
                self.blocks.append(block)

    def run(self):
        asyncio.run(self.dp.start_polling())

def read_schema(path):
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
        if data:
            return Schema(path, data)
