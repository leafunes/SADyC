import commandSender
import threading

cantAnalogicos = 0


def setAnalogsInputs(cantPines):
    global cantAnalogicos
    commandSender.setCantAnalog(cantPines)
    cantAnalogicos += cantPines


def setTimingForInput(miliseconds):
    commandSender.setTimingOfReciv(miliseconds)


def medir(analogCallback, digitalCallback):

    def toThread():
        while True:
            res = commandSender.read(1 + cantAnalogicos * 2)
            if(res):
                analog = []
                digital = []
                digitalByte = res[0]
                analogBytes = res[1:]

                for i in range(0, len(analogBytes), 2):
                    analog.append(
                        (ord(analogBytes[i]) << 8) + ord(analogBytes[i + 1]))

                for bit in __getBits(digitalByte):
                    digital.append(bit)

                analogCallback(analog)
                digitalCallback(digital)

    t = threading.Thread(target=toThread)
    t.setDaemon(True)
    t.start()


def __getBits(byte):
    mask = 128
    toRet = []
    for i in range(8):
        bit = (ord(byte) & mask) >> (7 - i)
        toRet.append(bit)
        mask = mask >> 1
    return toRet
