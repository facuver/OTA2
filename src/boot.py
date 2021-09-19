import network, machine

from ota_updater import OTAUpdater


sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)

sta_if.connect("Julio", "Misiones145")  # Connect to an AP
while not sta_if.isconnected():
    pass
print("Connected")

otaUpdater = OTAUpdater(
    "https://github.com/facuver/OTA2",
    github_src_dir="src",
    main_dir="",
    secrets_file="secrets.py",
)
otaUpdater.install_update_if_available()
del otaUpdater
