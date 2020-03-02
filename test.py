from model.contact import Contacto
from model.cita import Cita
from model.model import Model
from view.view import View
from controller.controller import Controller

"""m = Model()



contactos = []
m.agregar_contacto(1, 'Juan Pérez', '4621234567', 'eljuan@hotmail.com', 'Calle chida #123, Colonia chida')
m.agregar_contacto(2, 'Roger González', '4625821452', 'roger1@hotmail.com', 'Hola calle, Hola colonia')

s = m.leer_todos_contactos()

for c in s:
    print(c.nombre, c.tel)

m.agregar_contacto(3, 'Angela', '4648759451', 'hola@hola.com', 'Calle3')

m.actualizar_contacto(2, n_nombre = 'Abulilla')

s = m.leer_todos_contactos()

for c in s:
    print(c.nombre, c.tel)

s = m.leer_contactos_letra('a')

for c in s:
    print(c.nombre, c.tel)

m.borrar_contacto(3)

c4 = m.leer_contacto(3)

t1 = Cita(1, 1, 'Aula 310', '20-02-2020', '14:00', 'Clases de Sistemas de Información')


m.agregar_cita(1, 1, 'Café', '20/02/2020', '16:00', 'Ir a tomar café')
m.agregar_cita(2, 1, 'Cy', '25/02/2020', '11:00', 'Ir a ver Netflis')
m.agregar_cita(3, 2, 'Cyber hola', '25/02/2020', '11:00', 'Ir a ver Netflis con el otro')
m.agregar_cita(4, 2, 'Cyber x2', '25/02/2020', '11:00', 'Ir a ver Netflis con el otro')

s = m.leer_todas_citas()

for c in s:
    print(c.lugar)

v = View()
s = m.leer_todos_contactos()
v.mostrar_contactos(s)
c = m.leer_contacto(2)
v.mostrar_contacto(c)

f, c = m.borrar_contacto(1)
if f:
    v.borrar_contacto(c)
else:
    v.contacto_no_existe(1)

s = m.leer_todos_contactos()
v.mostrar_contactos(s)

s = m.leer_todas_citas()
v.mostrar_citas(s)
s = m.leer_cita(3)
v.mostrar_cita(s)
"""

cont = Controller()
cont.start()
cont.menu()