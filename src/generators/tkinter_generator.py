from src.base.project_generator import ProjectGenerator

class TkinterGenerator(ProjectGenerator):

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
            .generate_repository()\
            .generate_main_file()\
            .generate_main_window()\
            .generate_utils()\
            .generate_spec_file()\
            .generate_gitignore()\
            .generate_readme()

    def generate_main_file(self):
        self.path_manager.reset()
        self.path_manager.cd("src", True)
        self.path_manager.copy_python_template("tkinter/main/main.py", "main.py")

        return self
    
    def generate_main_window(self):
        self.path_manager.reset()
        self.path_manager.cd("src", True)
        self.path_manager.cd("gui", True)
        self.path_manager.copy_python_template("tkinter/gui/main_window.py", "main_window.py")

        return self
