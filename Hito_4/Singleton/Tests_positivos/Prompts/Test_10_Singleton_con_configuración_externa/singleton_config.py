import json

class Singleton:
    _instance = None

    def __new__(cls, config_path=None):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            if config_path:
                with open(config_path) as f:
                    cls._instance.config = json.load(f)
        return cls._instance
