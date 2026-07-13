class ProjectTypes:
    CLI = "cli"
    PYGAME = "pygame"
    TKINTER = "tkinter"

    @staticmethod
    def to_list():
        return [
            ProjectTypes.CLI,
            ProjectTypes.PYGAME,
            ProjectTypes.TKINTER,
        ]
    
    @staticmethod
    def to_set():
        return {
            ProjectTypes.CLI,
            ProjectTypes.PYGAME,
            ProjectTypes.TKINTER,
        }

    @staticmethod
    def is_valid(value):
        return value in ProjectTypes.to_set()
