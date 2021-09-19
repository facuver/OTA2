import network, machine, gc

from ota_updater import OTAUpdater


sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)

sta_if.connect("Julio", "Misiones145")  # Connect to an AP
while not sta_if.isconnected():
    pass
print("Connected")

otaUpdater = OTAUpdater(
    "https://github.com/rdehuyss/micropython-ota-updater",
    main_dir="app",
    secrets_file="secrets.py",
)
hasUpdated = otaUpdater.install_update_if_available()
if hasUpdated:
    machine.reset()
else:
    del otaUpdater
    gc.collect()
