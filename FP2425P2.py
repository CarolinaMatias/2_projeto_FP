"""
TAD posicao
- cria_posicao: str x int → posicao
- obtem_pos_col: posicao → str
- obtem_pos_lin: posicao → int
- eh_posicao: universal → booleano
- posicoes_iguais: universal x universal → booleano
- posicao_para_str: posicao → str
- str_para_posicao: str → posicao
- eh_posicao_valida: posicao x inteiro → booleano
- obtem_posicoes_adjacentes: posicao x inteiro x booleano → tuplo
- ordena_posicoes: tuplo x inteiro → tuplo
"""
#construtor
def cria_posicao(col,lin):
    """
    cria_posicao: str x int → posicao \n
    A função recebe um caracter e um inteiro correspondentes à coluna 'col' e à \n
    linha 'lin' e devolve a posição correspondente. O construtor verifica a validade \n
    dos seus argumentos gerando uma mensagem de erro se estes forem inválidos 
    """
    
    if not isinstance(col,str) or col not in ['a','b','c','d','e','f','g','h','i','j']\
    or not type(lin)==int or not (1<=lin<=10):
        raise ValueError('cria_posicao: argumentos invalidos')
    
    pos = col + str(lin) #retorina uma string correspondente à posição
    return pos


#seletores
def obtem_pos_col(pos):
    """
    obtem_pos_col: posicao → str\n
    A função devolve a coluna da posição
    """
    return pos[0] 

def obtem_pos_lin(pos):
    """
    obtem_pos_lin: posicao → int\n
    A função devolve a linha da posição
    """
    return int(pos[1:]) #(a linha de pos pode ter um/dois números (10))


#reconhecedor
def eh_posicao(arg):
    """
    eh_posicao: universal → booleano \n
    A função devolve True caso o seu argumento seja um TAD \n
    posicao e False caso contrário.
    """
    #len(arg) entre dois e três tem em atenção tanto a posição 'a1' como a 'i10'
    return isinstance(arg,str) and len(arg) in [2,3] and \
    arg[0] in ['a','b','c','d','e','f','g','h','i','j']\
    and arg[1:].isdigit() and (1<=int(arg[1:])<=10)


#teste
def posicoes_iguais(p1,p2):
    """
    posicoes_iguais: universal x universal → booleano\n
    A função devolve True apenas se p1 e p2 são posição e são \n
    iguais, e False caso contrário.
    """
    return obtem_pos_col(p1)==obtem_pos_col(p2) and obtem_pos_lin(p1)==obtem_pos_lin(p2)


#transformador
def posicao_para_str(pos):
    """
    posicao_para_str: posicao → str\n
    A função devolve a cadeia de caracteres que representa o seu argumento
    """
    return pos

def str_para_posicao(pos):
    """
    str_para_posicao: str → posicao\n
    A função devolve a posição representada pelo seu argumento.
    """
    return pos
    

#Funções de alto nível associadas ao TAD posicao
def eh_posicao_valida(pos,n):
    """
    eh_posicao_valida: posicao x inteiro → booleano\n
    A função devolve True se pos é uma posição válida dentro do tabuleiro\n
    de Orbito-n e False caso contrário.
    """

    if eh_posicao(pos) and 2<=n<=5:
        col=obtem_pos_col(pos)
        lin=obtem_pos_lin(pos)
        i_col_pos=ord(col)-ord('a')     

        if 0<=i_col_pos<2*n and 1<=lin<=2*n: 
            return True
    return False

def obtem_posicoes_adjacentes(pos,n,d):
    """
    obtem_posicoes_adjacentes: posicao x inteiro x booleano → tuplo\n
    A função devolve um tuplo com as posições do tabuleiro\n
    de Orbito-n adjacentes à posição p se d é True, ou as posições adjacentes ortogonais\n
    se d é False. As posições do tuplo são ordenadas em sentido horário começando\n
    pela posição acima de p.
    """

    col_pos=obtem_pos_col(pos)
    lin_pos=obtem_pos_lin(pos)
    nmr_linhas=2*n
    max_colunas=chr(ord('a')+2*n-1)
    p_adj=[] 
    p_adj_ort=[] 

    #vertical superior de pos
    nova_lin=lin_pos-1
    if 1<=nova_lin<=nmr_linhas and eh_posicao_valida(cria_posicao(col_pos,nova_lin),n):
        p_adj.append(cria_posicao(col_pos,nova_lin)) #se for válido, adiciono esse valor à lista de posições adjacentes
        p_adj_ort.append(cria_posicao(col_pos,nova_lin))#e à lista de posições adjacentes ortogonais
    
    #antidiagonal direita de pos
    nova_col=chr(ord(col_pos)+1)
    if 'a'<=nova_col<=max_colunas and 1<=nova_lin<=nmr_linhas and eh_posicao_valida(cria_posicao(nova_col,nova_lin),n):
        p_adj.append(cria_posicao(nova_col,nova_lin))#se for válido, adiciono esse valor à lista de posições adjacentes
    
    #horizontal direita de pos
    if 'a'<=nova_col<=max_colunas and eh_posicao_valida(cria_posicao(nova_col,lin_pos),n):
        p_adj.append(cria_posicao(nova_col,lin_pos)) 
        p_adj_ort.append(cria_posicao(nova_col,lin_pos))
    
    #diagonal direita de pos
    nova_lin=lin_pos+1
    if 'a'<=nova_col<=max_colunas and 1<=nova_lin<=nmr_linhas and eh_posicao_valida(cria_posicao(nova_col,nova_lin),n):
        p_adj.append(cria_posicao(nova_col,nova_lin))
    
    #vertical inferior de pos
    if 1<=nova_lin<=nmr_linhas and eh_posicao_valida(cria_posicao(col_pos,nova_lin),n):
        p_adj.append(cria_posicao(col_pos,nova_lin))
        p_adj_ort.append(cria_posicao(col_pos,nova_lin))
    
    
    #antidiagonal esquerda de pos
    nova_col=chr(ord(col_pos)-1)
    if 'a'<=nova_col<=max_colunas and 1<=nova_lin<=nmr_linhas and eh_posicao_valida(cria_posicao(nova_col,nova_lin),n):
        p_adj.append(cria_posicao(nova_col,nova_lin))

    #horizontal esquerda de pos
    if 'a'<=nova_col<=max_colunas and eh_posicao_valida(cria_posicao(nova_col,lin_pos),n):
        p_adj.append(cria_posicao(nova_col,lin_pos))
        p_adj_ort.append(cria_posicao(nova_col,lin_pos))
    

    #diagonal esquerda de pos
    nova_lin=lin_pos-1
    if 'a'<=nova_col<=max_colunas and 1<=nova_lin<=nmr_linhas and eh_posicao_valida(cria_posicao(nova_col,nova_lin),n):
        p_adj.append(cria_posicao(nova_col,nova_lin))
    

    #organização das posições: de cima para baixo no sentido horário
    if d==True:
        #se d for True retorna todas as posições adjacentes
        return tuple(p_adj)
    if d==False:
        #se d for False retorna apenas as posições adjacentes ortogonais
        return tuple(p_adj_ort)
    
