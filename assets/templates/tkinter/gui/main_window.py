import tkinter

from src.consts.icons import Icons
from src.singletons.assets import assets
from src.singletons.settings import settings

class MainWindow(tkinter.Tk):

    def __init__(self):
        super().__init__()
        self.title(settings["appName"])
        self.iconbitmap(assets.icons[Icons.ICON])
        self.minsize(700, 200)
        self.geometry("")
