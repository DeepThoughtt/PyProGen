import traceback
import pygame
import sys

from src.singletons.localization import localization
from src.singletons.settings import settings
from src.singletons.assets import assets
from src.consts.scenes import Scenes
from src.consts.images import Images
from src.utils.files import Files
from src.scenes.main_menu_scene import MainMenuScene
from src.utils.settings_checker import SettingsChecker

def main():
    pygame.init()

    def goto(scene_name):
        nonlocal scene
        scene = scenes_dict[scene_name](display, goto)

    scenes_dict = {
        Scenes.MAIN_MENU: MainMenuScene,
    }

    # Fullscreen mode
    # display = pygame.display.set_mode((0, 0), pygame.NOFRAME)

    # Windowed mode
    display = pygame.display.set_mode((800, 600))
    
    SettingsChecker.fix_and_save(settings)

    localization.set_language(settings["language"])
    pygame.display.set_caption(settings["appName"])

    assets.load_assets({
        "images": {
            Images.ICON: Files.load_image(Images.ICON),
        },
        "sounds": {
            # Empty for now, might use some sounds later in development
        },
    })

    scene = MainMenuScene(display, goto)
    pygame.display.set_icon(assets.images[Images.ICON])
    
    while True:
        events = pygame.event.get()
        scene.handle_events(events)
        scene.draw()
        pygame.display.flip()
        

if __name__ == "__main__":
    try:
        main()
    except Exception:
        if settings["createCrashReports"]:
            Files.write_crash_report(traceback.format_exc())
            
        pygame.quit()
        sys.exit()
