from liste import start
from Mac_or_wind import os
def start_with_os(os):
    if os.lower() == "linux":
        os = "mac"
    if os.lower() == "mac":
        from menu_nav_mac import menu_nav_mac
        menu_nav_mac(start())
    if os.lower() == "windows":
        from Menu_nav import menu_nav
        menu_nav(start())

start_with_os(os)