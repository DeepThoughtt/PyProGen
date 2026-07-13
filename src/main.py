from src.business.app_business import AppBusiness
from src.consts.project_types import ProjectTypes
from src.parser.custom_parser import CustomParser
from src.singletons.localization import localization

def main():
    parser = CustomParser(
        prog = "ppg",
        description = localization["pyprogenDescription"],
    )
    
    parser.add_argument(
        "dir",
        nargs = "?",
        help = localization["workingDirectory"],
    )

    group = parser.add_mutually_exclusive_group()

    group.add_argument(
        "--type",
        choices = ProjectTypes.to_list(),
        help = localization["projectType"],
    )

    group.add_argument(
        "--version",
        action = "store_true",
        help = localization["showVersion"],
    )

    parser.add_argument(
        "--name",
        help = localization["projectName"],
    )

    parser.add_argument(
        "--verbose",
        action = "store_true",
        help = localization["enableVerboseOutput"],
    )

    AppBusiness.handle_arguments(parser.parse_args())
    print(localization["helloWorld"])

if __name__ == "__main__":
    try:
        main()
    except Exception as exception:
        print(exception)
