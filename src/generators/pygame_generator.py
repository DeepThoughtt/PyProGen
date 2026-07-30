import string

from src.base.project_generator import ProjectGenerator
from src.utils.files import Files

class PygameGenerator(ProjectGenerator):

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
            .generate_pygame_scenes()\
            .generate_pygame_consts()\
            .generate_vscode_setup()\
            .generate_repository()\
            .generate_main_file()\
            .generate_utils()\
            .generate_github_build_workflow()\
            .generate_requirements_file()\
            .generate_spec_file()\
            .generate_gitignore()\
            .generate_readme()

    def generate_main_file(self):
        self.path_manager.reset()
        self.path_manager.cd("src", True)
        self.path_manager.copy_python_template("pygame/main/main.py", "main.py")

        return self
    
    def generate_pygame_scenes(self):
        self.path_manager.reset()
        self.path_manager.cd("src", True)
        self.path_manager.cd("scenes", True)
        self.path_manager.copy_python_template("pygame/scenes/main_menu_scene.py", "main_menu_scene.py")

        return self

    def generate_pygame_consts(self):
        self.path_manager.reset()
        self.path_manager.cd("src", True)
        self.path_manager.cd("consts", True)
        self.path_manager.copy_python_template("pygame/consts/scenes.py", "scenes.py")
        self.path_manager.copy_python_template("pygame/consts/colors.py", "colors.py")
        
        return self

    def generate_requirements_file(self):
        self.path_manager.reset()
        requirements = Files.get_resource_path(f"assets/templates/pygame/misc/requirements.txt")
        self.path_manager.copy_file(requirements, "requirements.txt")

        return self

    def generate_asset_files(self):
        self.path_manager.reset()
        self.path_manager.cd("src", True)
        self.path_manager.cd("singletons", True)
        self.path_manager.copy_python_template("pygame/singletons/assets.py", "assets.py")

        self.path_manager.reset()
        self.path_manager.cd("assets")
        self.path_manager.cd("images")

        icon_image = Files.get_resource_path(f"assets/templates/pygame/misc/icon.png")
        self.path_manager.copy_file(icon_image, "icon.png")

        self.path_manager.cd("..")
        self.path_manager.cd("icons")
        icon = Files.get_resource_path(f"assets/templates/shared/misc/icon.ico")
        self.path_manager.copy_file(icon, "icon.ico")

        self.path_manager.reset()
        self.path_manager.cd("src", True)
        self.path_manager.cd("consts", True)
        self.path_manager.copy_python_template("pygame/consts/images.py", "images.py")
        self.path_manager.copy_python_template("shared/consts/icons.py", "icons.py")

        return self

    def generate_utils(self):
        self.path_manager.reset()
        self.path_manager.cd("src", True)
        self.path_manager.cd("utils", True)

        utils_template = Files.load_template("pygame/utils/files.py")
        template = string.Template(utils_template.read_text(encoding = "utf-8"))
        formatted = template.substitute(app_name = self.app_name)
        self.path_manager.create_file_from_content(formatted, "files.py")
        self.path_manager.copy_python_template("shared/utils/settings_checker.py", "settings_checker.py")

        return self

    def generate_github_build_workflow(self):
        self.path_manager.reset()
        self.path_manager.cd(".github")
        self.path_manager.cd("workflows")

        build_workflow = Files.load_template("pygame/misc/build.yaml")
        build_workflow_template = string.Template(build_workflow.read_text(encoding = "utf-8"))
        formatted_build_workflow = build_workflow_template.substitute(app_name = self.app_name)
        self.path_manager.create_file_from_content(formatted_build_workflow, "build.yaml")

        return self
