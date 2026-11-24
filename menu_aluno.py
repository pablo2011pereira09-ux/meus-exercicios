#MENU
def mostrar_menu ():
    print("\n ===== MENU ===== ")
    print("[1] Dados do Aluno")
    print("[2] Calcular e apresentar a media das tres notas")
    print("[3] Aprovado ou reprovado")
    print("------------------------------------------------------")



#CHAMAR FUNCAO
mostrar_menu()



#PARTE MENU
def mostrar_resto(n):
    n = input("Insira o que deseja:")
    soma = 0
    if n == "1":
        n1 = input("Nome do aluno? ")
        n2 = int(input("Numero na escola:"))
        print(f"Olá {n1} o seu numero na escola é o {n2}.")
    elif n == "2":
        n3 = int(input("Diga a primeira nota: "))
        n4 = int(input("Diga a segunda nota: "))
        n5 = int(input("Diga a terceira nota: "))
        soma = n3+n4+n5
        media = soma/3
        print(f"Media do aluno: {media :.2f}")
    elif n == "3":
        n6 = int(input("Diga a sua nota:"))
        if n6 >= 10:
            print("Aprovado")
        else:
            print("Reprovado")



#CHAMAR FUNCAO
mostrar_resto("n")
mostrar_menu()
mostrar_resto("n")
mostrar_menu()
mostrar_resto("n")
