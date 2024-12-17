# Actividad de semana 5
# Se le pide a la persona que ingrese el año en que en que se encuentra actualmente
actual_año = int(input("Ingrese el año en que se encuentra actualmente: "))# se ingresa el año actual
usuario_año = int(input("Ingrese un año cualquiera: "))# se ingresa un año cualquiera la persona
#operacion para calcular el tiempo trascurrido entre los años que han ingresado
resta1= actual_año  - usuario_año
resta2 =usuario_año-actual_año

if actual_año == usuario_año:
    print("Error el año que ingresaste es el mismo que el año actual")#Si el usuario ingresa el mismo año se le maracara un mensaje que le dira su error
elif usuario_año > actual_año:
    print("Aun faltan",resta2, " años para llegar al año indicado")# si la persona marca un año mayor que el año actual se le presentara como "aun faltan los años que ha ingresado"
elif actual_año < usuario_año:
    print("Han pasado",resta1,"años desde el año que ha indicado")# si la persona marca menor al año actual se le presentera el resultado como "han pasado los años que ingreso y su resultado del año que paso"
elif usuario_año > actual_año:
    print("Para llegar a", (usuario_año), "falta"+ str(resta2) +"años" )
else:
    2023 <= actual_año and actual_año < 2024 #si es manor al año actual solo se le representara como"ha pasado solo un año del que ingreo"
    print("Ha pasado solo",resta1, "año del que ingresaste")