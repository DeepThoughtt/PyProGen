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
            .generate_spec_file()\
            .generate_vscode_setup()\
            .generate_app_business()\
            .generate_repository()\
            .generate_main_file()\
            .generate_utils()\
            .generate_gitignore()\
            .generate_readme()

    def generate_main_file(self):
        return self
