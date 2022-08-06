try:
    import configparser
except ImportError:
    import ConfigParser as configparser
import os
import platform

global CFG_UWP_CHECK
if platform.system() == "Windows" and platform.release() == 10:
    CFG_UWP_CHECK = True
else:
    CFG_UWP_CHECK = False

def createConfig():
    config = configparser.ConfigParser()
    config.add_section("Settings")
    config.set("Settings", "start", "true")
    config.set("Settings", "theme", "light")
    config.set("Settings", "folder", "%%APPDATA%%\.minecraft")
    with open("main.ini", "w") as config_file:
        config.write(config_file)
    config = configparser.ConfigParser()
    config.add_section("UWP")
    config.set("UWP", "name", "W10E Launcher")
    config.set("UWP", "launch", "explorer.exe shell:appsFolder\Microsoft.MinecraftUWP_8wekyb3d8bbwe")
    config.add_section("Classic")
    config.set("Classic", "name", "Classic Launcher")
    config.set("Classic", "launch", "C:\Program Files (x86)\Minecraft Launcher\MinecraftLauncher.exe")
    with open("lauch-profile.ini", "w") as config_file:
        config.write(config_file)
    config = configparser.ConfigParser()
    config.add_section("1")
    config.set("1", "active", "true")
    config.set("1", "name", "Mine Pack")
    config.set("1", "key_folder", "awdawd32e3")
    with open("mods-profile.ini", "w") as config_file:
        config.write(config_file)

if __name__ == "__main__":
    createConfig()