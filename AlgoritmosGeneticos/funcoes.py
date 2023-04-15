import random
import numpy as np

###############################################################################
#                                   Suporte                                   #
##############################################################################+

def distancia_entre_dois_pontos(a, b):
    """Computa a distância Euclidiana entre dois pontos em R^2

    Args:
      a: lista contendo as coordenadas x e y de um ponto.
      b: lista contendo as coordenadas x e y de um ponto.

    Returns:
      Distância entre as coordenadas dos pontos `a` e `b`.
    """

    x1 = a[0]
    x2 = b[0]
    y1 = a[1]
    y2 = b[1]

    dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1 / 2)

    return dist

def cria_cidades(n):
    """Cria um dicionário aleatório de cidades com suas posições (x,y).

    Args:
      n: inteiro positivo
        Número de cidades que serão visitadas pelo caixeiro.

    Returns:
      Dicionário contendo o nome das cidades como chaves e a coordenada no plano
      cartesiano das cidades como valores.
    """

    cidades = {}

    for i in range(n):
        cidades[f"Cidade {i}"] = (random.random(), random.random())

    return cidades

def computa_mochila(individuo, objetos, ordem_dos_nomes):
    """Computa o valor total e peso total de uma mochila
    Args:
      individiuo:
        Lista binária contendo a informação de quais objetos serão selecionados.
      objetos:
        Dicionário onde as chaves são os nomes dos objetos e os valores são
        dicionários com a informação do peso e valor.
      ordem_dos_nomes:
        Lista contendo a ordem dos nomes dos objetos.
    Returns:
      valor_total: valor total dos itens da mochila em unidades de dinheiros.
      peso_total: peso total dos itens da mochila em unidades de massa.
    """

    # Vamos ter uma lista cheia de zeros e uns,
    # Se 0, não pegou objeto
    # Se 1, pegou o objeto
    
    # Algoritmo irá gerar listas aleatórias que irão computar itens escolhidos aleatoriamente
    # Caso o item tenha sido escolhido, computa seu valor
    
    valor_total,peso_total = 0,0
    
    for pegou_o_item_ou_nao, nome_do_item in zip(individuo, ordem_dos_nomes):
        if pegou_o_item_ou_nao == 1:
            valor_do_item = objetos[nome_do_item]['valor']
            peso_do_item = objetos[nome_do_item]['peso']
            
            valor_total += valor_do_item
            peso_total += peso_do_item
    
    return valor_total, peso_total

###############################################################################
#                                    Genes                                    #
###############################################################################

def gene_cb():
    """
    Gera um gene válido para o problema das caixas binárias
    
    Args:
        
    
    Return:
        Valor entre 0 e 1
    """
    lista = [0,1]
    gene = random.choice(lista)
    return gene

def gene_cnb(valor_max_caixa):
    """
    Gera um gene válido para o problema das caixas binárias
    
    Args:
        
    
    Return:
        Valor entre 0 e um "valor_max_caixa"
    """
    gene = random.randint(0,valor_max_caixa)
    return gene

def gene_letras(letras):
    """Sorteia uma letra
    
    Args:
        letras: letras disponíveis que podem ser sorteadas
    
    Return:
        Retorna uma letra escolhida dentre as possíveis de serem sorteadas
    """
    
    letra = random.choice(letras)
    return letra

###############################################################################
#                                  Indivíduos                                 #
###############################################################################

def individuo_cb(n):
    """Gera um indivíduo para o problema das caixas binárias
    
    Args:
        n: número de genes do indivíduo
    
    Return:
        Lista com n genes, onde cada gene é um valor entre 0 e 1
    """
    individuo = []
    
    for i in range(n):
        individuo.append(gene_cb())
    
    return individuo

def individuo_cnb(n,valor_max_caixa):
    """Gera um indivíduo para o problema das caixas binárias
    
    Args:
        n: número de genes do indivíduo
    
    Return:
        Lista com n genes, onde cada gene é um valor entre 0 e 100
    """
    individuo = []
    
    for _ in range(n):
        gene = gene_cnb(valor_max_caixa)
        individuo.append(gene)
    
    return individuo

