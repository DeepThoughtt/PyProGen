from src.singletons.settings import settings

class AppBusiness:

    @staticmethod
    def handle_arguments(args):
        AppBusiness.check_arguments(args)

        if args.version:
            AppBusiness.show_app_version()
            return

        if args.type != None:
            AppBusiness.generate_project(args.type, args.name, args.verbose)
            return

        if args.json != None:
            AppBusiness.generate_project_from_json(args.json, args.verbose)
            return
        
        AppBusiness.generate_sample_json_file()

    @staticmethod
    def check_arguments(args):
        # Should raise an exception if something is wrong
        pass
    
    @staticmethod
    def show_app_version():
        version = settings["version"]
        app_name = settings["appName"]
        print(f"{app_name} v{version}")

    @staticmethod
    def generate_project(project_type, project_name, verbose_mode_enabled):
        pass
    
    @staticmethod
    def generate_project_from_json(json_file, verbose_mode_enabled):
        pass

    @staticmethod
    def generate_sample_json_file():
        pass
