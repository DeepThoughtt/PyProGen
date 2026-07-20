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
            .generate_spec_file()\
            .generate_gitignore()\
            .generate_readme()

    def generate_main_file(self):
        self.path_manager.reset()
        self.path_manager.cd("src", True)
        self.path_manager.copy_python_template("cli/main/main.py", "main.py")

        return self
    
    def generate_spec_file(self):
        self.path_manager.reset()
        self.path_manager.cd(".windows")

        spec = Files.load_template("cli/misc/main-windows.spec")
        spec_template = string.Template(spec.read_text(encoding = "utf-8"))
        formatted_spec = spec_template.substitute(app_name = self.app_name)
        self.path_manager.create_file_from_content(formatted_spec, "main-windows.spec")

        return self
