from src.consts.project_types import ProjectTypes
from src.generators.cli_generator import CliGenerator
from src.generators.pygame_generator import PygameGenerator
from src.generators.tkinter_generator import TkinterGenerator
from src.singletons.localization import localization
from src.singletons.settings import settings
from src.utils.validator import Validator

class AppBusiness:

    @staticmethod
    def handle_arguments(args):
        error_msg = Validator.validate_arguments(args)

        if error_msg != None:
            raise ValueError(error_msg)

        if args.version:
            AppBusiness.show_app_version()
            return
        
        AppBusiness.generate_project(args)
    
    @staticmethod
    def show_app_version():
        version = settings["version"]
        app_name = settings["appName"]
        print(f"{app_name} v{version}")

    @staticmethod
    def generate_project(args):
        generator_type = AppBusiness.get_project_type(args)

        if generator_type == None:
            raise ValueError(localization["unspecifiedOrInvalidProjectTypeError"])

        generator = generator_type(
            app_name = args.name,
            publisher = args.publisher,
            work_directory = args.dir,
            use_workdir = args.use_workdir,
            verbose_mode_enabled = args.verbose,
        )
        
        generator.generate()
        print(localization["generationCompleted"])

    @staticmethod
    def get_project_type(args):
        return {
            ProjectTypes.CLI: CliGenerator,
            ProjectTypes.TKINTER: TkinterGenerator,
            ProjectTypes.PYGAME: PygameGenerator,
        }.get(args.type)
