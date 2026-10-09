produto = "Mouse Gamer Wifi"
valores = [20,71,100,30]



if "mouse".lower() in produto.lower():
        print("Produto encontrado!")

else:
        print("Produto nao encontrado")



        
def dobrar (valor):
    resultado = valor * 2
    return resultado
print(dobrar(11))



for item in valores:
  valores_novos = []
  valores_novos.append (dobrar(item))
  print(valores_novos)
 

alunos = ["Ana","Hugo","Mariana","Pedro","Ana Paula"]

aluno_procurado = input("digite um nome: ")
alunos_encontrados = []

for item in alunos:
    alunos_encontrados.append(item)

print(alunos_encontrados)







