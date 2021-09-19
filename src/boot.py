import network, machine
import senko

GITHUB_URL = "https://raw.githubusercontent.com/facuver/OTA2/test/src"
OTA = senko.Senko(url=GITHUB_URL, files=["boot.py", "main.py"])

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)

sta_if.connect("Julio", "Misiones145")  # Connect to an AP
while not sta_if.isconnected():
    pass
print("Connected")

if OTA.update():
    print("Updated to the latest version! Rebooting...")
    machine.reset()
