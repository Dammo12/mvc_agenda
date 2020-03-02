from model.model import Model
from view.view import View

class Controller:

    #Constructor
    def __init__(self):
        self.model = Model()
        self.view = View()

    #Contacto conrtrollers
    def agregar_contacto(self, id_contacto, nombre, tel, correo, dire):
        b, c = self.model.agregar_contacto(id_contacto, nombre, tel, correo, dire)
        if b:
            self.view.agregar_contacto(c)
        else:
            self.view.contacto_ya_existe(id_contacto)

    def leer_contacto(self, id_contacto):
        e, c = self.model.leer_contacto(id_contacto)
        if e:
            self.view.mostrar_contacto(c)
        else:
            self.view.contacto_no_existe(id_contacto)
    
    def leer_todos_contactos(self):
        c = self.model.leer_todos_contactos()
        self.view.mostrar_contactos(c)

    def actualizar_contacto(self, id_contacto, n_nombre = '', n_tel = '', n_correo = '', n_dire = ''):
        e = self.model.actualizar_contacto(id_contacto, n_nombre, n_tel, n_correo, n_dire)
        if e:
            self.view.actualizar_contacto(id_contacto)
        else:
            self.view.contacto_no_existe(id_contacto)

    def borrar_contacto(self, id_contacto): 
        e, c = self.model.borrar_contacto(id_contacto)
        if e:
            self.view.borrar_contacto(c)
        else:
            self.view.contacto_no_existe(id_contacto)

    def leer_contactos_Letra(self, letra):
        c = self.model.leer_contactos_letra(letra)
        self.view.mostrar_contactos(c)

    # Citas

    def agregar_cita(self, id_cita, id_contacto, lugar, fecha, hora, asunto):
        b, c = self.model.agregar_cita(id_cita, id_contacto, lugar, fecha, hora, asunto)
        if b:
            self.view.crear_cita(c)
        else:
            self.view.cita_ya_existe(c)

    def actualizar_citas(self, id_cita, id_contacto, lugar, fecha, hora, asunto):
        comp, cita_o = self.model.leer_cita(id_cita)
        e, cita_n = self.model.actualizar_cita(id_cita, id_contacto, lugar, fecha, hora, asunto)
        if e:
            self.view.modificar_cita(cita_o, cita_n)
        else:
            self.view.cita_no_existe(id_cita)
        

    def leer_cita(self, id_cita):
        e, c = self.model.leer_cita(id_cita)
        if e:
            self.view.mostrar_cita(c)
        else:
            self.view.cita_no_existe(id_cita)

    def leer_citas(self):
        c = self.model.leer_todas_citas()
        self.view.mostrar_citas(c)


    def insertar_contactos(self):
        self.agregar_contacto(1, 'Damian', '4621234567', 'damian@hotmail.com', 'Calle 1')
        self.agregar_contacto(2, 'Hugo', '4627894561', 'hugo@hotmail.com', 'Calle 2')
        self.agregar_contacto(3, 'Juan', '4621452365', 'juan@hotmail.com', 'Calle 3')

    def insertar_citas(self):
        self.agregar_cita(1, 1, 'Cofee Italiano', '04/03/2020', '14:00', 'Charla')
        self.agregar_cita(2, 2, 'Abarrotes Doña Lupita', '25/10/2020', '13:00', 'Compra venta')
        self.agregar_cita(3, 3, 'Rosticería', '02/03/2020', '22:00', 'Ay apá un poliiito')

    def start(self):
        self.view.start()
        self.insertar_contactos()
        self.insertar_citas()
        self.leer_todos_contactos()
        self.leer_contactos_Letra('h')

    def menu(self):
        while(True):
            self.view.menu()
            o = input('Selecciona una opcion (1-9) ')
            if o == '1':
                id_contacto = input('Id: ')
                name = input('Nombre: ')
                tel = input('Telefono: ')
                correo = input('Correo: ')
                dire = input('Dirección: ')
                self.agregar_contacto(id_contacto, name, tel, correo, dire)
            elif o == '2':
                self.leer_todos_contactos()
            elif o == '3':
                self.view.menu_search()
                i = input('Seleccione una opción(1, 2) ')
                if i == '1':
                    id_contacto = int(input('Id: '))
                    self.leer_contacto(id_contacto)
                elif i == '2':
                    letra = input('Letra: ')
                    self.leer_contactos_Letra(letra) 
            elif o == '4':
                id_contacto = int(input('Id del contacto a actualizar: '))
                name = input('Nombre: ')
                tel = input('Telefono: ')
                correo = input('Correo: ')
                dire = input('Dirección: ')
                self.actualizar_contacto(id_contacto, name, tel, correo, dire)
            elif o == '5':
                id_contacto = int(input('Id: '))
                self.borrar_contacto(id_contacto)
            elif o == '6':
                id_cita = input('Id: ')
                id_contacto = input('Id Contacto: ')
                lugar = input('Lugar: ')
                fecha = input('Fecha: ')
                hora = input('Hora: ')
                asunto = input('Asunto: ')
                self.agregar_cita(id_cita, id_contacto, lugar, fecha, hora, asunto)
            elif o == '7':
                self.leer_citas()
            elif o == '8':
                i = int(input('Id: '))
                self.leer_cita(i)
            elif o == '9':
                id_cita = int(input('Id: '))
                id_contacto = input('Id Contacto: ')
                lugar = input('Lugar: ')
                fecha = input('Fecha: ')
                hora = input('Hora: ')
                asunto = input('Asunto: ')
                self.actualizar_citas(id_cita, id_contacto, lugar, fecha, hora, asunto)
            else:
                pass