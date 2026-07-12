class Icons:
    PYPROGEN = "pyprogen.ico"

    @staticmethod
    def to_set():
        return {
            Icons.PYPROGEN,
        }

    @staticmethod
    def is_valid(value):
        return value in Icons.to_set()
