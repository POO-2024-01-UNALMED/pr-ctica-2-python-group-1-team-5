from gestorAplicacion.establecimientos.establecimiento import Establecimiento
from gestorAplicacion.establecimientos.cementerio import Cementerio
from gestorAplicacion.establecimientos.crematorio import Crematorio
from gestorAplicacion.establecimientos.funeraria import Funeraria

from gestorAplicacion.personas.persona import Persona
from gestorAplicacion.personas.cliente import Cliente
from gestorAplicacion.personas.empleado import Empleado
from gestorAplicacion.personas.familiar import Familiar

from gestorAplicacion.inventario.urna import Urna
from gestorAplicacion.inventario.tumba import Tumba

if __name__ == "__main__":
    print("Holaaaaa")
    e1=Establecimiento("a")
    cementerio1=Cementerio("cementerio1",23,None,"oro",None,"cenizas",None)
    crematorio1=Crematorio("crematorio1",12,None,"oro",None,None)
    funeraria1=Funeraria("funeraria1",None,None)
    print(cementerio1)
    print(crematorio1)
    print(funeraria1)

    #personas
    persona1= Persona("persona1",123,23,None)
    cliente1=Cliente("cliente1",21,20)
    familiar1=Familiar("familiar1",0,45,None,"mama",0,None)
    empleado1=Empleado("empleado1",None,"mañana","se",23,0,2,None)

    print(persona1)
    print(cliente1)
    print(familiar1)
    print(empleado1)

    #inventario

    urna1=Urna("Urnita1",cementerio1,12,2,"fija")
    tumba1=Tumba("Tumbita1",cementerio1,12,2)
    
    print(urna1)
    print(tumba1)






