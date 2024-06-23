from pycomm3 import SLCDriver
import time

with SLCDriver('192.168.1.100') as PLC:
    # Leer valor entero
    readTag = PLC.read('N7:0')
    print(f"Valor entero: {readTag.value}")

    # Leer valor del temporizador
    readTag = PLC.read('T4:0.PRE')
    print(f"Valor de preajuste del temporizador: {readTag.value}")

    # Leer valor del contador
    readCount = 0
    while readCount < 10:
        readTag = PLC.read('C5:0.ACC')
        print(f"Iteración {readCount + 1}, Valor del contador: {readTag.value} @ {time.ctime()}")
        readCount += 1
        time.sleep(3)
