class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Connecting to DB...")
            cls._instance = super().__new__(cls)
        return cls._instance

db1 = Database()
db2 = Database()
print(db1 is db2)
