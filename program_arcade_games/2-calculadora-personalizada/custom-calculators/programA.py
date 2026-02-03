def main() -> None:
    # Inicialização de variáveis
    fahrenheit =  0
    celcius = 0
    
    # Entrada de dados
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))


    # Processamento de dados
    celcius = 5/9 * (fahrenheit - 32)

    # Saída de dados
    print(f"The temperature in Celcius: {celcius}")


if __name__ == "__main__":
    main()