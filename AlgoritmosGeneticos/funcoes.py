def funcao_objetivo_cb(individuo):
    """Computa a função objetivo no problema das caixas binárias
    
    Args:
        individuo: lista contendo os genes do indivíduo das caixas binárias
    
    Return:
        Um valor representando a soma dos genes do indivíduo
    """
    return sum(individuo) 
