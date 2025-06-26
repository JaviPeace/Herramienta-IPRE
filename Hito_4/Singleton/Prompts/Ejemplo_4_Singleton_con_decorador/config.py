from singleton_decorator import singleton

@singleton
class Config:
    def __init__(self):
        self.settings = {"debug": True}
