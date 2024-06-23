from pycomm.ab_comm.slc import Driver as SlcDriver

def main():
    # Dirección IP del PLC MicroLogix 1400
    plc_ip = '192.168.1.100'

    # Configurar el controlador
    plc = SlcDriver()

    # Conectar al PLC
    plc.open(plc_ip)

    # Obtener la lista de tags
    tag_list = plc.get_tag_list()

    # Imprimir la lista de tags
    print("Lista de tags disponibles en el PLC con IP", plc_ip)
    for tag in tag_list:
        print(tag)

    # Cerrar la conexión con el PLC
    plc.close()

if __name__ == "__main__":
    main()
