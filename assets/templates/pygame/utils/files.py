import datetime
import json
import os
import sys
import pathlib
import locale
import pygame

from src.consts.languages import Languages

class Files:

    @staticmethod
    def get_data_base_path():
        # Windows
        if os.name == "nt":
            return pathlib.Path(os.getenv("APPDATA"))
        # MacOS
        elif sys.platform == "darwin":
            return pathlib.Path.home() / "Library" / "Application Support"
        # Linux
        else:
            return pathlib.Path.home() / ".local" / "share"
        
    @staticmethod
    def get_data_path():
        app_data_dir = Files.get_data_base_path() / "$app_name"
        app_data_dir.mkdir(parents = True, exist_ok = True)
        return app_data_dir
    
    @staticmethod
    def get_resource_path(relative_path):
        # PyInstaller compatibility
        if hasattr(sys, "_MEIPASS"):
            return pathlib.Path(sys._MEIPASS) / relative_path
        
        return pathlib.Path(__file__).resolve().parent.parent.parent / relative_path

    @staticmethod
    def write_settings(settings):
        path = Files.get_data_path()
        path.mkdir(parents = True, exist_ok = True)
        file_path = path / "appsettings.json"

        with open(file_path, "w", encoding = "utf-8") as settings_file:
            json.dump(settings, settings_file, ensure_ascii = False, indent = 4)

    @staticmethod
    def write_crash_report(crash_report):
        path = Files.get_data_path() / "logs"
        path.mkdir(parents = True, exist_ok = True)
        now = datetime.datetime.now()
        file_path = path / f"crash_report_{now.strftime("%Y%m%d_%H%M%S")}.log"

        with open(file_path, "w", encoding = "utf-8") as crash_report_file:
            crash_report_file.write(crash_report)

    @staticmethod
    def read_settings():
        path = Files.get_data_path()
        path.mkdir(parents = True, exist_ok = True)
        file_path = path / "appsettings.json"

        # The file does not exist, so I copy the settings from the default settings file
        # Note: I also have to find the right localization to use for the system
        if  not file_path.is_file():
            default_settings = Files.read_default_settings()
            system_locale = locale.getlocale()

            if system_locale == None or len(system_locale[0]) < 2:
                default_settings["language"] = Languages.ENGLISH
            
            else:
                locale_initials = system_locale[0].lower()[:2]

                if Languages.is_valid(locale_initials):
                    default_settings["language"] = locale_initials
                else:
                    default_settings["language"] = Languages.ENGLISH

            with open(file_path, "w", encoding = "utf-8") as settings_file:
                json.dump(default_settings, settings_file, ensure_ascii = False, indent = 4)
                return default_settings

        with open(file_path, "r", encoding = "utf-8") as settings_file:
            return json.load(settings_file)
        
    @staticmethod
    def read_default_settings():
        default_settings_path = Files.get_resource_path("assets/configs/default_appsettings.json")

        with open(default_settings_path, "r", encoding = "utf-8") as settings_file:
            return json.load(settings_file)
        
    @staticmethod
    def read_localization(language_code):
        path = Files.get_resource_path(f"l10n/{language_code}.json")

        with open(path, "r") as localization:
            return json.load(localization)
        
    @staticmethod
    def load_icon(icon_name):
        return Files.get_resource_path(f"assets/icons/{icon_name}")
    
    @staticmethod
    def write_json(json_content, file_path):
        with open(file_path, "w", encoding = "utf-8") as json_file:
                json.dump(json_content, json_file, ensure_ascii = False, indent = 4)
    
    @staticmethod
    def write_file(file_content, file_path):
        with open(file_path, "w",encoding = "utf-8") as file:
            file.write(file_content)

    @staticmethod
    def load_image(image_name, handle_transparency = True):
        path = Files.get_resource_path(f"assets/images/{image_name}")

        if handle_transparency:
            return pygame.image.load(path).convert_alpha()
        else:
            return pygame.image.load(path).convert()
    
    @staticmethod
    def get_font(font_name, font_size):
        path = Files.get_resource_path(f"assets/fonts/{font_name}")

        try:
            return pygame.font.Font(str(path), font_size)
        except FileNotFoundError:
            return pygame.font.Font(None, font_size)

    @staticmethod
    def change_image_color(image, new_image_color):
        for x in range(image.get_width()):
            for y in range(image.get_height()):
                pixel = image.get_at((x, y))

                if pixel.a > 0:
                    color = (new_image_color[0], new_image_color[1], new_image_color[2], pixel.a)
                    image.set_at((x, y), color)