edad = int(input("ingrese su edad"))
salario = int(input("ingrese su salario"))
if edad >= 18 and salario >= 3000000:
    print("usted debe de tributar")
elif edad <= 17 and salario >=3000000:
    print("utd debe ributar")
else:
    print("usted no debe de tributar")
