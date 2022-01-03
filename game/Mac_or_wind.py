def wich_os():
    os = input("   Utilisez vous Windows, Mac ou Linux?: ")
    while os.lower() != "windows" and os.lower() != "mac" and os.lower() != "linux":
        os = input("   Utilisez vous Windows, Mac ou Linux?: ")
    return os


os = wich_os()