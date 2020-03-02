class View:
    def mostrar_contacto(self, contact):
        print('**** Datos del contacto ****')
        print('Nombre: ', contact.nombre)
        print('Telefono: ', contact.tel)
        print('Correo: ', contact.correo)
        print('Direccion: ', contact.dire)
        print('****************************')

    def mostrar_contactos(self, contactos):
        print('******** Contactos ********')
        for c in contactos:
            print(c.nombre, c.tel, c.correo, c.dire)
        print('***************************')

    def agregar_contacto(self, contacto):
        print(contacto.nombre, 'se ha agregado a la base de datos')

    def borrar_contacto(self, contacto):
        print(contacto.nombre, 'se ha borrado a la base de datos')

    def actualizar_contacto(self, id_contacto):
        print(id_contacto, 'se ha modificado correctamente')

    def contacto_ya_existe(self, contacto):
        print(contacto.id_contacto, 'YA EXISTE EN LA BD')

    def contacto_no_existe(self, id_contacto):
        print(id_contacto, 'NO EXISTE EN LA BD')

    def start(self):
        print('Esto es un ejemplo de vista sencilla')

    def end(self):
        print('Hasta la vista')
    
    def menu(self):
        print('1. Agregar contacto')
        print('2. Ver contactos')
        print('3. Buscar contacto')
        print('4. Actualizar contacto')
        print('5. Borrar contacto')
        print('6. Agregar cita')
        print('7. Ver citas')
        print('8. Buscar cita')
        print('9. Actualizar cita')
        print('10. Borrar cira')
        print('')
        print('')

    def menu_search(self):
        print('1. Buscar por Id')
        print('2. Buscar por letra')

    #Citas

    def mostrar_cita(self, cita):
        print('*********** Cita ***********')
        print('Contacto: ', cita.id_contacto)
        print('Lugar: ', cita.lugar)
        print('Hora: ', cita.hora)
        print('Fecha: ', cita.fecha)
        print('Asunto: ', cita.asunto)
        print('****************************')

    def mostrar_citas(self, citas):
        print('********** Citas **********')
        for c in citas:
            print(c.id_contacto, c.lugar, c.fecha, c.hora, c.asunto)
        print('***************************')

    def crear_cita(self, cita):
        print('Cita agregada el:', cita.fecha)

    def borrar_cita(self, cita):
        print('Cita eliminada el:', cita.fecha)

    def modificar_cita(self, cita_o, cita_n):
        print('Cita:', cita_o.id_cita, 'con fecha:', cita_o.fecha, 'se ha modificado correctamente')

    def cita_ya_existe(self, cita):
        print(cita.id_cita, 'YA EXISTE EN LA BD')

    def cita_no_existe(self, id_cita):
        print(id_cita, 'NO EXISTE EN LA BD')