## Experimentos de otimização e algoritmos genéticos

### Organização dos arquivos

Abaixo são elencados os experimentos desenvolvidos até o presente momento na disciplina e demais arquivos contidos nesta pasta do repositório.

<details><summary>Experimentos desenvolvidos em aula</summary>

    <a href="https://github.com/pedrozanineli/rnag/blob/main/AlgoritmosGeneticos/experimento%20A.01%20-%20busca%20aleatoria.ipynb">Experimento A.01</a> - experimento de busca aleatório para o problema das caixas binárias como forma de introduzir onde os algoritmos genéticos podem ser aplicados, entretanto, sem a aplicação de fato desses algoritmos;

    <a href="https://github.com/pedrozanineli/rnag/blob/main/AlgoritmosGeneticos/experimento%20A.02%20-%20busca%20em%20grade.ipynb"> Experimento A.02</a> - tal como desenvolvido no experimento A.01, o objetivo do A.02 também é de desenvolver o problema das caixas binárias, porém realizando uma busca em grade por meio da aplicação do produto cartesiano;

    <a href="https://github.com/pedrozanineli/rnag/blob/main/AlgoritmosGeneticos/experimento%20A.03%20-%20algoritmo%20genetico.ipynb"> Experimento A.03</a> - resolução do problema das caixas binárias por meio de um algoritmo genético, apoiando-se nas ideias de gene, indivíduo, população, seleção por roleta e cruzamento de ponto simples;

    <a href="https://github.com/pedrozanineli/rnag/blob/main/AlgoritmosGeneticos/experimento%20A.04%20-%20caixas%20nao-binarias.ipynb"> Experimento A.04</a> - problema das caixas não binárias, com uma resolução semelhante ao problema das caixas binárias, porém com a diferença de valor máximo para as caixas;

    <a href="https://github.com/pedrozanineli/rnag/blob/main/AlgoritmosGeneticos/experimento%20A.05%20-%20descobrindo%20a%20senha.ipynb">Experimento A.05</a> - problema de minimização denominado descoberta de senha, em que uma senha deve ser advinhada ou ao menos encontrar a que se aproxime o mais próximo possível da resposta exata;

    <a href="https://github.com/pedrozanineli/rnag/blob/main/AlgoritmosGeneticos/experimento%20A.06%20-%20o%20caixeiro%20viajante.ipynb">Experimento A.06</a> - 

    <a href="">Experimento A.07</a> - experimento de maximização com restrição da mochila, em que se deve buscar levar a maior quantidade de itens possíveis de acordo com um limite de peso imposto pelo problema.

</details>

<details><summary>Experimentos desenvolvidos da lista de exercícios</summary>

    <a href="https://github.com/pedrozanineli/rnag/blob/main/AlgoritmosGeneticos/experimento%20GA.02%20-%20performance%20caixas%20binarias.ipynb">Experimento performance das caixas binárias</a> - como três algoritmos diferentes foram testados para o problema das caixas binárias, o experimento tem como objetivo a comparação de cada um deles;

    <a href="https://github.com/pedrozanineli/rnag/blob/main/AlgoritmosGeneticos/experimento%20GA.09%20-%20liga%20ternaria%20mais%20cara.ipynb">Experimento da liga ternária mais cara do mundo</a> - experimento de maximização do preço de uma liga ternária aplicando restrições de peso para cada elemento da sua composição.

</details>

<details><summary>Outros arquivos</summary>
    
    <a href="https://github.com/pedrozanineli/rnag/blob/main/AlgoritmosGeneticos/classes.py">classes.py</a> - arquivo que contém as classes que foram utilizadas no desenvolvimento dos experimentos;
    
    <a href="https://github.com/pedrozanineli/rnag/blob/main/AlgoritmosGeneticos/constantes.py">constantes.py</a> - arquivo que contém as constantes que foram utilizadas no desenvolvimento dos experimentos;
    
    <a href="https://github.com/pedrozanineli/rnag/blob/main/AlgoritmosGeneticos/funcoes.py">funcoes.py</a> - arquivo que contém as funções que foram utilizadas no desenvolvimento dos experimentos.

</details>

### O que são algoritmos genéticos?

Os problemas apresentados são resolvidos por **algoritmos genéticos**, uma classe de algoritmos que utiliza como princípio alguns conceitos da evolução Darwiniana, reprodução e seleção. Para tanto, conceitos de variação, herança e seleção são considerados.

Diferentemente de algoritmos tradicionais, essa classe mantém uma população de soluções, utiliza representações genéticas das soluções, utiliza uma função objetivo para cada problema e exibe comportamento probabilístico.


### Quando aplicar os algoritmos 

A utilização pode ser dada para problemas:

- Com complexidade de representação matemática;
- Sem representação matemática;
- Que envolvam ambiente ruídoso;
- Que envolvam um ambiente que muda ao passar do tempo.

| Vantagens      | Desvantagens |
| ----------- | ----------- |
| Otimização global do problema      | Necessidade de definições especiais       |
| Aplicação em problemas complexos   | Adequação dos hiperparâmetros        |
|  Falta de representação matemática  | Intensividade computacional        |
|  Resiliência ao ruído  | Convergência prematura        |
|  Facilidade de paralelismo  | Sem garantia de solução        |

