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

###############################################################################
#                                  População                                  #
###############################################################################

def populacao_cb(tamanho, n):
    """Cria uma população no problema das caixas binárias
    
    Args:
        tamanho: tamanho da população
        n: número de genes de um indivíduo
    
    Return:
        Uma lista onde cada item é um indivíduo. Um indivíduo é uma lista com n genes.
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
        Uma lista onde cada item é um indivíduo. Um indivíduo é uma lista com n genes.
    """
    populacao = []
    
    for _ in range(tamanho):
        populacao.append(individuo_cnb(n,valor_max_caixa))
    
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
        fitness.append(funcao_objetivo_cb(individuo))
    
    return fitness