def ordena_posicoes(t,n):
    """
    ordena_posicoes: tuplo x inteiro → tuplo\n
    A função devolve um tuplo de posições com as mesmas posições de t\n
    ordenadas de acordo com a ordem de leitura do tabuleiro de Orbito-n.
    """
    
    def criterios_de_ordenacao(pos):
        crit1= f_chebyshev(pos,n)
        #Calcular a distância entre a posição central do tabuleiro e outra qualquer posição do tabuleiro
        #para verificar quais são as posições que estão mais próximas do meio (nas órbitas mais interiores).
        
        crit2=obtem_pos_lin(pos)
        #verifica as posições do tabuleiro de cima para baixo
        
        crit3=obtem_pos_col(pos)
        #erifica as posições da esquerda para a direita

        return(crit1,crit2,crit3)
    
    return tuple(sorted(t,key=criterios_de_ordenacao))


"""
TAD pedra
- cria_pedra_branca: {} → pedra
- cria_pedra_preta: {} → pedra
- cria_pedra_neutra: {} → pedra
- eh_pedra: universal → booleano
- eh_pedra_branca: pedra → booleano
- eh_pedra_preta: pedra → booleano
- pedras_iguais: universal x universal → booleano
- pedra_para_str: pedra → str
- eh_pedra_jogador: pedra → booleano
- pedra_para_int: pedra → int
"""
#construtores
def cria_pedra_branca():
    """
    cria_pedra_branca: {} → pedra\n
    A função devolve uma pedra pertencente ao jogador branco.
    """
    return -1

def cria_pedra_preta():
    """
    cria_pedra_preta: {} → pedra\n
    A função devolve uma pedra pertencente ao jogador preto.
    """
    return 1

def cria_pedra_neutra():
    """
    cria_pedra_neutra: {} → pedra\n
    A função devolve uma pedra neutra.
    """
    return 0
        

#reconhecedor
def eh_pedra(arg):
    """
    eh_pedra: universal → booleano\n
    A função devolve True caso o seu argumento seja um TAD pedra e False\n
    caso contrário.
    """
    return type(arg)==int and arg in [-1,0,1] 

def eh_pedra_branca(p):
    """
    eh_pedra_branca: pedra → booleano\n
    A função devolve True caso a pedra p seja do jogador branco e False\n
    caso contrário.
    """
    return p==-1
            
def eh_pedra_preta(p):           
    """
    eh_pedra_preta: pedra → booleano\n
    A função devolve True caso a pedra p seja do jogador preto e False\n
    caso contrário.
    """
    return p==1


#teste
def pedras_iguais(p1,p2):
    """
    pedras_iguais: universal x universal → booleano \n
    A função devolve True apenas se p1 e p2 são pedras e são iguais.
    """

    return eh_pedra(p1) and eh_pedra(p2) and p1==p2 


#trasnformador
def pedra_para_str(p):
    """
    pedra_para_str: pedra → str\n
    A função devolve a cadeia de caracteres que representa o jogador dono\n
    da pedra, isto é, 'O', 'X' ou ' ' para pedras do jogador branco, preto ou\n
    neutra respetivamente
    """

    if eh_pedra_branca(p):
        return 'O'
    elif eh_pedra_preta(p): 
        return 'X'
    else: 
        return ' '
        

#funções de alto nível associadas a este TAD
def eh_pedra_jogador(p):
    """
    eh_pedra_jogador: pedra → booleano\n
    A função devolve True caso a pedra p seja de um jogador e False caso\n
    contrário.
    """
    return eh_pedra_branca(p) or eh_pedra_preta(p)

def pedra_para_int(p):
    """
    pedra_para_int: pedra → int\n
    A função devolve o valor inteiro correspondente à pedra.\n
    1 para pedra preta, -1 para pedra branca, e 0 para pedra neutra.
    """
    if eh_pedra_preta(p): 
        return 1
    elif eh_pedra_branca(p):
        return -1
    else:
        return 0 


"""
TAD tabuleiro
- cria_tabuleiro_vazio: int → tabuleiro
- cria_tabuleiro: int x tuplo x tuplo → tabuleiro
- cria_copia_tabuleiro: tabuleiro → tabuleiro
- obtem_numero_orbitas: tabuleiro → int
- obtem_pedra: tabuleiro x posicao → pedra
- obtem_linha_horizontal: tabuleiro x posicao → tuplo
- obtem_linha_vertical: tabuleiro x posicao → tuplo
- obtem_linhas_diagonais: tabuleiro x posicao → tuplo x tuplo
- obtem_posicoes_pedra: tabuleiro x pedra → tuplo
- coloca_pedra: tabuleiro x posicao x pedra → tabuleiro
- remove_pedra: tabuleiro x posicao → tabuleiro
- eh_tabuleiro: universal → booleano
- tabuleiros_iguais: universal x universal → booleano
- tabuleiro_para_str: tabuleiro → str
- move_pedra: tabuleiro x posicao x posicao → tabuleiro
- obtem_posicao_seguinte: tabuleiro x posicao x booleano → posicao
- roda_tabuleiro: tabuleiro → tabuleiro
- verifica_linha_pedras: tabuleiro x posicao x pedra x int → booleano
"""
#construtores
def cria_tabuleiro_vazio(n):
    """
    cria_tabuleiro_vazio: int → tabuleiro\n
    A função devolve um tabuleiro de Orbito com n órbitas, sem \n
    posições ocupadas. O construtor verifica a validade do argumento, gerando \n
    um ValueError com a mensagem 'cria_tabuleiro_vazio: argumento \n
    invalido' caso o seu argumento não seja válido. O número \n
    mínimo de órbitas de um tabuleiro de Orbito é 2 e o máximo 5.
    """

    if not 2<=n<=5:
        raise ValueError('cria_tabuleiro_vazio: argumento invalido')

    colunas=[chr(ord('a')+i) for i in range(n*2)] 

    tabuleiro_vazio=[] 
    for lin in range(1,2*n+1): 
        nova_lin=[] 
        for col in colunas: 
            nova_lin.append(cria_pedra_neutra()) #adiciona colunas vazias à linha
        tabuleiro_vazio.append(nova_lin) #adiciona a linha vazia ao tabuleiro
    return tabuleiro_vazio

