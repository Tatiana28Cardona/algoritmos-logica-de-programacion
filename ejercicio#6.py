print("Bienvenidos a Pizzeria Bello Napoli")
print(" elija si desea 1. pizza vegetariana o  2. pizza no vegetariana")
pedido1 = input ("1. o 2.")
if pedido1 == "1":
    print("¡su pizza es vegetariana!!")
    vegetariana = input ("la base de todas las pizzas es de mozarella y tomate, adicional puede llevar p. pimiento y t tofu..cual desea agregar?")
    if vegetariana == "p":
        print("los ingrediente de su pizza son: mozarella, tomate y pimiento")
    else:
        print("los ingredientes de su pizza son: mozarella, tomate y tofu")
else:
    print("¡su pizza no es vegetariana!!")
    no_vegetariana = input("la base de todas las pizzas es de mozarella y tomate, adicional puede llevar, pp. peperoni, j. jamon, s. salmon...cual desea agregar?")
    if no_vegetariana == "pp":
        print("los ingrediente de su pizza son: mozarella, tomate y peperoni")
    elif no_vegetariana == "j":
        print("los ingrediente de su pizza son: mozarella, tomate y jamon")
    else:
        print("los ingrediente de su pizza son: mozarella, tomate y salmon")   









    

 
