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
