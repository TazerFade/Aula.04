User = input("Digite seu nome: ")
Data = int(input("Informe o número do mês: "))

if Data < 1 or Data > 12:
    print("Data inválida, por favor digite um número entre 1 e 12.")
else:
    if Data == 1:
        print("A data corresponde ao mês de Janeiro")
    elif Data == 2:
        print("A data corresponde ao mês de Fevereiro")
    elif Data == 3:
        print("A data corresponde ao mês de Março")
    elif Data == 4:
        print("A data corresponde ao mês de Abril")
    elif Data == 5:
        print("A data corresponde ao mês de Maio")
    elif Data == 6:
        print("A data corresponde ao mês de Junho")
    elif Data == 7:
        print("A data corresponde ao mês de Julho")
    elif Data == 8:
        print("A data corresponde ao mês de Agosto")
    elif Data == 9:
        print("A data corresponde ao mês de Setembro")
    elif Data == 10:
        print("A data corresponde ao mês de Outubro")
    elif Data == 11:
        print("A data corresponde ao mês de Novembro")
    else:
        print("A data corresponde ao mês de Dezembro")