def individuo_senha(tamanho_senha, letras):
    """Cria um candidato para o problema da senha
    
    Args:
        tamanho_senha: inteiro que representa o tamanho da senha
        letras: letras disponíveis para serem sorteadas
    
    Return:
        Lista com n letras sorteadas
    """
    
    candidato = []
    
    for n in range(tamanho_senha):
        candidato.append(gene_letras(letras))
    
    return candidato

def individuo_cv(cidades):
    """Sorteia um caminho possível no problema do caixeiro viajante

    Args:
      cidades:
        Dicionário onde as chaves são os nomes das cidades e os valores são as
        coordenadas das cidades.

    Return:
      Retorna uma lista de nomes de cidades formando um caminho onde visitamos
      cada cidade apenas uma vez.
    """
    
    nomes = list(cidades.keys())
    random.shuffle(nomes)
    return nomes

###############################################################################
#                                  População                                  #
###############################################################################

def populacao_cb(tamanho, n):
    """Cria uma população no problema das caixas binárias
    
    Args:
        tamanho: tamanho da população
        n: número de genes de um indivíduo
    
    Return:
        Uma lista onde cada item é um indivíduo. Um indivíduo é uma lista com n genes
    """
    populacao = []
    
    for _ in range(tamanho):
        populacao.append(individuo_cb(n))
    
    return populacao

def populacao_cnb(tamanho, n, valor_max_caixa):
    """Cria uma população no problema das caixas binárias
    
    Args:
        tamanho: tamanho da população
        n: número de genes de um indivíduo
    
    Return:
        Uma lista onde cada item é um indivíduo. Um indivíduo é uma lista com n genes
    """
    populacao = []
    
    for _ in range(tamanho):
        populacao.append(individuo_cnb(n,valor_max_caixa))
    
    return populacao

def populacao_inicial_senha(tamanho, tamanho_senha, letras):
    """Cria uma população inicial no problema da senha
    
    Args:
        tamanho: tamanho da população
        tamanho_senha: inteiro representando o tamanho da senha
        letras: letras possíveis a serem sorteadas
    
    Return:
        Lista com todos os indivíduos da população no problema da senha
    """
    
    populacao = []
    for n in range(tamanho):
        populacao.append(individuo_senha(tamanho_senha, letras))
    
    return populacao

def populacao_inicial_cv(tamanho, cidades):
    """Cria população inicial no problema do caixeiro viajante.

    Args
      tamanho:
        Tamanho da população.
      cidades:
        Dicionário onde as chaves são os nomes das cidades e os valores são as
        coordenadas das cidades.

    Returns:
      Lista com todos os indivíduos da população no problema do caixeiro
      viajante.
    """
    populacao = []
    for _ in range(tamanho):
        populacao.append(individuo_cv(cidades))
    return populacao

###############################################################################
#                                   Seleção                                   #
###############################################################################

def selecao_roleta_max(populacao,fitness):
    """Seleciona indivíduos de uma população usando o método da roleta
    
    Nota: apenas funciona para problemas de maximização
    
    Args:
        populacao: lista com todos os indivíduos da população
        fitness: lista com o valor da funcao objetivo dos individuos
    
    Return:
        População dos indivíduos selecionados
    """
    populacao_selecionada = random.choices(populacao,weights=fitness,k=len(populacao))
    
    return populacao_selecionada


