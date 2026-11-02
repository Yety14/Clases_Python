color = "rojo"  #"rojo", "amarillo", "verde", "azul"

match color:
    case "rojo":
        print("Para")
    case "amarillo":
        print("Prepárate")
    case "verde":
        print("Avanza")
    case _:
        print("Color no válido")   