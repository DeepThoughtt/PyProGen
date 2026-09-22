import pathlib

from src.consts.project_types import ProjectTypes
from src.singletons.localization import localization

class Validator:

    @staticmethod
    def validate_arguments(args):
        if args.version and args.type != None:
            return localization["tooManyArgumentsError"]
        
        if args.version:
            if args.dir != None or args.type != None or args.name != None or args.verbose or args.publisher != None:
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
            return localization["unspecifiedProjectNameError"]
        
        if args.publisher == None:
            return localization["unspecifiedPublisherError"]