def selecao_torneio_min(populacao, fitness, tamanho_torneio=3):
    """Faz a seleção de uma população usando torneio
    
    Args:
        populacao: população do problema
        fitness: lista com o valor da funcao objetivo dos individuos
        tamanho_torneio: quantidade de indivíduos que batalham entre si
    
    Return:
        Indivíduos selecionados. Lista com os indivíduos selecionados com o mesmo tamanho do argumento 'populacao'.
    """
    
    selecionados = []
    
    par_populacao_fitness = list(zip(populacao, fitness))
    
    for _ in range(len(populacao)):
        """
        É interessante perceber que, caso o tamanho do torneio seja a população total,
        sempre o mesmo indivíduo seria escolhido, criando uma lista com o mesmo elemento
        """
        combatentes = random.sample(par_populacao_fitness, tamanho_torneio)
        
        minimo_fitness = float('inf')
        
        for par_individuo_fitness in combatentes:
            individuo = par_individuo_fitness[0]
            fit = par_individuo_fitness[1]
            
            if fit < minimo_fitness:
                selecionado = individuo
                minimo_fitness = fit
        
        
        """
        Corre o risco de selecionar o mesmo indivíduo mais de uma vez, porque a população não deixa de ser a mesma
        Entretanto, isso não é algo ruim, uma vez que, se selecionar os melhores indivíduos mais de uma vez,
        ainda vai acontecer o cruzamento, podendo ocasionar em uma melhoria ainda maior
        """
        
        selecionados.append(selecionado)
    
    return selecionados

###############################################################################
#                                  Cruzamento                                 #
###############################################################################

def cruzamento_ponto_simples(pai,mae):
    """Operador de cruzamento de ponto simples
    
    Args:
        pai: uma lista representando um indivíduo
        mae: uma lista representando um indivíduo
    
    Return:
        Duas listas, sendo que cada uma representa um filho dos pais que foram os argumentos
    """
    
    # Se começasse no zero, ou seja, no primeiro índice da lista, não existira mistura
    # assim como se fosse possível pegar o último item da lista
    
    ponto_de_corte = random.randint(1,len(pai)-1)
    
    filho1 = pai[:ponto_de_corte] + mae[ponto_de_corte:]
    filho2 = mae[:ponto_de_corte] + pai[ponto_de_corte:]
    
    return filho1, filho2

def cruzamento_ordenado(pai, mae):
    """Operador de cruzamento ordenado.

    Neste cruzamento, os filhos mantém os mesmos genes que seus pais tinham,
    porém em uma outra ordem. Trata-se de um tipo de cruzamento útil para
    problemas onde a ordem dos genes é importante e não podemos alterar os genes
    em si. É um cruzamento que pode ser usado no problema do caixeiro viajante.

    Ver pág. 37 do livro do Wirsansky.

    Args:
      pai: uma lista representando um individuo
      mae : uma lista representando um individuo

    Returns:
      Duas listas, sendo que cada uma representa um filho dos pais que foram os
      argumentos. Estas listas mantém os genes originais dos pais, porém altera
      a ordem deles
    """
    
    corte1 = random.randint(0, len(pai)-2)
    corte2 = random.randint(corte1 + 1, len(pai)-1)
    
    filho1 = pai[corte1:corte2]
    
    for gene in mae:
        if gene not in filho1:
            filho1.append(gene)
    
    filho2 = mae[corte1:corte2]
    
    for gene in pai:
        if gene not in filho2:
            filho2.append(gene)
    
    return filho1, filho2

###############################################################################
#                                   Mutação                                   #
###############################################################################

def mutacao_cb(individuo):
    """Realiza a mutação de um gene no problema das caixas binárias
    
    Args:
        individuo: uma lista representando um indivíduo no problema das caixas binárias
    
    Return:
        Um indivíduo com um gene mutado
    """
    gene_a_ser_mutado = random.randint(0,len(individuo)-1)
    individuo[gene_a_ser_mutado] = gene_cb()
    return individuo

def mutacao_cnb(individuo, valor_max_caixa):
    """Realiza a mutação de um gene no problema das caixas não binárias
    
    Args:
        individuo: uma lista representando um indivíduo no problema das caixas binárias
    
    Return:
        Um indivíduo com um gene mutado
    """
    gene_a_ser_mutado = random.randint(0,len(individuo)-1)
    individuo[gene_a_ser_mutado] = gene_cnb(valor_max_caixa)
    return individuo

