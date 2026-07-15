from src.base.project_generator import ProjectGenerator

class CliGenerator(ProjectGenerator):

    def __init__(
        self,
        app_name,
        work_directory,
        use_workdir,
        verbose_mode_enabled,
    ):
        
        super().__init__(
            app_name,
            work_directory,
            use_workdir,
            verbose_mode_enabled,
        )

    def generate(self):
        pass

    def generate_main_file(self):
        pass
