class Images:
    ICON = "icon.png"

    @staticmethod
    def to_set():
        return {
            Images.ICON,
        }
    
    @staticmethod
    def is_valid(value):
        return value in Images.to_set()
