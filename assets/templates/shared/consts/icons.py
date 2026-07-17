class Icons:
    ICON = "icon.ico"

    @staticmethod
    def to_set():
        return {
            Icons.ICON,
        }

    @staticmethod
    def is_valid(value):
        return value in Icons.to_set()
