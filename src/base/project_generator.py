import pathlib

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
        
        # If the work directory doesn't exist it will be created when trying to write a file
        if not use_workdir:
            self.work_directory = self.work_directory / app_name

    def print_info_if_verbose(self, info):
        if not self.verbose:
            return
        
        print(info)
    
    def generate_repository(self):
        # https://www.reddit.com/r/Python/comments/1kch7hf/template_strings_in_python_314_an_useful_new/
        # Use template strings for this (import string and then string.Template)
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
    
    def generate_settings_files(self):
        return self
