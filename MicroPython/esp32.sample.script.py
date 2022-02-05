import machine

led = machine.Pin(2, Pin.OUT)
led.value(1)


pin12 = machine.Pin(12, machine.Pin.OUT)
pin12.value(1)
pin13 = machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_UP)
print(pin13.value())


i2c = machine.I2C(scl=machine.Pin(21), sda=machine.Pin(22))
i2c.scan()
i2c.writeto(addr, b'1234')
i2c.readfrom(addr, 4)




print(1 + 2)
print(1 + 2)
print(1 + 2)
print(1 + 2)

led.value(0)