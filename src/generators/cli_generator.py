import string

from src.base.project_generator import ProjectGenerator
from src.utils.files import Files

class CliGenerator(ProjectGenerator):

    def __init__(
        self,
        app_name,
        publisher,
        work_directory,
        use_workdir,
        verbose_mode_enabled,
    ):
        
        super().__init__(
            app_name,
            publisher,
            work_directory,
            use_workdir,
            verbose_mode_enabled,
        )

    def generate(self):
        self.generate_asset_files()\
            .generate_localization_files()\
            .generate_settings_files()\
            .generate_installer()\
            .generate_vscode_setup()\
            .generate_app_business()\
            .generate_main_file()\
            .generate_utils()\
            .generate_github_build_workflow()\
            .generate_spec_file()\
            .generate_gitignore()\
            .generate_readme()

    def generate_main_file(self):
        self.path_manager.reset()
        self.path_manager.cd("src", True)
        self.path_manager.copy_python_template("cli/main/main.py", "main.py")

        return self

    def generate_github_build_workflow(self):
        self.path_manager.reset()
        self.path_manager.cd(".github")
        self.path_manager.cd("workflows")

        build_workflow = Files.load_template("cli/misc/build.yaml")
        build_workflow_template = string.Template(build_workflow.read_text(encoding = "utf-8"))
        formatted_build_workflow = build_workflow_template.substitute(app_name = self.app_name)
        self.path_manager.create_file_from_content(formatted_build_workflow, "build.yaml")

        return self

    def generate_settings_files(self):
        self.path_manager.reset()
        self.path_manager.cd("assets")
        self.path_manager.cd("configs")

        settings = Files.read_default_settings()
        settings["appName"] = self.app_name
        settings["version"] = "0.1.0"

        # We don't add the "language" setting and the "createCrashReports" setting
        # because the language is detected from the locale and cannot be changed
        # in a CLI application while the crash reports are written in the
        # console, not in a log file

        self.path_manager.create_json(settings, "default_appsettings.json")
        
        self.path_manager.reset()
        self.path_manager.cd("src", True)
        self.path_manager.cd("singletons", True)
        self.path_manager.copy_python_template("shared/singletons/settings.py", "settings.py")

        return self

    def generate_installer(self):
        self.path_manager.reset()
        self.path_manager.cd(".windows")

        installer = Files.load_template("cli/misc/installer.iss")
        installer_template = string.Template(installer.read_text(encoding = "utf-8"))
        formatted_installer = installer_template.substitute(app_name = self.app_name, publisher = self.publisher)
        self.path_manager.create_file_from_content(formatted_installer, "installer.iss")

        return self
