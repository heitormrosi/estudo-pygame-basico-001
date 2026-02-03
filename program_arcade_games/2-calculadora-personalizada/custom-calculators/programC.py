from math import pi

def main() -> None:
    # Inicialização de variáveis
    r = 0
    area = 0

    # Entrada de dados
    print("Area of a circle")
    r = float(input("Enter the radius: "))
    
    # Processamento de dados
    area = pi * r ** 2
    
    # Saída de dados
    print(f"The area is: {area}")


if __name__ == "__main__":
    main()