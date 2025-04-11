menu ="""

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""

saldo = 0
limite = 500
extrato = []
numero_saques = 0
limite_saques = 3
saque_dia = 0
valor_deposito = 0
saque = 0


while True:

    
    opcao = input(menu)

    if opcao == "d":
        print("Depósito")
        valor_deposito = int(input("Qual valor será depositado?"))
        if valor_deposito > 0:
            saldo += valor_deposito
            print(f"O deposito de {valor_deposito} foi realizado")
            extrato.append(f"Deposito: R${valor_deposito:.2f}")
        else:
            print("Insira um valor positivo de depósito")


    elif opcao == "s":
        print("Saque")
        if numero_saques < limite_saques:
            saque = int(input("Qual o valor a sacar: "))
            if saque <= limite: # 500 reais
                if (saque_dia + saque) <= 1500:
                    if saque <= saldo:
                        saldo -= saque
                        print(f"Voce acaba de sacar {saque:.2f}")
                        saque_dia += saque
                        numero_saques += 1
                        ### armazenar cada saque no extrato
                        extrato.append(f"Saque: R${saque:.2f}")
                elif saldo < saque:
                    print("voçe não tem saldo suficiente.")
                elif (saque_dia + saque) > 1500:
                    print("O saque ultrapassa o limitew diario de 1500 reais")
            else:
                print("Seu limite de saque é de 500 reais")
        else:
            print("Numero de saques diários excedido!")
            

    elif opcao == "e":
        print("")
        print(10*"#")
        print("Extrato")
        print("")
        for i in extrato:
            print(i)
        print(f"Saldo: {saldo   }")

    elif opcao == "q":
        print("Voce finalizou suas operações!")
        break
    
    else:
        print("Digite uma opção valida no Menu")