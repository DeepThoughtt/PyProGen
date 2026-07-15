import argparse
import sys

from src.singletons.localization import localization

class CustomParser(argparse.ArgumentParser):

    def __init__(self, prog, description):
        super().__init__(
            prog = prog, 
            description = description,
        )

    def error(self, message):
        if "unrecognized arguments" in message:
            unrecognized_arguments_msg = localization["unrecognizedArgumentsError"].format(cmd = message.split(":")[1].strip())
            print(f"{self.get_usage()}{unrecognized_arguments_msg}")
        
        else:
            print(message)

        sys.exit(2)

    def print_help(self, file = None):
        help_text = super().format_help()
        
        help_text = help_text\
            .replace("usage:", localization["usageHelpText"])\
            .replace("options:", localization["optionsHelpText"])\
            .replace("show this help message and exit", localization["showsHelpMessage"])
        
        print(help_text)
