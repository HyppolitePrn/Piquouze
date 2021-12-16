from liste import start
from Mac_or_wind import os
def start_with_os(os):
    if os == "linux":
        os = "mac"
    if os == "mac":
        from menu_nav_mac import menu_nav_mac
        menu_nav_mac(start())
    if os == "windows":
        from Menu_nav import menu_nav
        menu_nav(start())

start_with_os(os)