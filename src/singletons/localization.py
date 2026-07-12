import locale

from src.consts.languages import Languages
from src.utils.files import Files

class Localization:

    def set_language(self, language_code):
        self.localization = Files.read_localization(language_code)

    def set_language_from_locale(self):
        system_locale = locale.getlocale()

        if system_locale == None or len(system_locale[0]) < 2:
            self.localization = Files.read_localization(Languages.ENGLISH)
            return
        
        locale_initials = system_locale[0].lower()[:2]

        if Languages.is_valid(locale_initials):
            self.localization = Files.read_localization(locale_initials)
            return
        
        self.localization = Files.read_localization(Languages.ENGLISH)

    def __getitem__(self, label):
        return self.localization.get(label, "[MISSING LOCALIZATION]")

localization = Localization()
localization.set_language_from_locale()
