import sqlite3
import atexit

from src.utils.files import Files

class Repository:

    def __init__(self):
        db_folder = Files.get_data_path() / "database"
        db_folder.mkdir(parents = True, exist_ok = True)
        db_filename = db_folder / "database.db"

        # The connect function automatically creates the database if it doesn't exist
        self.connection = sqlite3.connect(db_filename)
        self.cursor = self.connection.cursor()

        # Closes the connection automatically when the program is closed
        atexit.register(self.connection.close)

repository = Repository()
