texto = "ola, mundo"

#fatiar do inicio até um indice especifico
print(texto[:5])

#fatiar a partir de um indice especifico até o final
print(texto[6:])

#fatiar do inicio até o final, com um passo especifico
print(texto[::2])

#fatiar com inicioe e fim especifico
print(texto[4:9])

#fatiar com um passo negativo para inverter uma substring
print(texto[::-1])



frutas = ["maca", "banana", "laranja"]
print("lista de frutas:", frutas)

frutas.append("uva")
print("lista de frutas atualizadas:", frutas)
print("primeira fruta:", frutas[3])

frutas.remove(frutas[2])
print("lista de frutas atualizadas:", frutas)



#exemplo com dicionarios/objetos
pessoa = {"nome": "Tailaine", "idade": 21}
print("pessoa:", pessoa)

#acessando valores
print("nome:", pessoa["nome"])

#adicionando um novo par chave-valor
pessoa["cidade"] = "Franca"
print("pessoa atualizada:", pessoa)

del pessoa["cidade"]
print(pessoa)



listapessoa = []

pessoa = {"nome": "Tailaine", "idade": 21}
listapessoa.append(pessoa)
print(listapessoa)

pessoa = {"nome": "Felipe", "idade": 20}
listapessoa.append(pessoa)
print(listapessoa)

Tailaine = listapessoa [1]
print(Tailaine)



#tuple
coordenadas = (10, 20)
print("coordenadas:", coordenadas)

a = {1,2,3}
b = {3,4,5}
conjunto = (b & a)
print(6 in conjunto)