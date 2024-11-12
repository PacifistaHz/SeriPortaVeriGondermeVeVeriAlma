def seriPortOkumayıBaslat():
    import serial

    serialBaglanti = serial.Serial()

    serialBaglanti.port = 'COM5'
    serialBaglanti.baudrate = 9600
    serialBaglanti.parity = serial.PARITY_NONE
    serialBaglanti.stopbits = serial.STOPBITS_ONE
    serialBaglanti.bytesize = serial.EIGHTBITS
    serialBaglanti.timeout = 0

    if not serialBaglanti.isOpen():
        serialBaglanti.open()

    while True:
        print(serialBaglanti.readline())

    serialBaglanti.close()

def seriPortVeriGonder(veri):
    import serial

    serialBaglanti = serial.Serial()

    serialBaglanti.port = "COM5"
    serialBaglanti.baudrate = 9600
    serialBaglanti.parity = serial.PARITY_NONE
    serialBaglanti.stopbits = serial.STOPBITS_ONE
    serialBaglanti.bytesize = serial.EIGHTBITS
    serialBaglanti.timeout = 0

    if not serialBaglanti.isOpen():
        serialBaglanti.open()

    serialBaglanti.write(veri)

    serialBaglanti.close()

