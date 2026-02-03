def main() -> None:
    # Inicialização de variáveis
    x1 = 0
    x2 = 0
    h = 0
    area = 0

    # Entrada de dados
    print("Area of a trapezoid")
    h = float(input("Enter the height of the trapezoid: "))
    x1 = float(input("Enter the lenght of the bottom base: "))
    x2 = float(input("Enter the length of the top base: "))
    
    # Processamento de dados
    area = 1/2 * (x1 + x2) * h
    
    # Saída de dados
    print(f"The area is: {area}")


if __name__ == "__main__":
    main()