def cria_tabuleiro(n,tp,tb):
    """
    cria_tabuleiro: int x tuplo x tuplo → tabuleiro \n
    devolve um tabuleiro de Orbito com n órbitas, com as posições do tuplo tp ocupadas \n
    por pedras pretas e as posições do tuplo tb ocupadas por pedras brancas. O construtor \n 
    verifica a validade dos argumentos, gerando um ValueError com a mensagem \n
    'cria_tabuleiro: argumentos invalidos' caso os seus argumentos não sejam válidos. \n
    O número mínimo de órbitas de um tabuleiro de Orbito é 2 e o máximo 5.
    """

    if not (type(n)==int and 2<=n<=5) or not isinstance(tp, tuple) or not isinstance(tb, tuple):
        raise ValueError('cria_tabuleiro: argumentos invalidos')

    #verifica se a mesma posição não se repete mais do que uma vez dentro do mesmo tuplo
    for b in range(len(tb)):
        if tb[b] in tb[b+1:]:
            raise ValueError('cria_tabuleiro: argumentos invalidos')
    
    for p in range(len(tp)):
        if tp[p] in tp[p+1:]:
            raise ValueError('cria_tabuleiro: argumentos invalidos')

    #verifica se a mesma posição está em ambos os tuplos
    for pos in tp:
        if pos in tb:
            raise ValueError('cria_tabuleiro: argumentos invalidos')


    tabuleiro=cria_tabuleiro_vazio(n) #inicialemente o tabuleiro é vazio (antes do jogo começar)

    for pos in tp: 
        if not eh_posicao_valida(pos,n):
            raise ValueError('cria_tabuleiro: argumentos invalidos')
        else:  
            lin_pos=obtem_pos_lin(pos) 
            i_lin_pos=lin_pos-1
            col_pos=obtem_pos_col(pos) 
            i_col_pos=ord(col_pos)-ord('a')
            
            if 0<=i_lin_pos<n*2 and 0<=i_col_pos<n*2: 
                tabuleiro[i_lin_pos][i_col_pos]=cria_pedra_preta() 
                #irá substituir no tabuleiro vazio, a linha e a coluna da posição, 
                #pelo identificador da pedra preta(1)

    for pos in tb:
        if not eh_posicao_valida(pos,n):
            raise ValueError('cria_tabuleiro: argumentos invalidos')
        else:
            lin_pos=obtem_pos_lin(pos)
            i_lin_pos=lin_pos-1
            col_pos=obtem_pos_col(pos) 
            i_col_pos=ord(col_pos)-ord('a')
            
            if 0<=i_lin_pos<n*2 and 0<=i_col_pos<n*2:
                tabuleiro[i_lin_pos][i_col_pos]=cria_pedra_branca()
                #irá substituir no tabuleiro vazio, a linha e a coluna da posição, 
                #pelo identificador da pedra branca(-1)
    
    return tabuleiro

def cria_copia_tabuleiro(t):
    """
    cria_copia_tabuleiro: tabuleiro → tabuleiro \n
    A função recebe um tabuleiro e devolve uma cópia do tabuleiro.
    """
    #para cada linha que compõe o tabuleiro, a função cria uma cópia de cada linha e adiciona
    #essa nova linha a uma lista (essa lista será a cópia do tabuleiro)
    return [t[linha].copy() for linha in range(len(t))]


#seletores
def obtem_numero_orbitas(t):
    """
    obtem_numero_orbitas: tabuleiro → int\n
    A função devolve o número de órbitas do tabuleiro t.
    """
    return len(t)//2

def obtem_pedra(t,p):
    """
    obtem_pedra: tabuleiro x posicao → pedra\n
    A função devolve a pedra na posição p do tabuleiro t. Se a posição\n
    não estiver ocupada, devolve uma pedra neutra.
    """
    n=obtem_numero_orbitas(t)
    coluna_p=obtem_pos_col(p) 
    i_linha_p=obtem_pos_lin(p)-1
    i_coluna_p=ord(coluna_p)-ord('a') 
    
    if 0<=i_coluna_p<(n*2) and 0<=i_linha_p<(n*2):
        return t[i_linha_p][i_coluna_p] 

def obtem_linha_horizontal(t,p):
    """
    obtem_linha_horizontal: tabuleiro x posicao → tuplo\n
    A função devolve o tuplo formado por tuplos de dois elementos correspondentes à \n
    posição e o valor de todas as posições da linha\n
    horizontal que passa pela posição p, ordenadas de esquerda para a direita.\n
    """
    n=obtem_numero_orbitas(t)
    linha_p=obtem_pos_lin(p)
    colunas=['a','b','c','d','e','f','g','h','i','j']
    colunas=colunas[:n*2] 

    return tuple((col+str(linha_p), obtem_pedra(t,cria_posicao(col, linha_p))) for col in colunas)
   #retorna um tuplo formado de tuplos constituidos pela posição (ex.: 'a1') e pelo valor da pedra 
   #que se encontra nessa posição (ex.: 1) numa linha completa (resultado final (ex): ('a1',1) ('b1',0) ('c1',0) ('d1',-1))

