import network, machine
import senko

OTA = senko.Senko(
    user="facuver",  # Required
    repo="OTA",  # Required
    branch="master",  # Optional: Defaults to "master"
    files=["boot.py", "main.py"],
)

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)

sta_if.connect("Julio", "Misiones145")  # Connect to an AP
while not sta_if.isconnected():
    pass
print("Connected")

if OTA.update():
    print("Updated to the latest version! Rebooting...")
    machine.reset()
