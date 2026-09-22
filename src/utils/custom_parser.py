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
        split_message = message.split(":")
        error_type = split_message[0]
        error_description = split_message[1]

        match error_type:
            case "unrecognized arguments":
                unrecognized_arguments_msg = localization["unrecognizedArgumentsError"].format(cmd = error_description.strip())
                usage_msg = self.format_usage().replace("usage:", localization["usageHelpText"])
                print(f"{usage_msg}{unrecognized_arguments_msg}")

            case "ambiguous option":
                params = error_description.split(" could match ")
                used = params[0].strip()
                possibilities = params[1].strip()
                ambiguous_option_msg = localization["ambiguousOptionError"].format(used = used, possibilities = possibilities)
                print(ambiguous_option_msg)

            case _:

                # This is a special case, the syntax of the error message is different than usual
                # Example: argument -t/--type: not allowed with argument -ver/--version
                if "not allowed with argument" in error_description:
                    first_argument = error_type.split()[1]
                    second_argument = error_description.split()[-1]
                    not_allowed_with_arg_msg = localization["argumentNotAllowedWithError"].format(first_argument = first_argument, second_argument = second_argument)
                    print(not_allowed_with_arg_msg)

                else:
                    print(message)

        sys.exit(2)

    def print_help(self, file = None):
        help_text = super().format_help()\
            .replace("usage:", localization["usageHelpText"])\
            .replace("options:", localization["optionsHelpText"])\
            .replace("show this help message and exit", localization["showHelpMessage"])
        
        print(help_text)
