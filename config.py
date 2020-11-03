import configparser
import os


class Config():
    def __init__(self):
        app_name = "FireDownloader"
        settings_file = "settings.conf"
        config_folder = os.path.join(os.path.expanduser("~"), '.config', app_name)
        self.full_config_file_path = os.path.join(config_folder, settings_file)
        self.config = configparser.ConfigParser()

        if not os.path.exists(self.full_config_file_path) or\
                os.stat(self.full_config_file_path).st_size == 0:
            os.makedirs(config_folder, exist_ok=True)
            self.config['DEFAULT'] = {"path": os.path.expanduser('~/Downloads/'), "theme": "ElegantDark"}
            with open(self.full_config_file_path, 'w') as configfile:
                self.config.write(configfile)

    def setSetting(self,name,setting,value):
        self.config.set(name, setting, value)
        with open(self.full_config_file_path, 'w') as configfile:
            self.config.write(configfile)

    def getSetting(self,name,setting):
        self.config.read(self.full_config_file_path)
        return self.config[name][setting]
