menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """
saldo = 0
limite = 500
extrato = " "
numero_saque = 0
limite_saques = 3

while True:
  opcao = input(menu)
  if opcao == "1":
    print("Deposito")
    deposito=float(input("qual o valor gostaria de depositar?"))
    if deposito > 0:
      saldo += deposito
      extrato += f"Depósito: R$  {deposito:.2f}\n"
      print(saldo) 
    else:
      print("valor incorreto")
  elif opcao == "2":
    print("Saque")
    valor_saque = float(input("Qual valor deseja sacar?"))
    
    excedeu_saldo = valor_saque > saldo
    
    excedeu_limiti = valor_saque > limite
    
    excedeu_saque = numero_saque >= limite_saques 
    
    if excedeu_saldo:
      print("Operação falhou! Voçe não tem saldo suficiente")
    elif excedeu_limiti:
      print("Operação falhou! o valor do saque excede o limite diário")
    elif excedeu_saque:
      print("Operação falhou! Númeo máximo de saques excedido")
    elif valor_saque > 0:
      saldo -= valor_saque
      extrato += f"Saque: R$ {valor_saque:.2f}\n"
      numero_saque += 1
      print (f"valor de saque de R$ {valor_saque:.2f}, realizado com sucesso")
    else:
      print("O valor informado é invalido!" )
         
    
  elif opcao == "3":
    print("\n----------Extrato----------")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\n Saldo: R$ {saldo:.2f}")
    print("------------------------------")
  
  
  
  elif opcao == "0":
    break
  else:
    print("Opçao invalida, por favor tente novamente")
    

