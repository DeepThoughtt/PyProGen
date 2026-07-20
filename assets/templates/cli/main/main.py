from src.business.app_business import AppBusiness

def main():
    AppBusiness.hello_world()

if __name__ == "__main__":
    try:
        main()
    except Exception as exception:
        print(exception)