def obtem_linha_vertical(t,p):
    """
    obtem_linha_vertical: tabuleiro x posicao → tuplo \n
    A função devolve o tuplo formado por tuplos de dois elementos correspondentes \n
    à posicao e o valor de todas as posições da linha vertical\n
    que passa pela posição p, ordenadas de cima para a baixo.
    """
    n=obtem_numero_orbitas(t)
    coluna_p=obtem_pos_col(p)
    return tuple((coluna_p+str(linha+1),obtem_pedra(t,cria_posicao(coluna_p,linha +1))) for linha in range(n*2))
   #retorna um tuplo formado de tuplos constituidos pela posição (ex.: 'a1') e pelo valor da pedra 
   #que se encontra nessa posição (ex.: 1) numa coluna completa (resultado final (ex): ('a1',1) ('a2',0) ('a3',0) ('a4',-1))

def obtem_linhas_diagonais(t,p):
    """
    obtem_linhas_diagonais: tabuleiro x posicao → tuplo x tuplo\n
    A função devolve dois tuplos formados cada um deles por tuplos de dois elementos correspondentes \n
    à posição e o valor de todas as posições que formam a diagonal (descendente da esquerda para a direita) \n
    e antidiagonal (ascendente da esquerda para a direita) que passam pela posição p, respetivamente.
    """
    coluna_pos=obtem_pos_col(p) 
    i_coluna=ord(coluna_pos)-ord('a') 
    linha_pos=obtem_pos_lin(p) 
    numero_linhas=obtem_numero_orbitas(t)*2 
    numero_colunas=obtem_numero_orbitas(t)*2

    diagonal=((p, obtem_pedra(t,p)),) 
    
    i,j=linha_pos-1,i_coluna-1 
    #i: linha anterior à da posição / j: índice da coluna anterior à da posição
    while i>=1 and j>=0: 
        diagonal=((cria_posicao(chr(j+ord('a')),i),obtem_pedra(t,cria_posicao(chr(j+ord('a')), i))),)+diagonal 
        #criam-se os primeiros valores da diagonal e adicionam-se estes aos início da lista das diagonais
        i-=1 
        j-=1
    
    i,j= linha_pos+1,i_coluna+1
    #i: linha seguinte à da posição / j: índice da coluna seguinte à da posição
    while i<=numero_linhas and j<numero_colunas:
        diagonal=diagonal+((cria_posicao(chr(j+ord('a')),i),obtem_pedra(t,cria_posicao(chr(j+ord('a')), i))),)
        #criam-se os seguintes valores da diagonal e adicionam-se estes aos fim da lista das diagonais
        i+=1
        j+=1

    antidiagonal=((p, obtem_pedra(t,p)),)

    i,j= linha_pos+1,i_coluna-1
    #i:linha seguinte à da posição / j:coluna anterior à da posição
    while i<=numero_linhas and j>=0:
        antidiagonal=((cria_posicao(chr(j+ord('a')),i),obtem_pedra(t,cria_posicao(chr(j+ord('a')), i))),)+antidiagonal
       #criam-se os primeiros valores da antidiagonal e adicionam-se estes aos início da lista das antidiagonais
        i+=1
        j-=1
    
    i,j= linha_pos-1,i_coluna+1
    #i: linha anterior à da posição / j: coluna seguinte à da posição
    while i>=1 and j<numero_colunas:
        antidiagonal=antidiagonal+((cria_posicao(chr(j+ord('a')),i),obtem_pedra(t,cria_posicao(chr(j+ord('a')), i))),)
        #criam-se os seguintes valores da antidiagonal e adicionam-se estes aos fim da lista das antidiagonais
        i-=1
        j+=1
    
    diagonais=diagonal,antidiagonal
    return diagonais

def obtem_posicoes_pedra(t,j):
    """
    obtem_posicoes_pedra: tabuleiro x pedra → tuplo \n
    A função devolve o tuplo formado por todas as posições do \n
    tabuleiro ocupadas por pedras j (brancas, pretas ou neutras), ordenadas em \n
    ordem de leitura do tabuleiro.
    """
    posicoes_pedra=() 
    n=obtem_numero_orbitas(t)

    for i in range(n*2): 
        for k in range(n*2):  
            if pedras_iguais(t[i][k],j): #verificamos se as pedras da linha i e coluna k do tabuleiro, são iguais ao j
                posicoes_pedra+=(cria_posicao(chr(k+ord('a')),(i+1)),) 
    
    return ordena_posicoes(posicoes_pedra,n) 


#modificadores
def coloca_pedra(t,p,j):
    """
    coloca_pedra: tabuleiro x posicao x pedra → tabuleiro\n
    A função modifica destrutivamente o tabuleiro t colocando a pedra\n
    j na posição p, e devolve o próprio tabuleiro.

    """
    i_coluna=ord(obtem_pos_col(p))-ord('a') 
    i_linha=obtem_pos_lin(p)-1 
    t[i_linha][i_coluna]=j #altera os valores da coluna e da linha diretamente no tabuleiro pela pedra 
    return t 
      
def remove_pedra(t,p):
    """
    remove_pedra: tabuleiro x posicao → tabuleiro\n
    A função modifica destrutivamente o tabuleiro p removendo a pedra\n
    da posição p, e devolve o próprio tabuleiro.
    """
    i_coluna=ord(obtem_pos_col(p))-ord('a') 
    i_linha_p=obtem_pos_lin(p)-1
    n=obtem_numero_orbitas(t)
    
    if 1<=i_linha_p<n*2 and 0<=i_coluna<n*2: 
        t[i_linha_p][i_coluna]=cria_pedra_neutra() 
        #substitui o a linha e a coluna de p (usando o indice da linha e da coluna) por uma pedra neutra
    return t


#reconhecedor   
def eh_tabuleiro(arg):
    """
    eh_tabuleiro: universal → booleano
    A função devolve True caso o seu argumento seja um TAD tabuleiro e False caso contrário.
    """
    #o tabuleiro é representado internamente uma lista de listas 
    if not isinstance(arg,list) or len(arg)==0:
        return False

    numero_colunas=len(arg)
    #como o tabuleiro é quadrado, o número de linhas e colunas é igual por isso é que faço
    #numero_colunas=len(arg), mesmo que, em teoria, 'len(arg)' seja o número de linhas
    for linha in arg: 
        if not isinstance(linha,list):
            return False
        if len(linha)!=numero_colunas:
            return False
        for coluna in linha:
            if not isinstance(coluna,int):
                return False
    return True

