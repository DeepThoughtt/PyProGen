import argparse
import sys

from src.singletons.localization import localization

class CustomParser(argparse.ArgumentParser):

    def __init__(self, prog, description):
        super().__init__(prog = prog, description = description)

    def error(self, message):
        if "unrecognized arguments" in message:
            cmd_msg = message.split(":")[1].strip()
            unrecognized_arguments_msg = localization["unrecognizedArgumentsError"].format(cmd = cmd_msg)
            print(f"{self.get_usage()}{unrecognized_arguments_msg}")
        
        else:
            print(message)

        sys.exit(2)

    def get_usage(self):
        usage_format = self.format_usage().replace("usage: ", "")
        return localization["usage"].format(formatted = usage_format)
