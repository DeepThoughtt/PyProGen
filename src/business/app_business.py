import pathlib

from src.consts.project_types import ProjectTypes
from src.singletons.localization import localization
from src.singletons.settings import settings

class AppBusiness:

    @staticmethod
    def handle_arguments(args):
        error_msg = AppBusiness.check_arguments(args)

        if error_msg != None:
            raise ValueError(error_msg)

        if args.version:
            AppBusiness.show_app_version()
            return
        
        AppBusiness.generate_project(args.type, args.name, args.verbose)

    @staticmethod
    def check_arguments(args):
        if args.version and args.type != None:
            return localization["tooManyArgumentsError"]
        
        if args.version:
            if args.dir != None or args.type != None or args.name != None or args.verbose:
                return localization["tooManyArgumentsError"]
            
            # No need to check further, we print the program version
            return
        
        # Now we can handle the generation parameters alone
        if args.dir == None:
            return localization["unspecifiedProjectdirectoryError"]

        project_directory = pathlib.Path(args.dir)

        if not project_directory.exists():
            return localization["directoryDoesNotExistError"].format(dir = args.dir)

        if not project_directory.is_dir():
            return localization["notADirectoryError"].format(dir = args.dir)
        
        if args.type == None or not ProjectTypes.is_valid(args.type):
            return localization["unspecifiedOrInvalidProjectTypeError"]
        
        if args.name == None:
            return localization["projectNameNotSpecified"]
    
    @staticmethod
    def show_app_version():
        version = settings["version"]
        app_name = settings["appName"]
        print(f"{app_name} v{version}")

    @staticmethod
    def generate_project(project_type, project_name, verbose_mode_enabled):
        pass