def tabuleiros_iguais(t1,t2):
    """
    tabuleiros_iguais: universal x universal → booleano \n
    A função devolve True apenas se t1 e t2 forem tabuleiros e forem iguais.
    """
    
    if not eh_tabuleiro(t1) or not eh_tabuleiro(t2) or obtem_numero_orbitas(t1)!=obtem_numero_orbitas(t2):
        return False
    
    n=obtem_numero_orbitas(t1)
    for i in range(n*2): 
        for j in range(n*2): 
            if not pedras_iguais(t1[i][j],t2[i][j]): 
                return False
    return True

def tabuleiro_para_str(t):
    """
    tabuleiro_para_str : tabuleiro → str
    A função devolve a cadeia de caracteres que representa o tabuleiro
    """
    n=obtem_numero_orbitas(t)
    rep_tab=' ' 
    for i in range(n*2):
        rep_tab+='   '+chr(ord('a')+i)
    rep_tab+='\n' 

    for i_linha in range(n*2):
        if i_linha+1<10: 
        #se o valor das linhas for menor que 10, adiciona um 0 antes do número (ex:01) e para no 9 para que não aconteça i010 (ex), e fique apenas i10
            rep_tab+= '0' + str(i_linha+1) + ' ' 
        #adiciona a identificação das linhas antes de cada linha (01/02...)
        else:
            rep_tab+=str(i_linha+1) + ' ' 

        for i_coluna in range(n*2):
            valor=obtem_pedra(t,cria_posicao(chr(ord('a')+i_coluna), i_linha+1)) 
            rep_tab+='['+pedra_para_str(valor)+']'
        
            if i_coluna<n*2-1: 
                rep_tab+='-' 
        
        if i_linha<n*2-1: 
            rep_tab+='\n '+'   |'*(n*2)+'\n' 
    return rep_tab


#funções de alto nível associadas ao TAD tabuleiro
def move_pedra(t,p1,p2):
    """
    move pedra: tabuleiro x posicao x posicao → tabuleiro\n
    A função modifica destrutivamente o tabuleiro t movendo a pedra da\n
    posição p1 para a posição p2, e devolve o próprio tabuleiro.\n
    """
    
    coloca_pedra(t, p2, obtem_pedra(t, p1)) 
    coloca_pedra(t, p1, cria_pedra_neutra()) #substitui o valor que estava em p1 por uma pedra neutra
    return t

def obtem_posicao_seguinte(t,p,s):
    """
    obtem posicao seguinte: tabuleiro x posicao x booleano → posicao \n
    A função devolve a posição da mesma órbita que p que se \n
    encontra a seguir no tabuleiro t em sentido horário se s for True ou anti-horário \n
    se for False
    """
    #estratégia:
    #(1) obter as posições adjacentes ortogonais a p e verificar quais destas posições se encontram também na mesma 
    #orbita de p e adicionar esses valores a uma lista (essa lista será sempre composta por apenas dois valores);
    #(2) com a função auxiliar 'primeira_coluna_orbita', obter a primeira coluna da orbita e verificar
    #se a posição se encontra nessa coluna;
    #(3) verificar se a posição se encontra na primeira linha da sua orbita 

    #Se a posição se encontrar na primeira coluna ou na primeira linha da orbita, 
    #escolhemos o primeiro valor da lista,caso se encontre nas seguintes posições 
    #da orbita, escolhe-se o segundo elemento da lista

    n=obtem_numero_orbitas(t) 
    orbita_p=obtem_orbita(p,n)
    coluna_p=obtem_pos_col(p)
    posicoes_adjacentes_p=obtem_posicoes_adjacentes(p,n,False) 
    
    posicoes_adj_orbita=[] 
    
    for pos in posicoes_adjacentes_p:
        if obtem_orbita(pos,n)==orbita_p: # se a posição adjacente se encontra na mesma orbita de p
            posicoes_adj_orbita.append(pos)
            #Esta lista está ordenada de cima para baixo e da direita para a esquerda (sentido horário)
    
    primeira_coluna_orbita_p=primeira_coluna_orbita(p,t) 
    i_primeira_coluna_orbita=ord(primeira_coluna_orbita_p)-ord('a') 
    i_linha_p=obtem_pos_lin(p)-1 
    
    if s==True: #sentido horário
        if coluna_p==primeira_coluna_orbita_p:
            return posicoes_adj_orbita[0]  
        elif i_linha_p==i_primeira_coluna_orbita:
            return posicoes_adj_orbita[0]
        else: 
            return posicoes_adj_orbita[1]
    
    if s==False: #sentido anti-horário
        if coluna_p==primeira_coluna_orbita_p: 
            return posicoes_adj_orbita[1]
        elif i_linha_p==i_primeira_coluna_orbita:
            return posicoes_adj_orbita[1]
        else: 
            return posicoes_adj_orbita[0]   

def roda_tabuleiro(t):
    """
    roda_tabuleiro: tabuleiro → tabuleiro\n
    A função modifica destrutivamente o tabuleiro t rodando todas as pedras\n
    uma posição em sentido anti-horário, e devolve o próprio tabuleiro.
    """     
    n=obtem_numero_orbitas(t)
    copia_t=cria_copia_tabuleiro(t)
    #usamos a cópia do tabuleiro como uma 'referência' para saber onde é que cada pedra estava
    #e para saber para onde é que é suposto cada pedra ir depois da rotação do tabuleiro 
    
    todas_pos_tab=todas_posicoes_tabuleiro(n)
    
    for pos in todas_pos_tab:
        pos_seguinte=obtem_posicao_seguinte(t,pos,False) 
        #obtém a posição que a pedra irá ocupar depois da rotação em sentido anti-horário
        pedra_pos=obtem_pedra(copia_t,pos)
        #vê qual é a pedra que ocupa a posição pos no tabuleiro de referência
        coloca_pedra(t,pos_seguinte,pedra_pos)
        #e coloca a pedra no 'novo tabuleiro' (tabuleiro rodado)

    return t

