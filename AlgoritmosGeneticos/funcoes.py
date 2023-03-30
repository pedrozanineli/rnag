import random

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