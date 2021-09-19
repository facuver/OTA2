import machine, utime

p = machine.Pin(2,machine.Pin.OUT)
while True:
    p.on()
    utime.sleep(1)
    p.off()
    utime.sleep(1)
