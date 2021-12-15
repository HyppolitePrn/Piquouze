# from liste import start
def wich_os():
    os = input("   Utilisez vous Windows, Mac ou Linux?: ")
    while os.lower() != "windows" and os.lower() != "mac" and os.lower() != "linux":
        os = input("   Utilisez vous Windows, Mac ou Linux?: ")
    return os


os = wich_os()
# def start_with_os(os):
#     if os == "linux":
#         os = "mac"
#     if os == "mac":
#         from menu_nav_mac import menu_nav_mac
#         menu_nav_mac(start())
#     if os == "windows":
#         from Menu_nav import menu_nav
#         menu_nav(start())