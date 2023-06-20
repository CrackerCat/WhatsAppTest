import configparser


class ConfigManager():
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read("config.ini",encoding="utf-8")
        try:
            self.config.add_section("Main")
        except:
            pass


    def ReadConfig(self,key:str):
        try:
            return self.config.get("Main", key)
        except:
            pass
        return ""

    def WriteConfig(self,key:str,value:str):
        self.config.set("Main",key,value)
        self.config.write(open("config.ini", "w",encoding="utf-8"))


Instance = ConfigManager()
