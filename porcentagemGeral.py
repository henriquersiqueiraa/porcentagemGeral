valor = float(input("Digite o valor: R$ ").replace(",", "."))
porc = float(input("Digite a porcentagem: ").replace(",", "."))
perc = valor * (porc / 100)
desc = valor - perc
aum = valor + perc
print(f"O valor com desconto é R$ {desc:.2f}".replace(".", ","))
print(f"O valor do desconto é R$ {perc:.2f}".replace(".", ","))

print(f"O valor com aumento é R$ {aum:.2f}".replace(".", ","))
print(f"O valor do aumento é R$ {perc:.2f}".replace(".", ","))

print(f"O valor original é R$ {valor:.2f}".replace(".", ","))
print(f"A porcentagem de desconto é {porc:.2f}%".replace(".", ","))