def mutacao_senha(individuo, letras):
    """Realiza a mutação de um gene no problema da senha
    
    Args:
        individuo: uma lista representando um indivíduo no problema da senha
        letras: letras possíveis de serem sorteadas
    
    Return:
        Um indivíduo (senha) com um gene mutado
    """
    gene = random.randint(0, len(individuo)-1)
    individuo[gene] = gene_letras(letras)
    return individuo

def mutacao_de_troca(individuo):
    """Troca o valor de dois genes.

    Args:
      individuo: uma lista representado um individuo.

    Return:
      O indivíduo recebido como argumento, porém com dois dos seus genes
      trocados de posição.
    """
    
    indices = list(range(len(individuo)))
    lista_sorteada = random.sample(indices, k=2)
    
    indice1 = lista_sorteada[0]
    indice2 = lista_sorteada[1]
    
    individuo[indice1], individuo[indice2] = individuo[indice2], individuo[indice1]
    
    return individuo

###############################################################################
#                         Função objetivo - indivíduos                        #
###############################################################################

def funcao_objetivo_cb(individuo):
    """Computa a função objetivo no problema das caixas binárias
    
    Args:
        individuo: lista contendo os genes do indivíduo das caixas binárias
    
    Return:
        Um valor representando a soma dos genes do indivíduo
    """
    
    # +1 para evitar o problema de fitness quando for normalizado na seleção
    
    return sum(individuo) + 1

def funcao_objetivo_cnb(individuo):
    """Computa a função objetivo no problema das caixas não-binárias.
    
    Args:
      individiuo: lista contendo os genes das caixas não-binárias
    
    Return:
      Um valor representando a soma dos genes do individuo.
    """
    return sum(individuo)

def funcao_objetivo_senha(individuo, senha_verdadeira):
    """Computa a funcao objetivo de um individuo no problema da senha
    
    Args:
      individiuo: lista contendo as letras da senha
      senha_verdadeira: a senha que você está tentando descobrir
    
    Returns:
        "Distância" entre a senha proposta e a senha verdadeira. Essa distância é medida letra por letra. Quanto mais distante uma letra for da que deveria ser, maior é essa distância.
    """
    diferenca = 0

    for letra_candidato, letra_oficial in zip(individuo, senha_verdadeira):
        diferenca = diferenca + abs(ord(letra_candidato) - ord(letra_oficial))

    return diferenca

def funcao_objetivo_cv(individuo, cidades):
    """Computa a funcao objetivo de um individuo no problema do caixeiro viajante.

    Args:
      individiuo:
        Lista contendo a ordem das cidades que serão visitadas
      cidades:
        Dicionário onde as chaves são os nomes das cidades e os valores são as
        coordenadas das cidades.

    Returns:
      A distância percorrida pelo caixeiro seguindo o caminho contido no
      `individuo`. Lembrando que após percorrer todas as cidades em ordem, o
      caixeiro retorna para a cidade original de onde começou sua viagem.
    """

    distancia = 0
    
    for posicao in range(len(individuo)-1):
        partida = cidades[individuo[posicao]]
        chegada = cidades[individuo[posicao+1]]
        
        percurso = distancia_entre_dois_pontos(partida, chegada)
        distancia = distancia + percurso
    
    # Cálculo do caminho de volta para a cidade inicial
    partida = cidades[individuo[-1]]
    chegada = cidades[individuo[0]]
    
    percurso = distancia_entre_dois_pontos(partida,chegada)
    distancia = distancia + percurso

    return distancia

