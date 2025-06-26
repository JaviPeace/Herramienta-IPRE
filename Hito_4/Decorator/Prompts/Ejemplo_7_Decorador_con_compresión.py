class Logger:
    def log(self, message):
        print(f"LOG: {message}")

class LoggerDecorator(Logger):
    def __init__(self, logger):
        self._logger = logger

    def log(self, message):
        self._logger.log(message)

class TimestampDecorator(LoggerDecorator):
    def log(self, message):
        from datetime import datetime
        ts = datetime.now().isoformat()
        self._logger.log(f"{ts} - {message}")

# Uso
logger = Logger()
ts_logger = TimestampDecorator(logger)
ts_logger.log("Something happened")