def verifica_linha_pedras(t,p,j,k):
    """
    verifica_linha_pedras: tabuleiro x posicao x pedra x int → booleano\n
    A função devolve True se existe pelo menos uma linha (horizontal, vertical ou diagonal)\n
    que contenha a posição p com k ou mais pedras consecutivas do jogador com \n
    pedras j, e False caso contrário.
    """
    vlrs_linhas=obtem_linha_horizontal(t,p)
    vlrs_colunas=obtem_linha_vertical(t,p)
    vlrs_diagonais=obtem_linhas_diagonais(t,p)[0]
    vlrs_antidiagonais=obtem_linhas_diagonais(t,p)[1]

    linhas=(vlrs_linhas,vlrs_colunas,vlrs_diagonais,vlrs_antidiagonais)
    
    for linha in linhas:
        pos_contada=False
        cont=0
        for e in linha:
            #verificar se as k pedras seguidas passam pela posição p
            if posicoes_iguais(e[0],p):
                pos_contada=True 
            if pedras_iguais(e[1],j):
                cont+=1    
            else:
                cont=0 
                if pos_contada:
                    pos_contada=False
                #como o contador passa a 0 (porque não existem mais peças seguidas próprias), não
                #é necessário continuar a ver se esta existem 'k peças seguidas' que passam pela posição
            if cont>=k and pos_contada:
                return True      
    return False



#Funções adicionais
def eh_vencedor(t,j):
    """
    eh_vencedor: tabuleiro x pedra → booleano \n
    É uma função auxiliar que recebe um tabuleiro e uma pedra de jogador, \n
    e devolve True se existe uma linha completa do tabuleiro de pedras do \n
    jogador ou False caso contrário.
    """
    n=obtem_numero_orbitas(t)

    todas_pos_tab=todas_posicoes_tabuleiro(n)
    for pos in todas_pos_tab:
        if verifica_linha_pedras(t,pos,j,n*2):
            return True
    return False

def eh_fim_jogo(t):
    """
    eh_fim_jogo: tabuleiro -> booleano \n
    é uma função auxiliar que recebe um tabuleiro e devolve True se o jogo\n
    já terminou ou False caso contrário.
    """
    return tabuleiro_cheio(t) or eh_vencedor(t,cria_pedra_preta()) or eh_vencedor(t,cria_pedra_branca()) 

def escolhe_movimento_manual(t):
    """
    escolhe_movimento_manual: tabuleiro → posicao \n
    é uma função auxiliar que recebe um tabuleiro t e permite escolher uma posição \n
    livre do tabuleiro onde colocar uma pedra. A função não modifica o seu argumento \n
    e devolve a posição escolhida. 
    """      
    while True:
        pos=input('Escolha uma posicao livre:')

        if 'a'<=pos[0]<='j' and pos[1:].isdigit() and 1<=int(pos[1:])<=10:
            pos_manual=str_para_posicao(pos)

            if eh_posicao(pos_manual) and pos_manual in posicoes_livres(t):
                return pos_manual
            
def escolhe_movimento_auto(t,j,lvl):
    """
    escolhe_movimento_auto: tabuleiro x pedra x str → posicao \n
    é uma função auxiliar que recebe um tabuleiro t (em que o jogo não terminou \n
    ainda), uma pedra j, e a cadeia de carateres lvl correspondente à estratégia, e \n
    devolve a posição escolhida automaticamente de acordo com a estratégia\n
    selecionada para o jogador com pedras j. A função não modifica nenhum dos seus argumentos. 
    """

    n=obtem_numero_orbitas(t)
    k=n*2

    if lvl=='facil':
        return estrategia_facil(t,j)
    if lvl=='normal':
        return estrategia_normal(t,j,k)
       
