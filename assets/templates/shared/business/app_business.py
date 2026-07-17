from src.singletons.localization import localization

class AppBusiness:

    @staticmethod
    def hello_world():
        print(localization["helloWorld"])
