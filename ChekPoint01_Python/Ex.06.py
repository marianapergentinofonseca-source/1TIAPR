# 6. Desconto em produto
# Receba o valor de um produto e mostre o preço 
# final com desconto de 10% se o valor for maior que 100; caso contrário, mostre o preço sem desconto.

valor_produto = float(input("digite aqui o valor do produto: "))
if valor_produto <=100:
    print(f"o valor do produto é {valor_produto}")
else:
    valor_desconto = valor_produto*0.9
    print(f"o valor do produto com desconto é R$ {valor_desconto}")