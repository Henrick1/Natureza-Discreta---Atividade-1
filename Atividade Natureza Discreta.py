'''
Henrique Tetilha Golias

Enunciado:
Para  obter  os  pontos  relativos  a  este  trabalho,  você  deverá  criar  um  programa,  utilizando  a 
linguagem  Python, C, ou C++.  Este  programa,  quando  executado,  irá  apresentar  os  resultados  de 
operações que serão realizadas entre dois conjuntos de dados.  
O  programa  que  você  desenvolverá  irá  receber  como  entrada um arquivo de texto  (.txt) 
contendo vários conjuntos de dados e várias operações. Estas operações e dados estarão representadas 
em um arquivo de textos contendo apenas os dados referentes as operações que devem ser realizadas 
segundo a seguinte regra fixa: a primeira linha do arquivo de texto de entrada conterá o número de 
operações  que  estão  descritas  no  arquivo,  este  número  de  operações  será  um  inteiro;  as  linhas 
seguintes  seguirão  sempre  o  mesmo  padrão  de  três  linhas:  a  primeira  linha  apresenta  o  código  da 
operação  (U para união, I para interseção, D para diferença e C produto cartesiano),  a  segunda  e 
terceira linhas conterão os elementos dos conjuntos separados por virgulas. A seguir está um exemplo 
das linhas que podem existir em um arquivo de testes para o programa que você irá desenvolver: 
4 
U 
3, 5, 67, 7 
1, 2, 3, 4  
I 
1, 2, 3, 4, 5 
4, 5 
D 
1, A, C, 34 
A, C, D, 23 
C 
3, 4, 5, 5, A, B, R 
1, B, C, D, 1 
Neste exemplo temos 4 operações uma união (U), uma interseção (I), um diferença (D) e um 
produto cartesiano (C). A união, definida por U, deverá ser executada sobre os conjuntos {𝟑,𝟓,𝟔𝟕,𝟕} e 
{𝟏,𝟐,𝟑,𝟒}, cujos elementos estão explicitados nas linhas posteriores a definição da operção (U).  
A resposta do seu programa deverá conter a operação realizada, descrita por extenso, os dados 
dos conjuntos identificados, e o resultado da operação. No caso da união a linha de saída deverá conter 
a informação e a formatação mostrada a seguir:    
União: conjunto 1 {3,5,67,7}, conjunto 2 {1,2,3,4}. Resultado: {3,5,67,7,1,2,4}   
Seu programa deverá mostrar a saída no terminal, ou em um arquivo de textos. Em qualquer 
um dos casos, a saída será composta por uma linha de saída para cada operação constante no arquivo 
de  textos  de  entrada  formatada  segundo  o  exemplo  de  saída  acima.  Observe  as  letras  maiúsculas  e 
minúsculas, e os pontos utilizados na formatação da linha de saída apresenta acima.  
No  caso  do  texto  de  exemplo,  teremos  4  linhas,  e  apenas  4  linhas  de  saída,  formatadas  e 
pontuadas conforme o exemplo de saída acima. O uso de linhas extras na saída, ou erros de formatação, 
implicam em perda de pontos como pode ser visto na rubrica de avaliação constante neste documento. 
Para que seu programa possa ser testado você deve criar, no mínimo, três arquivos de entrada 
contendo um número diferente de operações, operações com dados diferentes, e operações em ordem 
'''
arquivo = open("operacoes.txt")
numbop = int(arquivo.readline(1))
numb = 0

def op():
    part1 = con1
    part2 = con2
    uni = []
    if line.startswith('U'):
        print('União: ' , end= '')
        print("Conjunto 1 {" , ','.join(map(str , part1)) , "}, ", sep="", end='')
        print("Conjunto 2 {" , ','.join(map(str , part2)) , "}, ", sep="", end='')
        for i in range(len(part1)):
            uni.append(part1[i])
        for i in range(len(part2)):
            if part2[i] not in uni:
                uni.append(part2[i])
        print('Resultado: {', ','.join(map(str , uni)), '}\n' ,sep="", end="")
    elif line.startswith('I'):
        inte = []
        print('Interseção: ' , end='')
        print("Conjunto 1 {" , ','.join(map(str , part1)) , "}, ", sep="", end='')
        print("Conjunto 2 {" , ','.join(map(str , part2)) , "}, ", sep="", end='')
        for i in range(len(part1)):
            if part1[i] in part2:
                inte.append(part1[i])
        print('Resultado: {' , ','.join(map(str , inte)) , "}\n" , sep="", end='')
    elif line.startswith('D'):
        dif = []
        print('Diferença: ' , end='')
        print("Conjunto 1 {" , ','.join(map(str , part1)) , "}, ", sep="", end='')
        print("Conjunto 2 {" , ','.join(map(str , part2)) , "}, ", sep="", end='')
        for i in range(len(part1)):
            if part1[i] not in part2:
                dif.append(part1[i])
        print('Resultado: {', ','.join(map(str, dif)), '}\n', sep="", end="")
    elif line.startswith('C'):
        cart = []
        print('Plano cartesiano: ' , end='')
        print("Conjunto 1 {" , ','.join(map(str , part1)) , "}, ", sep="", end='')
        print("Conjunto 2 {" , ','.join(map(str , part2)) , "}, ", sep="", end='')
        cartesiano = [(i,j) for i in part1 for j in part2]
        print('Resultado: {', ','.join(map(str, cartesiano)).replace("'","").strip(), '}', sep="")

while numb < numbop:
    for line in arquivo:
            part1 = []
            part2 = []
            final = []
            if line.startswith("U") or line.startswith("I") or line.startswith("D") or line.startswith("C"):
                con1 = []
                con2 = []
                con1 = arquivo.readline().replace(',' , '').strip().split()
                con2 = arquivo.readline().replace(',' , '').strip().split()
                op()
                numb += 1