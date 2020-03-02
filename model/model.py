from .contact import Contacto
from .cita import Cita

class Model:
    def __init__(self):
        self.contacts = []
        self.citas =[]

    def esta_id(self, id_contacto):
        for c in self.contacts:
            if c.id_contacto == id_contacto:
                return True, c
        return False, 0
    

    def agregar_contacto(self, id_contacto, nombre, tel, correo, dire):
        if not self.esta_id(id_contacto)[0]:
            c = Contacto(id_contacto, nombre, tel, correo, dire)
            self.contacts.append(c)
            return True, c
        return False, c

    def leer_contacto(self, id_contacto):
        e, c = self.esta_id(id_contacto)
        return e, c

    def leer_todos_contactos(self):
        return self.contacts

    def leer_contactos_letra(self, letra):
        lista = [c for c in self.contacts if c.nombre.lower().startswith(letra.lower())]
        #lista = []
        #for c in self.contacts:
        #    if c.nombre.lower().startswith(letra):
        #        lista.append(c)
        return lista

    def actualizar_contacto(self, id_contacto, n_nombre, n_tel, n_correo, n_dire):
        e, c = self.esta_id(id_contacto)
        if e:
            if n_nombre != '':
                c.nombre = n_nombre
            if n_tel != '':
                c.tel = n_tel
            if n_correo != '':
                c.correo = n_correo
            if n_dire != '':
                c.dire = n_dire
            return True
        return False

    def borrar_contacto(self, id_contacto):
        e, contacto = self.esta_id(id_contacto)

        if e:
            self.contacts.remove(contacto)
            lista_temp = [c for c in self.citas if c.id_contacto == id_contacto]
            for c in lista_temp:
                self.citas.remove(c)
            return True, contacto
        return False, 0

    def cita_id(self, id_cita):
        for c in self.citas:
            if c.id_cita == id_cita:
                return True, c
        return False, 0
    
    def agregar_cita(self, id_cita, id_contacto, lugar, fecha, hora, asunto):
        if not self.cita_id(id_cita)[0]:
            c = Cita(id_cita, id_contacto, lugar, fecha, hora, asunto)
            self.citas.append(c)
            return True, c
        return False, c

    def leer_cita(self, id_cita):
        e, c = self.cita_id(id_cita)
        if e:
            return True, c
        return False, 0

    def actualizar_cita(self, id_cita, id_contacto, lugar, fecha, hora, asunto):
        e, c = self.cita_id(id_cita)
        if e:
            c.id_contacto = id_contacto
            c.lugar = lugar
            c.fecha = fecha
            c.hora = hora
            c.asunto = asunto
            return True, c
        return False, c

    def borrar_cita(self, id_cita):
        e, c = self.cita_id(id_cita)

        if e:
            self.citas.remove(c)
            return True, c
        return False, 0

    def leer_citas_fecha(self, fecha):
        lista = [c for c in self.citas if c.fecha == fecha]
        return lista

    def leer_todas_citas(self):
        return self.citas