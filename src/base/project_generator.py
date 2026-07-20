import pathlib
import string

from src.consts.languages import Languages
from src.utils.files import Files
from src.utils.path_manager import PathManager

class ProjectGenerator:

    def __init__(
        self,
        app_name,
        publisher,
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
        self.publisher = publisher
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
        self.path_manager.reset()
        self.path_manager.cd("src", True)
        self.path_manager.cd("singletons", True)
        self.path_manager.copy_python_template("shared/singletons/assets.py", "assets.py")

        self.path_manager.reset()
        self.path_manager.cd("assets")
        self.path_manager.cd("icons")

        icon = Files.get_resource_path(f"assets/templates/shared/misc/icon.ico")
        self.path_manager.copy_file(str(icon), "icon.ico")

        self.path_manager.reset()
        self.path_manager.cd("src")
        self.path_manager.cd("consts")
        self.path_manager.copy_python_template("shared/consts/icons.py", "icons.py")
        
        return self

    def generate_localization_files(self):
        self.path_manager.reset()
        self.path_manager.cd("src", True)
        self.path_manager.cd("singletons", True)
        self.path_manager.copy_python_template("shared/singletons/localization.py", "localization.py")

        self.path_manager.cd("..")
        self.path_manager.cd("consts", True)
        self.path_manager.copy_python_template("shared/consts/languages.py", "languages.py")

        self.path_manager.reset()
        self.path_manager.cd("l10n")

        for language in Languages.to_set():
            self.path_manager.create_json(
                content = {"helloWorld": "Hello world!"},
                filename = f"{language[0:2]}.json",
            )

        return self

    def generate_utils(self):
        self.path_manager.reset()
        self.path_manager.cd("src", True)
        self.path_manager.cd("utils", True)

        utils_template = Files.load_template("shared/utils/files.py")
        template = string.Template(utils_template.read_text(encoding = "utf-8"))
        formatted = template.substitute(app_name = self.app_name)
        self.path_manager.create_file_from_content(formatted, "files.py")
        self.path_manager.copy_python_template("shared/utils/settings_checker.py", "settings_checker.py")

        return self

    def generate_readme(self):
        self.path_manager.reset()
        readme = Files.load_template("shared/misc/README.md")
        template = string.Template(readme.read_text(encoding = "utf-8"))
        formatted = template.substitute(app_name = self.app_name)
        self.path_manager.create_file_from_content(formatted, "README.md")

        return self

    def generate_gitignore(self):
        self.path_manager.reset()
        gitignore = Files.get_resource_path(f"assets/templates/shared/misc/.gitignore")
        self.path_manager.copy_file(gitignore, ".gitignore")
        
        return self

    def generate_installer(self):
        self.path_manager.reset()
        self.path_manager.cd(".windows")

        installer = Files.load_template("shared/misc/installer.iss")
        installer_template = string.Template(installer.read_text(encoding = "utf-8"))
        formatted_installer = installer_template.substitute(app_name = self.app_name, publisher = self.publisher)
        self.path_manager.create_file_from_content(formatted_installer, "installer.iss")

        return self
    
    def generate_spec_file(self):
        self.path_manager.reset()
        self.path_manager.cd(".windows")

        spec = Files.load_template("shared/misc/main-windows.spec")
        spec_template = string.Template(spec.read_text(encoding = "utf-8"))
        formatted_spec = spec_template.substitute(app_name = self.app_name)
        self.path_manager.create_file_from_content(formatted_spec, "main-windows.spec")

        return self

    def generate_vscode_setup(self):
        self.path_manager.reset()
        self.path_manager.cd(".vscode")

        launch = Files.get_resource_path(f"assets/templates/shared/misc/launch.json")
        self.path_manager.copy_file(launch, "launch.json")
        
        return self
    
    def generate_app_business(self):
        self.path_manager.reset()
        self.path_manager.cd("src", True)
        self.path_manager.cd("business", True)
        self.path_manager.copy_python_template("shared/business/app_business.py", "app_business.py")

        return self
