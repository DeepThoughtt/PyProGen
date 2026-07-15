from src.business.app_business import AppBusiness
from src.utils.custom_parser import CustomParser
from src.singletons.localization import localization

def main():
    parser = CustomParser(
        prog = "ppg",
        description = localization["pyprogenDescription"],
    )
    
    parser.add_argument(
        "--dir",
        help = localization["workingDirectory"],
    )

    group = parser.add_mutually_exclusive_group()

    group.add_argument(
        "--type",
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

    # We will make no checks on this parameter, if it isn't specified
    # we will not specify the publisher in the .iss file
    parser.add_argument(
        "--publisher",
        help = localization["publisher"],
    )

    parser.add_argument(
        "--verbose",
        action = "store_true",
        help = localization["enableVerboseOutput"],
    )

    AppBusiness.handle_arguments(parser.parse_args())

if __name__ == "__main__":
    try:
        main()
    except Exception as exception:
        print(exception)