def funcao_objetivo_mochila(individuo, objetos, limite, ordem_dos_nomes):
    """Computa a funcao objetivo de um candidato no problema da mochila.
    Args:
      individiuo:
        Lista binária contendo a informação de quais objetos serão selecionados.
      objetos:
        Dicionário onde as chaves são os nomes dos objetos e os valores são
        dicionários com a informação do peso e valor.
      limite:
        Número indicando o limite de peso que a mochila aguenta.
      ordem_dos_nomes:
        Lista contendo a ordem dos nomes dos objetos.
    Returns:
      Valor total dos itens inseridos na mochila considerando a penalidade para
      quando o peso excede o limite.
    """
    
    valor_mochila, peso_mochila = computa_mochila(individuo,objetos,ordem_dos_nomes)
    
    if peso_mochila > limite:
        return 0.01
    
    return valor_mochila

###############################################################################
#                         Função objetivo - população                         #
###############################################################################

def funcao_objetivo_pop_cb(populacao):
    """Calcula a função objetivo para todos os membros de uma população
    
    Args:
        populacao: lista com todos os indivíduos da população
    
    Return:
        Lista de valores representando o fitness de cada indivíduo da população
    """
    fitness = []
    
    for individuo in populacao:
        fitness.append(funcao_objetivo_cb(individuo))
    
    return fitness

def funcao_objetivo_pop_cnb(populacao):
    """Calcula a função objetivo para todos os membros de uma população
    
    Args:
        populacao: lista com todos os indivíduos da população
    
    Return:
        Lista de valores representando o fitness de cada indivíduo da população
    """
    fitness = []
    
    for individuo in populacao:
        fitness.append(funcao_objetivo_cnb(individuo))
    
    return fitness

def funcao_objetivo_pop_senha(populacao, senha_verdadeira):
    """Computa a funcao objetivo de uma populaçao no problema da senha.
    
    Args:
      populacao: lista com todos os individuos da população
      senha_verdadeira: a senha que você está tentando descobrir
    
    Return:
      Lista contendo os valores da métrica de distância entre senhas.
    """
    resultado = []

    for individuo in populacao:
        resultado.append(funcao_objetivo_senha(individuo, senha_verdadeira))

    return resultado

def funcao_objetivo_pop_cv(populacao, cidades):
    """Computa a funcao objetivo de uma população no problema do caixeiro viajante.

    Args:
      populacao: lista com todos os inviduos da população
      cidades: dicionário onde as chaves são os nomes das cidades e os valores são as
        coordenadas das cidades.

    Returns:
      Lista contendo a distância percorrida pelo caixeiro para todos os
      indivíduos da população.
    """

    resultado = []
    for individuo in populacao:
        resultado.append(funcao_objetivo_cv(individuo, cidades))

    return resultado

def funcao_objetivo_pop_mochila(populacao, objetos, limite, ordem_dos_nomes):
    """Computa a fun. objetivo de uma populacao no problema da mochila
    Args:
      populacao:
        Lista com todos os individuos da população
      objetos:
        Dicionário onde as chaves são os nomes dos objetos e os valores são
        dicionários com a informação do peso e valor.
      limite:
        Número indicando o limite de peso que a mochila aguenta.
      ordem_dos_nomes:
        Lista contendo a ordem dos nomes dos objetos.
    Returns:
      Lista contendo o valor dos itens da mochila de cada indivíduo.
    """

    resultado = []
    for individuo in populacao:
        resultado.append(
            funcao_objetivo_mochila(
                individuo, objetos, limite, ordem_dos_nomes
            )
        )

    return resultado

###############################################################################
#                         Exercício GA.09 - Liga Ternária                     #
###############################################################################

def gene_lt(valor_max):
    """Define uma quantidade em massa para um componente da liga ternária.
    
    Args:
        valor_max: o valor máximo de peso disponível para a componente da liga.
        
    Return:
        Uma massa entre 5 gramas, que é o mínimo para cada componente da liga, e a quantidade máxima total disponível.
    
    """
    
    gene = random.uniform(5,valor_max)    
    return gene

