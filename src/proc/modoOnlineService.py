import commandSender
import threading
import placaService

cantAnalogicos = 0


def setAnalogsInputs(cantPines):
    global cantAnalogicos

    commandSender.setCantAnalog(cantPines)
    cantAnalogicos = cantPines
    placaService.__estados["seteado"] = True
    print cantAnalogicos


def setTimingForInput(miliseconds):
    commandSender.setTimingOfReciv(miliseconds)


def setTimingForRegistro(segundos):
    commandSender.setTimingOfRegistro(segundos)


def medir(analogCallback, digitalCallback):

    placaService.__estados["midiendo"] = True

    def toThread():
        while True:
            res = commandSender.read(1 + cantAnalogicos * 2)

            if not placaService.__estados["midiendo"]:
                break

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

    thread = threading.Thread(target=toThread)
    thread.start()


def __getBits(byte):
    mask = 128
    toRet = []
    for i in range(8):
        bit = (ord(byte) & mask) >> (7 - i)
        toRet.append(bit)
        mask = mask >> 1
    return toRet
