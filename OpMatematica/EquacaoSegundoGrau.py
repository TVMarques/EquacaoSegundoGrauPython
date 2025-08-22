import math

while True:
        print("====EQUAÇÃO DE 2° GRAU====")
        print("A equação é assim: Ax² + Bx + C = 0")

        # Entrada dos coeficientes
        a = int(input("Digite o valor de A: "))
        b = int(input("Digite o valor de B: "))
        c = int(input("Digite o valor de C: "))

        # Mostrando a equação
        print(f"\nEquação: {a}x² + {b}x + {c} = 0")

        # Fórmula do Delta
        print("Δ = B² - 4.A.C")

        # Calculando o Delta
        delta = b**2 - 4*a*c
        print(f"Δ = {b}² - 4.{a}.{c}")
        print(f"Δ = {delta}\n")

        # Verificando as raízes
        if delta < 0:
            print("Não existem raízes reais.")
        elif delta == 0:
            x = -b / (2*a)
            print("Existe uma raiz real (raiz dupla).")
            print(f"x = {x:.1f}")
        else:
            x1 = (-b + math.sqrt(delta)) / (2*a)
            x2 = (-b - math.sqrt(delta)) / (2*a)
            print("Existem duas raízes reais:")
            print(f"X¹ = (-B + √Δ) / (2.A) = (-{b} + √{delta}) / (2.{a})")
            print(f"X¹ = {x1:.1f}")
            print(f"X² = (-B - √Δ) / (2.A) = (-{b} - √{delta}) / (2.{a})")
            print(f"X² = {x2:.1f}")

        # Loop para validar a resposta do usuário
        while True:
            resposta = input("\nDeseja calcular outra equação? (S/N): ").strip().upper()#//strip remove os espaços e upper deixa tudo maiúsculo.
            if resposta in ["S", "N"]: #Aqui se usa in e uma lista. Pode se fazer com o || e usando uma tupla.
                break
            print("Entrada inválida! Digite 'S' para sim ou 'N' para não.")

        if resposta == "N":
          break

print("Fim do programa!")