def individuo_lt(numero_genes, preco):
    """Define um indivíduo com as massas de cada um dos elementos possíveis
    
    Args:
        preco: lista que contenha todos os elementos disponíveis.
        numero_genes: quantidade de genes do indivíduo, como é a liga ternária, a constante passada deve ser 3.
    
    Return:
        Retorna o indivíduo, que é uma lista com 92 posições que represente a massa de cada um dos elementos do dicionário de elementos.
    """
    
    individuo = [0 for _ in range(len(list(preco.values())))]
    valor_maximo_massa = 100
    
    for n in range(numero_genes-1):
        cond = True
        while cond:
            index = random.randint(0,len(individuo)-1)
            
            if individuo[index] == 0:
                
                # O valor máximo de cada elemento da liga deve ser no mínimo 5
                # Por isso, devemos considerar um limite para cada elemento                
                gene = gene_lt(valor_maximo_massa-((numero_genes-n-1)*5))
                
                individuo[index] = gene
                valor_maximo_massa -= gene
                cond = False
    
    index = random.randint(0,len(individuo)-1)    
    individuo[index] = valor_maximo_massa
    
    return individuo

def populacao_inicial_lt(numero_genes, tamanho_populacao, preco):
    """Cria população inicial em que cada indivíduo é uma liga ternária.
    
    Args:
        numero_genes:  quantidade de genes do indivíduo, como é a liga ternária, a constante passada deve ser 3;
        tamanho_populacao: quantidade de indivíduos dentro da população;
        preco: lista que contenha todos os elementos disponíveis.
    
    Return:
        Retorna a população de indivíduos.
    """
    populacao = []
    for _ in range(tamanho_populacao):
        indv = individuo_lt(numero_genes,preco)
        populacao.append(indv)
    return populacao

def funcao_objetivo_lt(individuo, preco):
    """Calcula o fitness da liga ternária.
    
    Args:
        individuo: lista que contém os genes das ligas ternárias.
        preco: dicionário que contém a relação de cada elemento com seu respectivo valor (dólar por kg).
    
    Return:
        Retorna um valor que representa o fitness da liga.
    """
    valor_final = 0
    for massa, valor in zip(individuo, preco.values()):
        valor_final += massa*valor/1e3
    return valor_final

def funcao_objetivo_pop_lt(populacao, preco):
    """Calcula a função objetivo para todos os membros da população.
    
    Args:
        populacao: lista com todos os indivíduos da população;
        preco: dicionário que contém a relação de cada elemento com seu respectivo valor (dólar por kg).
    
    Return:
        Retorna a lista de valores que representa o fitness de cada elemento da população.
    """
    fitness = []
    for individuo in populacao:
        fobj = funcao_objetivo_lt(individuo, preco)
        fitness.append(fobj)
    return fitness

def cruzamento_lt(pai, mae, preco, n_genes):
    """Operador de cruzamento que mantém os valores do pai e da mãe, mutando a posição de forma aleatória.
    
    Args:
        pai: uma lista representando um indivíduo;
        mae: uma lista representando um indivíduo;
        preco: dicionário que contém a relação de elementos e preço;
        n_genes: quantidade de genes, na liga ternária, será 3.
        
    Return:
        Retorna dois filhos a partir do cruzamento
    """
    
    lista_index_pai = [index for index, valor in enumerate(pai) if valor != 0]
    lista_index_mae = [index for index, valor in enumerate(mae) if valor != 0]

    lista_valores_pai = [valor for index, valor in enumerate(pai) if valor != 0]
    lista_valores_mae = [valor for index, valor in enumerate(mae) if valor != 0]

    CHANCE_TROCA = 0.05

    filho1,filho2 = np.zeros(len(preco.values())),np.zeros(len(preco.values()))
    
    for n in range(n_genes):
        if random.random() < CHANCE_TROCA:
            aux = lista_index_pai[n]
            lista_index_pai[n] = lista_index_mae[n]
            lista_index_mae[n] = aux
    
    for index, valor in zip(lista_index_pai,lista_valores_pai):
        filho1[index] = valor

    for index, valor in zip(lista_index_mae,lista_valores_mae):
        filho2[index] = valor

    return filho1, filho2
