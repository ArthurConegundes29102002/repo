import MINHEAP as heap
import linecache
#---------------------------------------- algoritmo de prim :

with open('valores.txt','r') as arquivo:
    tabela = arquivo.readlines()

numero_nos=int(len(tabela)**(1/2))

numero_de_arestas=int(len(tabela))

lista_heap=[]

#lista de vizinhos pra cada nó : 

lista_vizinhos=[[]*numero_nos for i in range(numero_nos)]

lst_adj=[]

for j in range(1,numero_de_arestas):

    linha = linecache.getline('valores.txt',j)

    nova_lista=linha.split()

    deusmeajuda=list(map(int,nova_lista))

    valor1=int(deusmeajuda[0])

    valor2=int(deusmeajuda[1])

    custo=int(deusmeajuda[2])

    lista_vizinhos[valor1].append((valor2,custo))

    lista_vizinhos[valor2].append((valor1,custo))

    lst_adj.append((valor1,valor2))
# até aqui estamos apenas criando a estrutura do grafo 

# começando a bagunça ...... 

#raiz escolhida : 

raiz = int(input("digite o ID da cidade de onde deseja começar:"))

for (x,custo) in lista_vizinhos[raiz]:

    heap.heappush(lista_heap,(custo,raiz,x))

contador_auxiliar = 0

custo_total=0

marcados=[raiz]

arvore_geradora=[]

while contador_auxiliar<numero_nos-1:

    while True:

        (custo,valor1,valor2)=heap.heappop(lista_heap)

        if valor2 not in marcados:

            break
        
    marcados.append(valor2)

    custo_total+=custo

    arvore_geradora.append((valor1,valor2))

    contador_auxiliar+=1

    for(x,custo) in lista_vizinhos[valor2]:

        if x not in marcados:

            heap.heappush(lista_heap,(custo,valor2,x))


#-------------------------------------- dicionario de nomes das cidades : 

lista=[]

for x in range(1,numero_nos+1):

    tabela = linecache.getline('base.txt',x)

    lista.append(tabela)


dicionario=lista

print('')
print(f'distância percorrida :  {custo_total} KM ')

for x in arvore_geradora:
    print(f'{dicionario[x[0]]}     ------>     {dicionario[x[1]]}')

    
