
def big_mac():
    print("sanduíche big mac")

print("inicio")
big_mac()
print("fim")

def fazer_big_mac(nome):
     print(f"sanduíche big mac {nome}")


#fazer_big_mac("Higor")
#fazer_big_mac("Larissa")
#fazer_big_mac("Lucas")

def fazer_batata(tamanho):
     print(f"batata {tamanho}")

def preparar_refrigerante(tipo,tamanho):
     print(f"{tipo} {tamanho}")

#fazer_big_mac("Higor")
#fazer_batata("Grande")
#preparar_refrigerante("Coca-cola","Média")

def fazer_combo_big_mac(nome, tamanho_batata,tipo_refri, tamanho_refri):
     fazer_big_mac(nome)
     fazer_batata(tamanho_batata)
     preparar_refrigerante(tipo_refri, tamanho_refri)

#fazer_combo_big_mac("Higor", "Grande", "Coca-cola", "Média")

def soma_num(num1, num2):
     return num1 + num2

#resultado = soma_num(15,20)
#print(resultado)

def maior_num(lista_num):
     lista_num.sort()
     lista_num.reverse()
     maior_num = lista_num[0]
     return maior_num

resultado = maior_num([3123,12,312,321,62,534345,5634634])
print(resultado)