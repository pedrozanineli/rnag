## Experimentos de otimização e algoritmos genéticos

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

### Problemas resolvidos:

Abaixo são elencados os experimentos desenvolvidos até o presente momento na disciplina.

- experimento A.01 - experimento de busca aleatório para o problema das caixas binárias como forma de introduzir onde os algoritmos genéticos podem ser aplicados - entretanto, sem a aplicação de fato desses algoritmos;
- experimento A.02 - tal como desenvolvido no experimento A.01, o objetivo do A.02 também é de desenvolver o problema das caixas binárias, porém realizando uma busca em grade por meio do produto cartesiano;
- experimento A.03 - resolução do problema das caixas binárias por meio de um algoritmo genético, apoiando-se nas ideias de gene, indivíduo, população, seleção por roleta e cruzamento de ponto simples;
- experimento A.04 - resolução semelhante ao problema das caixas binárias, porém aplicado ao problema das caixas não binárias;
- experimento A.05 - problema de descoberta de senha, utilizando a seleção de torneio mínimo;