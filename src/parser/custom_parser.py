import argparse
import sys

from src.consts.project_types import ProjectTypes
from src.singletons.localization import localization

class CustomParser(argparse.ArgumentParser):

    def error(self, message):
        if "unrecognized arguments: --type" in message:
            valid_projects = ", ".join(ProjectTypes.to_list())
            invalid_project_msg = localization["invalidProjectTypeError"]
            usage_msg = localization["usage"].format(projects = "{" + valid_projects + "}")
            print(f"{usage_msg}\n{invalid_project_msg}")
        
        else:
            print(message)

        sys.exit(2)
