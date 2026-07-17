import pathlib
import os

from src.consts.languages import Languages
from src.singletons.localization import localization
from src.utils.files import Files

class ProjectGenerator:

    def __init__(
        self,
        app_name,
        work_directory,
        use_workdir,
        verbose_mode_enabled,
    ):
        
        self.verbose = verbose_mode_enabled
        self.work_directory = pathlib.Path(work_directory)
        self.app_name = app_name
        
        # If the work directory doesn't exist it will be created when trying to write a file
        if not use_workdir:
            self.work_directory = self.work_directory / app_name

    def print_file_info_if_verbose(self, info):
        if not self.verbose:
            return
        
        message = localization["generatingFile"].format(file = info)
        print(message)
    
    def generate_repository(self):
        # https://www.reddit.com/r/Python/comments/1kch7hf/template_strings_in_python_314_an_useful_new/
        # Use template strings for this (import string and then string.Template)
        return self
    
    def generate_settings_files(self):
        settings_path = self.work_directory / "assets" / "configs"
        settings_path.mkdir(parents = True, exist_ok = True)
        settings = Files.read_default_settings()

        settings["version"] = "0.1.0"
        settings["appName"] = self.app_name
        settings["language"] = Languages.ENGLISH
        settings["createCrashReports"] = True

        appsettings_file = settings_path / "default_appsettings.json"
        self.print_file_info_if_verbose(appsettings_file)
        Files.write_json(settings, appsettings_file)
        settings_template_path = Files.load_template("shared/settings.py")

        src_path = self.work_directory / "src"
        self.create_python_directory(src_path)

        singletons_path = src_path / "singletons"
        self.create_python_directory(singletons_path)

        settings_file = singletons_path / "settings.py"
        self.print_file_info_if_verbose(settings_file)
        Files.write_from_template(settings_template_path, settings_file)

        return self

    def generate_asset_files(self):
        return self

    def generate_localization_files(self):
        return self

    def generate_utils(self):
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
    
    def create_python_directory(self, path):
        directory_exists = os.path.isdir(str(path))
        path.mkdir(parents = True, exist_ok = True)

        # If the directory has just been created we have to add the __init__.py file
        init_path = path / "__init__.py"

        if not directory_exists:
            self.print_file_info_if_verbose(init_path)
            open(init_path, "a").close()
