while True: 
    print("-----Menu-----")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("5 - Sair")
    print(10 * "-")
    escolha = int(input("Escolha uma operação ou tecle 5 para sair: "))
    print(10 * "-")
    if escolha >= 1 and escolha <=4:
        a = float(input("Digite o primeiro numero: "))
        print(10 * "-")
        b = float(input("Digite o segundo numero: "))
        print(10 * "-")
        if escolha == 1:
            print(f"Resultado: {a+b}")
        elif escolha == 2:
            print(f"Resultado: {a-b}")
        elif escolha == 3:
            print(f"Resultado: {a*b}")
        elif escolha == 4:
            if b != 0:
                print(f"Resultado: {a/b}")
            else:
                print("Erro: Divisão por zero!")    
    elif escolha == 5:
        print("Saindo do programa")        
        break
    else:
        print("Opção inválida")
