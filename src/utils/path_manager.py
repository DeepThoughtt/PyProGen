from src.singletons.localization import localization
from src.utils.files import Files


class PathManager:

    def __init__(self, work_directory, app_name, use_workdir, verbose):
        if not use_workdir:
            work_directory = work_directory / app_name

        self.work_directory = work_directory
        self.actual_directory = work_directory
        self.verbose = verbose

    def cd(self, directory, is_python_module = False):
        if directory == "..":
            self.actual_directory = self.actual_directory.parent
            return
        
        self.actual_directory = self.actual_directory / directory
        self.actual_directory.mkdir(parents = True, exist_ok = True)

        if is_python_module:
            self.actual_directory.mkdir(parents = True, exist_ok = True)
            init_path = self.actual_directory / "__init__.py"
            self.print_file_info_if_verbose(init_path)
            open(init_path, "a").close()

    def reset(self):
        self.actual_directory = self.work_directory

    def print_file_info_if_verbose(self, info):
        if not self.verbose:
            return
        
        message = localization["generatingFile"].format(file = info)
        print(message)

    def create_json(self, content, filename):
        json_path = self.actual_directory / filename
        self.print_file_info_if_verbose(json_path)
        Files.write_json(content, json_path)

    def copy_python_template(self, template_path, new_filename):
        template = Files.load_template(template_path)
        settings_file = self.actual_directory / new_filename
        self.print_file_info_if_verbose(settings_file)
        Files.write_from_template(template, settings_file)

    def create_file_from_content(self, content, filename):
        file_path = self.actual_directory / filename
        self.print_file_info_if_verbose(file_path)
        Files.write_file(content, file_path)
