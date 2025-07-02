class Singleton:
    _instance = None
    _config = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @classmethod
    def configure(cls, **kwargs):
        cls._config.update(kwargs)

Singleton.configure(api_key="123")
print(Singleton._config)
