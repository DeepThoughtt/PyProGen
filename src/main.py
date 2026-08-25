from src.business.app_business import AppBusiness
from src.consts.project_types import ProjectTypes
from src.utils.custom_parser import CustomParser
from src.singletons.localization import localization

def main():
    parser = CustomParser(
        prog = "ppg",
        description = localization["pyProGenDescription"],
    )
    
    parser.add_argument(
        "-d",
        "--dir",
        help = localization["workingDirectory"],
    )

    group = parser.add_mutually_exclusive_group()

    group.add_argument(
        "-t",
        "--type",
        help = localization["projectType"].format(project_types = ", ".join(ProjectTypes.to_list())),
    )

    group.add_argument(
        "-ver",
        "--version",
        action = "store_true",
        help = localization["showVersion"],
    )

    parser.add_argument(
        "-n",
        "--name",
        help = localization["projectName"],
    )

    parser.add_argument(
        "-p",
        "--publisher",
        help = localization["projectPublisher"],
    )

    parser.add_argument(
        "-u",
        "--use-workdir",
        action = "store_true",
        help = localization["useWorkdirDescription"],
    )

    parser.add_argument(
        "-v",
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