def orbito(n,modo,jog):
    """
    orbito: int x str x str → int \n
    É a função principal que permite jogar um jogo completo de Orbiton. A função recebe o \n
    número de órbitas do tabuleiro, uma cadeia de carateres que \n
    representa o modo de jogo, e a representação externa de uma pedra (preta ou branca),\n
    e devolve um inteiro identificando o jogador vencedor (1 para preto ou -1 para branco),\n
    ou 0 em caso de empate. A função gera a mensagem de erro 'orbito: argumentos invalidos' \n
    caso algum argumento recebido seja inválido\n
    \n 
    O jogo começa sempre com o jogador com pedras preta e desenvolve-se do seguinte modo:\n
    O jogo inicia-se com o tabuleiro vazio e o objetivo de cada jogador é fazer k=2*n pedras próprias seguidas.\n
    Cada turno do jogador consiste na colocação de uma pedra própria numa casa livre e na rotação\n
    de uma posição em sentido antihorário (cada pedra roda dentro de sua orbita). O jogo termina se já não existem\n
    casas livres no tabuleiro ou se algum dos jogadores obteu k=2*n pedras próprias seguidas. Se ambos\n
    os jogadores obterem k=2*n pedras próprias seguidas, o jogo termina em empate.\n
    \n
    Os modos de jogo possíveis são:\n
    \n
    'facil' ->  Jogo de um jogador contra o computador que utiliza a estratégia fácil. O jogador joga com a \n
                representação externa de jog e no fim aparece uma mensagem de 'VITORIA', 'DERROTA' ou 'EMPATE'\n
                seguido do número do jogador vencedor\n
    \n
    'normal' -> Jogo de um jogador contra o computador que utiliza a estratégia normal. O jogador joga com a \n
                representação externa de jog e no fim aparece uma mensagem de 'VITORIA', 'DERROTA' ou 'EMPATE'\n
                seguido do número do jogador vencedor\n
    \n
    '2jogadores' -> Jogo de dois jogadores e que no fim aparece uma mensagem de 'VITORIA DO JOGADOR 'X',\n
                    'VITORIA DO JOGADOR 'O' ou 'EMPATE'
    
    
    """      
    if not type(n)==int or not 2<=n<=5 or not isinstance(modo,str) or \
    modo not in ['facil','normal','2jogadores'] or not isinstance(jog,str) \
    or jog not in ['X','O']:
        raise ValueError('orbito: argumentos invalidos')

    tabuleiro=cria_tabuleiro_vazio(n) #o jogo começa com um tab vazio
    pedra_do_jogador=cria_pedra_preta() if jog=='X' else cria_pedra_branca()
    
    #mensagens do inicio do jogo
    print(f'Bem-vindo ao ORBITO-{n}.')
    if modo=='2jogadores':
        print('Jogo para dois jogadores.')
    else:
        print(f'Jogo contra o computador ({modo}).')
        print(f"O jogador joga com '{jog}'.")

    jogador_atual=cria_pedra_preta() #começa o jogador com pedra preta
    print(tabuleiro_para_str(tabuleiro))

    while not eh_fim_jogo(tabuleiro):
        pedra_do_adv=(cria_pedra_branca() if eh_pedra_preta(jogador_atual) else cria_pedra_preta())
        adv=pedra_para_str(pedra_do_adv)
        
        #jogador contra jogador
        if modo=='2jogadores':
            print(f"Turno do jogador '{pedra_para_str(jogador_atual)}'.")
            
            pos=escolhe_movimento_manual(tabuleiro)
            tabuleiro=coloca_pedra(tabuleiro,pos,jogador_atual)
            tabuleiro=roda_tabuleiro(tabuleiro)

            print(tabuleiro_para_str(tabuleiro))
            
            verifica_jog_atual=eh_vencedor(tabuleiro,jogador_atual)
            verifica_adv=eh_vencedor(tabuleiro,pedra_do_adv)
            
            if verifica_adv and verifica_jog_atual:
            #se ambos os jogadores vencerem, há um empate
                print('EMPATE')
                return 0    
            
            if verifica_jog_atual:
                print(f"VITORIA DO JOGADOR '{pedra_para_str(jogador_atual)}'")
                return pedra_para_int(jogador_atual)
            
            if verifica_adv:
                print(f"VITORIA DO JOGADOR '{adv}'")
                return pedra_para_int(pedra_do_adv)           
            
        
        else:
            #jogo do jogador humano contra o bot
            if pedras_iguais(jogador_atual,pedra_do_jogador):
                print('Turno do jogador.')
                pos=escolhe_movimento_manual(tabuleiro)
                tabuleiro=coloca_pedra(tabuleiro,pos,jogador_atual)
                tabuleiro=roda_tabuleiro(tabuleiro)
            else: 
                print(f'Turno do computador ({modo}):')
                pos=escolhe_movimento_auto(tabuleiro,jogador_atual,modo)
                tabuleiro=coloca_pedra(tabuleiro,pos,jogador_atual)
                tabuleiro=roda_tabuleiro(tabuleiro)
            
            print(tabuleiro_para_str(tabuleiro))
            
            verifica_jog_atual=eh_vencedor(tabuleiro,jogador_atual)
            verifica_adv=eh_vencedor(tabuleiro,pedra_do_adv)

            if verifica_adv and verifica_jog_atual:
                print('EMPATE')
                return 0

            if verifica_jog_atual:
            #Se for o turno do jogador humano a colocar a pedra e se verificar que existe uma
            #linha completa do tabuleiro com pedras do próprio:
                print('VITORIA' if pedras_iguais(jogador_atual,pedra_do_jogador) else 'DERROTA')
                return pedra_para_int(jogador_atual)
            
            if verifica_adv:
            #Se for o turno do jogador humano a colocar a pedra e se verificar que existe uma
            #linha completa do tabuleiro com pedras do adversário:
                print('DERROTA' if pedras_iguais(jogador_atual,pedra_do_jogador) else 'VITORIA')
                return pedra_para_int(pedra_do_adv)

        #troca o turno dos jogadores
        jogador_atual=(cria_pedra_branca() if eh_pedra_preta(jogador_atual) else cria_pedra_preta())
    
    print('EMPATE')
    return 0


    
#Funções auxiliares
def obtem_orbita(p,n):
    """
    posicao x inteiro -> inteiro \n
    A função devlve um número inteiro correspondente à orbita em que p se encontra
    """
    coluna_p=obtem_pos_col(p)
    i_coluna_p=ord(coluna_p)-ord('a')+1 #os índices das colunas começam em 1 e não em 0
    i_linha_p=obtem_pos_lin(p) #indice da linha a começar em 1 e não em 0 
    
    #obter a coluna e a linha da 'posição central' (será uma posição central 'falsa' 
    #já que o tabuleiro tem o número de colunas e linhas par):
    col_centro=(2*n+1)/2 
    lin_centro=(2*n+1)/2

    d=max(abs(lin_centro-i_linha_p),abs(col_centro-i_coluna_p))
    return int(d + 0.5)
    
def f_chebyshev(p, n):
    """
    posicao x int -> int\n
    A função recebe uma posição e calcula a distância entre a posição e o centro do tabuleiro. 
    """
    
    i_col_central=ord('a')+n-0.5
    lin_central=n+0.5 
    col_p1=obtem_pos_col(p)
    lin_p1=obtem_pos_lin(p)

    d=max(abs(lin_p1-lin_central),abs(ord(col_p1)-i_col_central))
    return d

def todas_posicoes_tabuleiro(n):
    """
    int -> lista \n
    A função recebe um inteiro correspondente ao número de orbitas e devolve a lista com\n
    todas as posições do tabuleiro
    """
    posicoes=[] 
    for i_coluna in range(n*2): 
        l_coluna=chr(ord('a')+i_coluna) #letra da coluna 
        for linha in range(1,n*2+1): 
            pos=cria_posicao(l_coluna,linha) 
            posicoes.append(pos) 
    return posicoes

