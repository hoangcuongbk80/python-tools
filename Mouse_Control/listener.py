import uinput

device = uinput.Device([
        uinput.BTN_LEFT,
        uinput.BTN_RIGHT,
        uinput.REL_X,
        uinput.REL_Y,
        ])

for i in range(20):
    device.emit(uinput.REL_X, 5)
    time.sleep(1)
    device.emit(uinput.REL_Y, 5)
    device.emit(uinput.REL_X, 45)
    device.emit(uinput.REL_Y, 45)
