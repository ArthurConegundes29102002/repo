def heapbaixo(heap, posicaoinicial, posicao):

    novo_valor = heap[posicao]

    while posicao > posicaoinicial:

        posicao_pai = (posicao - 1) >> 1

        parente = heap[posicao_pai]

        if novo_valor < parente:

            heap[posicao] = parente

            posicao = posicao_pai

            continue
        break
    heap[posicao] = novo_valor
#----------------------------------------
def heapcima(heap, posicao):

    posicaofinal = len(heap)

    posicaoinicial = posicao

    novo_valor = heap[posicao]

    posicao_filho = 2*posicao + 1 

    while posicao_filho < posicaofinal:

        rightpos = posicao_filho + 1

        if rightpos < posicaofinal and not heap[posicao_filho] < heap[rightpos]:

            posicao_filho = rightpos

        heap[posicao] = heap[posicao_filho]

        posicao = posicao_filho

        posicao_filho = 2*posicao + 1

    heap[posicao] = novo_valor

    heapbaixo(heap, posicaoinicial, posicao)
#----------------------------------------
def heappush(heap, valor):

    heap.append(valor)

    heapbaixo(heap, 0, len(heap)-1)
#----------------------------------------
def heappop(heap):

    ultimo_elemento = heap.pop()

    if heap:

        retorna_valor = heap[0]

        heap[0] = ultimo_elemento

        heapcima(heap, 0)

        return retorna_valor

    return ultimo_elemento

#----------------------------------------