def primeira_coluna_orbita(p,t):
    """
    posicao x tabuleiro -> str\n
    Esta função tem o objetivo de perceber qual é que é a menor coluna (primeira coluna) de uma dada orbital.\n
    Sabemos que a menor coluna da orbita, será aquela em que o índice da coluna no tabuleiro é menor\n
    """
    n=obtem_numero_orbitas(t)
    orbita_p=obtem_orbita(p, n)
    todas_pos_orbita=todas_posicoes_orbita(orbita_p,t)
    
    menor_coluna=obtem_pos_col(todas_pos_orbita[0]) 
    #incializamos a menor coluna (que será a primeira coluna da orbital de p) como sendo a coluna
    #da primeira posição

    for pos in todas_pos_orbita[1:]: 
    #iterar sobre as posições restantes para encontrar a menor coluna 
        col_atual=obtem_pos_col(pos)
        if col_atual<menor_coluna: 
            menor_coluna=col_atual 
    
    return menor_coluna 
    
def todas_posicoes_orbita(orbita_p,t):
    """
    int x tabuleiro -> lista \n
    A função recebe a orbita de uma posição e um tabuleiro e devolve\n
    todas as posições que estão contidas nessa orbita
    """
    n=obtem_numero_orbitas(t) 
    posicoes_tabuleiro=todas_posicoes_tabuleiro(n) 

    posicoes_orbita_p=[]
    for pos in posicoes_tabuleiro:    
        if obtem_orbita(pos,n)==orbita_p:
            posicoes_orbita_p.append(pos)
    return posicoes_orbita_p

def tabuleiro_cheio(t):
    """
    tabuleiro -> booleano\n
    Se o tabuleiro tiver alguma pedra vazia, a função retorna False, se não, retorna True
    """
    n=obtem_numero_orbitas(t)
    todas_pos_t=todas_posicoes_tabuleiro(n)

    for p in todas_pos_t:
        if pedras_iguais(obtem_pedra(t,p),cria_pedra_neutra()):
            return False
    return True

def posicoes_livres(t):
    """
    posicoes_livres: tabuleiro -> lista\n
    A função recebe um tabuleiro e devolve a lista composta por todas as posições livres do tabuleiro
    """
    n=obtem_numero_orbitas(t)
    posicoes_livres=[]
    for pos in todas_posicoes_tabuleiro(n):
        if pedras_iguais(obtem_pedra(t,pos),cria_pedra_neutra()):
            posicoes_livres.append(pos)
    return posicoes_livres

def estrategia_facil(t,j):
    """
    tabuleiro x pedra -> posição
    A função determina a posição onde a pedra deve ser jogada de acordo com a 
    descrição da estratégia fácil:
        (1) Se existir no tabuleiro pelo menos uma posição livre que no fim do turno (após
        rotação) fique adjacente a uma pedra própria, jogar numa dessas posições;
        (2) Se não, jogar numa posição livre.
    """

    n=obtem_numero_orbitas(t)
    tab=cria_copia_tabuleiro(t)
    tab=roda_tabuleiro(tab)
    pos_livres=posicoes_livres(t)
    pos_livres_ordenadas=ordena_posicoes(pos_livres,n)

    for p in pos_livres_ordenadas:
        p_rodada =obtem_posicao_seguinte(t,p,False)
        pos_ajdacentes=obtem_posicoes_adjacentes(p_rodada,n,True) #adjacentes a p apos rotacao
        for a in pos_ajdacentes:
            if pedras_iguais(j,obtem_pedra(tab,a)):
            #se, no tab rodado, alguma das adjacentes a p tiverem a mesma pedra que o jogador
                return p
            
    #caso não haja posições adjacentes a p que tenham sejam da mesma pedra que jogador        
    primeira_pos=pos_livres_ordenadas[0]  
    return primeira_pos 

def estrategia_normal(t,j,k):
    """
    tabuleiro x pedra x inteiro -> posicao \n
    A função determina qual será a posição a jogar de acordo com a estratégia normal: \n
    Determinar o maior valor de L ≤ k tal que o próprio jogador conseguir colocar L\n
    peçaas consecutivas que contenha essa jogada no fim do turno atual, ou seja, após\n
    uma rotação; ou que o conseguir o adversário no fim do seu seguinte turno, ou\n
    seja, após duas rotações. estrégia:\n
        (1) Se existir pelo menos uma posição que permita obter L pedras consecutivas próprias,\n
        jogar nessa posição\n
        (2) Se não, jogar numa poisção que impossibilite o jogador de obter L pedras consecutivas 
    """

    n=obtem_numero_orbitas(t)
    pos_livres=posicoes_livres(t)
    pos_livres_ordenadas=ordena_posicoes(pos_livres,n)   
    pos_possiveis_vitoria=[]
    pos_possiveis_bloqueio=[]
    
    for L in range(k,0,-1): 
        #diminui o valor de k até encontrar o maior L de pedras seguidas do jogador
        for pos in pos_livres_ordenadas:
            copia_tab1=cria_copia_tabuleiro(t) #copia_tab1: ver a possibilidade de o jogador conseguir L em linha
            coloca_pedra(copia_tab1,pos,j)
            roda_tabuleiro(copia_tab1)
            if verifica_linha_pedras(copia_tab1,obtem_posicao_seguinte(copia_tab1,pos,False),j,L):
                pos_possiveis_vitoria.append(pos)
                #posições que possibilitam conseguir L peças consecutivas próprias


            adv=(cria_pedra_branca() if eh_pedra_preta(j) else cria_pedra_preta())
            #troca a pedra para a pedra do adversário
            #verifica se é possível bloquear o adversário e impedir que este consiga L peças consecutivas
            copia_tab2=cria_copia_tabuleiro(t)
            coloca_pedra(copia_tab2,pos,adv)
            roda_tabuleiro(copia_tab2) 
            roda_tabuleiro(copia_tab2)
            if verifica_linha_pedras(copia_tab2,obtem_posicao_seguinte(copia_tab2,obtem_posicao_seguinte(copia_tab2,pos,False),False),adv,L):
                pos_possiveis_bloqueio.append(pos)
                #posições que impossibilitam o adversário de conseguir L peças 
                #seguidas no final do seu próximo turno
        
        if pos_possiveis_vitoria:
            return pos_possiveis_vitoria[0]     

        if pos_possiveis_bloqueio:
            return pos_possiveis_bloqueio[0] 

    return pos_livres_ordenadas[0]


t=[[1,0,-1],[1,0,0],[1,1,0]]
print(orbito(2,'2jogadores','X'))
#print(obtem_linha_vertical(t,'a2'))