def wich_os():
    os = input("   Utilisez vous windows ou mac?: ")
    while os.lower() != "windows" and os.lower() != "mac":
        os = input("   Utilisez vous windows ou mac?: ")
    return os
