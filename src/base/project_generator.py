import pathlib
import os
import string

from src.consts.languages import Languages
from src.singletons.localization import localization
from src.utils.files import Files
from src.utils.path_manager import PathManager

class ProjectGenerator:

    def __init__(
        self,
        app_name,
        work_directory,
        use_workdir,
        verbose_mode_enabled,
    ):
        
        self.path_manager = PathManager(
            work_directory = pathlib.Path(work_directory), 
            app_name = app_name, 
            use_workdir = use_workdir,
            verbose = verbose_mode_enabled,
        )

        self.verbose = verbose_mode_enabled
        self.app_name = app_name
    
    def generate_repository(self):
        self.path_manager.reset()
        self.path_manager.cd("src", True)
        self.path_manager.cd("singletons", True)
        self.path_manager.copy_python_template("shared/singletons/repository.py", "repository.py")
        return self
    
    def generate_settings_files(self):
        self.path_manager.reset()
        self.path_manager.cd("assets")
        self.path_manager.cd("configs")

        settings = Files.read_default_settings()
        settings["version"] = "0.1.0"
        settings["appName"] = self.app_name
        settings["language"] = Languages.ENGLISH
        settings["createCrashReports"] = True
        self.path_manager.create_json(settings, "default_settings.json")
        
        self.path_manager.reset()
        self.path_manager.cd("src", True)
        self.path_manager.cd("singletons", True)

        self.path_manager.copy_python_template("shared/singletons/settings.py", "settings.py")
        return self

    def generate_asset_files(self):
        return self

    def generate_localization_files(self):
        return self

    def generate_utils(self):
        self.path_manager.reset()
        self.path_manager.cd("src", True)
        self.path_manager.cd("utils", True)

        utils_template = Files.load_template("shared/utils/files.py")
        template = string.Template(utils_template.read_text(encoding = "utf-8"))
        formatted = template.substitute(app_name = self.app_name)
        self.path_manager.create_file_from_content(formatted, "files.py")

        return self

    def generate_readme(self):
        return self

    def generate_gitignore(self):
        return self

    def generate_spec_and_installer(self):
        return self

    def generate_vscode_setup(self):
        return self
    
    def generate_app_business(self):
        return self
