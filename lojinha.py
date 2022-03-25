pedido = input("O que você deseja comprar? Fruta ou Legume?").lower()

if pedido == "fruta":
    escolha = input("Temos Banana, Uva, Morango e Laranja").lower()
    if escolha == "banana":
        quantidade = int(input(f"Quantas {escolha}s você deseja?"))
        if quantidade > 1:
            print(f"No seu carrinho tem {quantidade} {escolha}s")
        else:
            print(f"No seu carrinho tem {quantidade} {escolha}")
    elif escolha == "uva":
        quantidade = int(input(f"Quantas {escolha}s você deseja?"))
        if quantidade > 1:
            print(f"No seu carrinho tem {quantidade} {escolha}s")
        else:
            print(f"No seu carrinho tem {quantidade} {escolha}")
    elif escolha == "morango":
        quantidade = int(input(f"Quantas {escolha}s você deseja?"))
        if quantidade > 1:
            print(f"No seu carrinho tem {quantidade} {escolha}s")
        else:
            print(f"No seu carrinho tem {quantidade} {escolha}")
    elif escolha == "laranja":
        quantidade = int(input(f"Quantas {escolha}s você deseja?"))
        if quantidade > 1:
            print(f"No seu carrinho tem {quantidade} {escolha}s")
        else:
            print(f"No seu carrinho tem {quantidade} {escolha}")
elif pedido == "legume":
    escolha = input("Temos Alface, Tomate e Cenoura").lower()
    if escolha == "alface":
        quantidade = int(input(f"Quantas {escolha}s você deseja?"))
        if quantidade > 1:
            print(f"No seu carrinho tem {quantidade} {escolha}s")
        else:
            print(f"No seu carrinho tem {quantidade} {escolha}")
    elif escolha == "tomate":
        quantidade = int(input(f"Quantas {escolha}s você deseja?"))
        if quantidade > 1:
            print(f"No seu carrinho tem {quantidade} {escolha}s")
        else:
            print(f"No seu carrinho tem {quantidade} {escolha}")
    elif escolha == "cenoura":
        quantidade = int(input(f"Quantas {escolha}s você deseja?"))
        if quantidade > 1:
            print(f"No seu carrinho tem {quantidade} {escolha}s")
        else:
            print(f"No seu carrinho tem {quantidade} {escolha}")
