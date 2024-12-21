import pytest 
import sys
import FP2425P2 as fp # <--- Change the name projectoFP to the file name with your project

class TestPublicPosicao:

    def test_1(self):
        with pytest.raises(ValueError) as excinfo:
            i1 = fp.cria_posicao('a', 21)        
        assert "cria_posicao: argumentos invalidos" == str(excinfo.value)
    
    def test_2(self):
        assert not fp.posicoes_iguais(fp.cria_posicao('a', 2), fp.cria_posicao('b', 3))

    def test_3(self):
        assert fp.posicoes_iguais(fp.cria_posicao('a', 2), fp.str_para_posicao('a2'))

    def test_4(self):
        assert fp.posicao_para_str(fp.cria_posicao('b', 3)) == 'b3'

    def test_5(self):
        i1 = fp.cria_posicao('a', 2)
        assert ('a1', 'b2', 'a3') == tuple(fp.posicao_para_str(i) for i in fp.obtem_posicoes_adjacentes(i1, 2, False))
        
    def test_6(self):
        i1 = fp.cria_posicao('a', 2)
        assert ('a1', 'b1', 'b2', 'b3', 'a3') == tuple(fp.posicao_para_str(i) for i in fp.obtem_posicoes_adjacentes(i1, 2, True))    
        
    def test_7(self):
        tup = (fp.cria_posicao('a',1), fp.cria_posicao('a',3), fp.cria_posicao('b',1), fp.cria_posicao('b',2))
        assert ('b2', 'a1', 'b1', 'a3') == tuple(fp.posicao_para_str(i) for i in fp.ordena_posicoes(tup, 2))
    
class TestCadetePosicao:
    def test_1a(self):
        with pytest.raises(ValueError) as excinfo:
            i1 = fp.cria_posicao('a', True)
        assert "cria_posicao: argumentos invalidos" == str(excinfo.value)

    def test_1b(self):
        with pytest.raises(ValueError) as excinfo:
            i1 = fp.cria_posicao(31, 3)
        assert "cria_posicao: argumentos invalidos" == str(excinfo.value)

    def test_1c(self):
        with pytest.raises(ValueError) as excinfo:
            i1 = fp.cria_posicao('ab', 3)
        assert "cria_posicao: argumentos invalidos" == str(excinfo.value)

    def test_A1(self):
        assert not fp.eh_posicao((1, 2))

    def test_A2(self):
        assert not fp.eh_posicao(('a', 2, 3))

    def test_A3(self):
        assert not fp.eh_posicao(('a', True))

    def test_A4(self):
        assert not fp.eh_posicao(('ab', 2))
    def test_A5(self):
        assert not fp.eh_posicao(('a', 11))  # Como 2<=n<=5, a linha só pode ir até 10 (=2*5)

    def test_A6(self):
        assert not fp.eh_posicao(('a', 0))  # A linha não pode ser menor que 1

    def test_A7(self):
        assert not fp.eh_posicao(('z', 2))  # Como n<=5, a linha só pode ir até j (abcdefghij => 123456789(10))

    def test_A8(self):
        assert not fp.eh_posicao_valida(('j', 10), 2)  # Se n=2, só existem 4 linhas e até à coluna d, por exemplo.
    
    def test_5a(self):
        i1 = fp.cria_posicao('a', 1)
        assert ('b1', 'a2') == tuple(fp.posicao_para_str(i) for i in fp.obtem_posicoes_adjacentes(i1, 2, False))

    def test_5b(self):
        i1 = fp.cria_posicao('d', 4)
        assert ('d3', 'c4') == tuple(fp.posicao_para_str(i) for i in fp.obtem_posicoes_adjacentes(i1, 2, False))

    def test_6a(self):
        i1 = fp.cria_posicao('d', 4)
        assert ('d3', 'c4', 'c3') == tuple(
            fp.posicao_para_str(i) for i in fp.obtem_posicoes_adjacentes(i1, 2, True))

    def test_6b(self):
        i1 = fp.cria_posicao('b', 2)
        assert ('b1', 'c1', 'c2', 'c3', 'b3', 'a3', 'a2', 'a1') == tuple(
            fp.posicao_para_str(i) for i in fp.obtem_posicoes_adjacentes(i1,2,True))



class TestPublicPedra:

    def test_1(self):
        assert  fp.eh_pedra(fp.cria_pedra_branca())

    def test_2(self):
        assert not fp.pedras_iguais(fp.cria_pedra_branca(), fp.cria_pedra_preta())

    def test_3(self):
        b, p = fp.cria_pedra_branca(), fp.cria_pedra_preta()
        assert fp.pedra_para_str(b), fp.pedra_para_str(p) == ('O', 'X')
    
    def test_4(self):
        assert not fp.eh_pedra_jogador(fp.cria_pedra_neutra())
        
    def test_5(self):
        b, p = fp.cria_pedra_branca(), fp.cria_pedra_preta()
        assert fp.pedra_para_int(b), fp.pedra_para_int(p) == (-1, 1)
             
        
        
class TestPublicTabuleiro:
    def test_1(self):
        with pytest.raises(ValueError) as excinfo:
            tab = fp.cria_tabuleiro_vazio(12)
        assert "cria_tabuleiro_vazio: argumento invalido" == str(excinfo.value)

    def test_2(self):
        assert fp.eh_tabuleiro(fp.cria_tabuleiro_vazio(2))
        
    def test_3(self):
        tab = fp.cria_tabuleiro_vazio(2)
        pos = fp.cria_posicao('c',2)
        assert fp.pedra_para_str(fp.obtem_pedra(tab, pos)) == ' '
        
    def test_4(self):
        tab = fp.cria_tabuleiro_vazio(2)
        b, p = fp.cria_pedra_branca(), fp.cria_pedra_preta()
        ib = 'c1', 'c2', 'd2', 'd3', 'd4'
        ip = 'a3', 'a4', 'b1', 'b3', 'c3'
        for i in ib: fp.coloca_pedra(tab, fp.str_para_posicao(i), b)
        for i in ip: fp.coloca_pedra(tab, fp.str_para_posicao(i), p)
        hyp = \
"""    a   b   c   d
01 [ ]-[X]-[O]-[ ]
    |   |   |   |
02 [ ]-[ ]-[O]-[O]
    |   |   |   |
03 [X]-[X]-[X]-[O]
    |   |   |   |
04 [X]-[ ]-[ ]-[O]"""

        assert fp.tabuleiro_para_str(tab) == hyp
      
    def test_5(self):
        tab = fp.cria_tabuleiro_vazio(2)
        b, p = fp.cria_pedra_branca(), fp.cria_pedra_preta()
        ib = 'c1', 'c2', 'd2', 'd3', 'd4'
        ip = 'a3', 'a4', 'b1', 'b3', 'c3'
        for i in ib: fp.coloca_pedra(tab, fp.str_para_posicao(i), b)
        for i in ip: fp.coloca_pedra(tab, fp.str_para_posicao(i), p)
        pos = fp.cria_posicao('c',3)
        ref =  (('c1', 'O'), ('c2', 'O'), ('c3', 'X'), ('c4', ' '))
        assert tuple((fp.posicao_para_str(p), fp.pedra_para_str(v)) for p, v in fp.obtem_linha_vertical(tab, pos)) == ref

    def test_6(self):
        tab = fp.cria_tabuleiro_vazio(2)
        b, p = fp.cria_pedra_branca(), fp.cria_pedra_preta()
        ib = 'c1', 'c2', 'd2', 'd3', 'd4'
        ip = 'a3', 'a4', 'b1', 'b3', 'c3'
        for i in ib: fp.coloca_pedra(tab, fp.str_para_posicao(i), b)
        for i in ip: fp.coloca_pedra(tab, fp.str_para_posicao(i), p)
        diag, anti = fp.obtem_linhas_diagonais(tab, fp.cria_posicao('c',3))
        ref_d = (('a1', ' '), ('b2', ' '), ('c3', 'X'), ('d4', 'O'))
        ref_a = (('b4', ' '), ('c3', 'X'), ('d2', 'O'))
        assert tuple((fp.posicao_para_str(p), fp.pedra_para_str(v)) for p, v in diag) == ref_d and \
            tuple((fp.posicao_para_str(p), fp.pedra_para_str(v)) for p, v in anti) == ref_a


    def test_7(self):
        tab = fp.cria_tabuleiro_vazio(2)
        b, p = fp.cria_pedra_branca(), fp.cria_pedra_preta()
        ib = 'c1', 'c2', 'd2', 'd3', 'd4'
        ip = 'a3', 'a4', 'b1', 'b3', 'c3'
        for i in ib: fp.coloca_pedra(tab, fp.str_para_posicao(i), b)
        for i in ip: fp.coloca_pedra(tab, fp.str_para_posicao(i), p)
        _ = fp.roda_tabuleiro(tab)
        assert fp.tabuleiro_para_str(tab) == \
"""    a   b   c   d
01 [X]-[O]-[ ]-[O]
    |   |   |   |
02 [ ]-[O]-[X]-[O]
    |   |   |   |
03 [ ]-[ ]-[X]-[O]
    |   |   |   |
04 [X]-[X]-[ ]-[ ]"""

    def test_8(self):
        tab = fp.cria_tabuleiro_vazio(2)
        b, p = fp.cria_pedra_branca(), fp.cria_pedra_preta()
        ib = 'c1', 'c2', 'd2', 'd3', 'd4'
        ip = 'a3', 'a4', 'b1', 'b3', 'c3'
        for i in ib: fp.coloca_pedra(tab, fp.str_para_posicao(i), b)
        for i in ip: fp.coloca_pedra(tab, fp.str_para_posicao(i), p)
        
        assert (not fp.verifica_linha_pedras(tab,fp.cria_posicao('d',1), fp.cria_pedra_branca(), 3)) and \
            fp.verifica_linha_pedras(tab,fp.cria_posicao('d',2), fp.cria_pedra_branca(), 3)
        
    def test_9(self):
        orbits = 2
        ib = 'c1', 'c2', 'd2', 'd3', 'd4'
        ip = 'a3', 'a4', 'b1', 'b3', 'c3'
        ib = tuple(fp.str_para_posicao(i) for i in ib)
        ip = tuple(fp.str_para_posicao(i) for i in ip)
        b, p = fp.cria_pedra_branca(), fp.cria_pedra_preta()
        
        tab1 = fp.cria_tabuleiro_vazio(2)

        for i in ib: fp.coloca_pedra(tab1, i, b)
        for i in ip: fp.coloca_pedra(tab1, i, p)
        
        tab2 = fp.cria_tabuleiro(2, ip, ib)
        assert fp.tabuleiros_iguais(tab1, tab2)
        
    def test_10(self):
        orbits = 2
        ib = 'c1', 'c2', 'd2', 'd3', 'd4'
        ip = 'a3', 'a4', 'b1', 'b3', 'c3'
        ib = tuple(fp.str_para_posicao(i) for i in ib)
        ip = tuple(fp.str_para_posicao(i) for i in ip)
        b, p = fp.cria_pedra_branca(), fp.cria_pedra_preta()
        
        tab1 = fp.cria_tabuleiro_vazio(2)

        for i in ib: fp.coloca_pedra(tab1, i, b)
        for i in ip: fp.coloca_pedra(tab1, i, p)
        
        _ = fp.roda_tabuleiro(tab1)
        
        tab2 = fp.cria_tabuleiro(2, ip, ib)
        assert not fp.tabuleiros_iguais(tab1, tab2)
        
    def test_11(self):
        tab = fp.cria_tabuleiro_vazio(2)
        b, p = fp.cria_pedra_branca(), fp.cria_pedra_preta()
        ib = 'c1', 'c2', 'd2', 'd3', 'd4'
        ip = 'a3', 'a4', 'b1', 'b3', 'c3'
        for i in ib: fp.coloca_pedra(tab, fp.str_para_posicao(i), b)
        for i in ip: fp.coloca_pedra(tab, fp.str_para_posicao(i), p)
        pos = fp.cria_posicao('c',3)
        ref =  (('a3', 'X'), ('b3', 'X'), ('c3', 'X'), ('d3', 'O'))
        assert tuple((fp.posicao_para_str(p), fp.pedra_para_str(v)) for p, v in fp.obtem_linha_horizontal(tab, pos)) == ref

    def test_12(self):
        tab = fp.cria_tabuleiro_vazio(2)
        b, p = fp.cria_pedra_branca(), fp.cria_pedra_preta()
        ib = 'c1', 'c2', 'd2', 'd3', 'd4'
        ip = 'a3', 'a4', 'b1', 'b3', 'c3'
        for i in ib: fp.coloca_pedra(tab, fp.str_para_posicao(i), b)
        for i in ip: fp.coloca_pedra(tab, fp.str_para_posicao(i), p)
        ref = ('b3', 'c3', 'b1', 'a3', 'a4')
        
        assert tuple(fp.posicao_para_str(pos) for pos in fp.obtem_posicoes_pedra(tab, p)) == ref


class TestCadeteTabuleiro:
    # PARA QUEM USOU LISTAS
    def test_A1(self):
        n = fp.cria_pedra_neutra()
        assert not fp.eh_tabuleiro([[n, n, n], [n, n, n], [n, n, n]])
    def test_B1(self):
        res = fp.obtem_posicoes_adjacentes(fp.cria_posicao('e', 5), 5, True)
        assert res==(('e', 4), ('f', 4), ('f', 5), ('f', 6), ('e', 6), ('d', 6), ('d', 5), ('d', 4))

    def test_linha_horizontal(self):
        t = fp.cria_tabuleiro_vazio(3)
        fp.coloca_pedra(t, fp.cria_posicao('a', 1), fp.cria_pedra_preta())
        fp.coloca_pedra(t, fp.cria_posicao('b', 1), fp.cria_pedra_preta())
        fp.coloca_pedra(t, fp.cria_posicao('c', 1), fp.cria_pedra_preta())
        assert fp.verifica_linha_pedras(t, fp.cria_posicao('b', 1), fp.cria_pedra_preta(), 3) == True

    def test_linha_vertical(self):
        t = fp.cria_tabuleiro_vazio(3)
        fp.coloca_pedra(t, fp.cria_posicao('a', 1), fp.cria_pedra_preta())
        fp.coloca_pedra(t, fp.cria_posicao('a', 2), fp.cria_pedra_preta())
        fp.coloca_pedra(t, fp.cria_posicao('a', 3), fp.cria_pedra_preta())
        assert fp.verifica_linha_pedras(t, fp.cria_posicao('a', 2), fp.cria_pedra_preta(), 3) == True

    def test_linha_diagonal(self):
        t = fp.cria_tabuleiro_vazio(3)
        fp.coloca_pedra(t, fp.cria_posicao('a', 1), fp.cria_pedra_preta())
        fp.coloca_pedra(t, fp.cria_posicao('b', 2), fp.cria_pedra_preta())
        fp.coloca_pedra(t, fp.cria_posicao('c', 3), fp.cria_pedra_preta())
        assert fp.verifica_linha_pedras(t, fp.cria_posicao('b', 2), fp.cria_pedra_preta(), 3) == True

    def test_linha_antidiagonal(self):
        t = fp.cria_tabuleiro_vazio(3)
        fp.coloca_pedra(t, fp.cria_posicao('a', 3), fp.cria_pedra_preta())
        fp.coloca_pedra(t, fp.cria_posicao('b', 2), fp.cria_pedra_preta())
        fp.coloca_pedra(t, fp.cria_posicao('c', 1), fp.cria_pedra_preta())
        assert fp.verifica_linha_pedras(t, fp.cria_posicao('b', 2), fp.cria_pedra_preta(), 3) == True

    def test_linha_incompleta(self):
        t = fp.cria_tabuleiro_vazio(3)
        fp.coloca_pedra(t, fp.cria_posicao('a', 1), fp.cria_pedra_preta())
        fp.coloca_pedra(t, fp.cria_posicao('b', 1), fp.cria_pedra_preta())
        assert fp.verifica_linha_pedras(t, fp.cria_posicao('b', 1), fp.cria_pedra_preta(), 3) == False

    def test_linha_mista(self):
        t = fp.cria_tabuleiro_vazio(3)
        fp.coloca_pedra(t, fp.cria_posicao('a', 1), fp.cria_pedra_preta())
        fp.coloca_pedra(t, fp.cria_posicao('b', 1), fp.cria_pedra_branca())
        fp.coloca_pedra(t, fp.cria_posicao('c', 1), fp.cria_pedra_preta())
        assert fp.verifica_linha_pedras(t, fp.cria_posicao('b', 1), fp.cria_pedra_preta(), 3) == False

    def test_linha_horizontal_branca(self):
        t = fp.cria_tabuleiro_vazio(3)
        fp.coloca_pedra(t, fp.cria_posicao('a', 1), fp.cria_pedra_branca())
        fp.coloca_pedra(t, fp.cria_posicao('b', 1), fp.cria_pedra_branca())
        fp.coloca_pedra(t, fp.cria_posicao('c', 1), fp.cria_pedra_branca())
        assert fp.verifica_linha_pedras(t, fp.cria_posicao('b', 1), fp.cria_pedra_branca(), 3) == True

    def test_linha_vertical_branca(self):
        t = fp.cria_tabuleiro_vazio(3)
        fp.coloca_pedra(t, fp.cria_posicao('a', 1), fp.cria_pedra_branca())
        fp.coloca_pedra(t, fp.cria_posicao('a', 2), fp.cria_pedra_branca())
        fp.coloca_pedra(t, fp.cria_posicao('a', 3), fp.cria_pedra_branca())
        assert fp.verifica_linha_pedras(t, fp.cria_posicao('a', 2), fp.cria_pedra_branca(), 3) == True

    def test_linha_diagonal_branca(self):
        t = fp.cria_tabuleiro_vazio(3)
        fp.coloca_pedra(t, fp.cria_posicao('a', 1), fp.cria_pedra_branca())
        fp.coloca_pedra(t, fp.cria_posicao('b', 2), fp.cria_pedra_branca())
        fp.coloca_pedra(t, fp.cria_posicao('c', 3), fp.cria_pedra_branca())
        assert fp.verifica_linha_pedras(t, fp.cria_posicao('b', 2), fp.cria_pedra_branca(), 3) == True

    def test_linha_antidiagonal_branca(self):
        t = fp.cria_tabuleiro_vazio(3)
        fp.coloca_pedra(t, fp.cria_posicao('a', 3), fp.cria_pedra_branca())
        fp.coloca_pedra(t, fp.cria_posicao('b', 2), fp.cria_pedra_branca())
        fp.coloca_pedra(t, fp.cria_posicao('c', 1), fp.cria_pedra_branca())
        assert fp.verifica_linha_pedras(t, fp.cria_posicao('b', 2), fp.cria_pedra_branca(), 3) == True

    def test_mais_um_teste(self):
        t = fp.cria_tabuleiro_vazio(3)
        fp.coloca_pedra(t, fp.cria_posicao('a', 1), fp.cria_pedra_preta())
        fp.coloca_pedra(t, fp.cria_posicao('b', 1), fp.cria_pedra_branca())
        fp.coloca_pedra(t, fp.cria_posicao('c', 1), fp.cria_pedra_preta())
        fp.coloca_pedra(t, fp.cria_posicao('d', 1), fp.cria_pedra_preta())

        # This should return True, but if the function does not handle boundaries correctly, it might fail.
        res = fp.verifica_linha_pedras(t, fp.cria_posicao('a', 1), fp.cria_pedra_preta(), 2)
        assert res==False

    def test_seguinte1(self):
        tab = fp.cria_tabuleiro_vazio(2)
        p = fp.cria_posicao('a', 2)
        assert fp.posicao_para_str(fp.obtem_posicao_seguinte(tab, p, False)) == 'a3'

    def test_seguinte2(self):
        tab = fp.cria_tabuleiro_vazio(2)
        p = fp.cria_posicao('a', 3)
        assert fp.posicao_para_str(fp.obtem_posicao_seguinte(tab, p, False)) == 'a4'

    def test_seguinte3(self):
        tab = fp.cria_tabuleiro_vazio(2)
        p = fp.cria_posicao('a', 4)
        assert fp.posicao_para_str(fp.obtem_posicao_seguinte(tab, p, False)) == 'b4'

    def test_seguinte4(self):
        tab = fp.cria_tabuleiro_vazio(2)
        p = fp.cria_posicao('b', 4)
        assert fp.posicao_para_str(fp.obtem_posicao_seguinte(tab, p, False)) == 'c4'

    def test_seguinte5(self):
        tab = fp.cria_tabuleiro_vazio(2)
        p = fp.cria_posicao('c', 4)
        assert fp.posicao_para_str(fp.obtem_posicao_seguinte(tab, p, False)) == 'd4'

    def test_seguinte6(self):
        tab = fp.cria_tabuleiro_vazio(2)
        p = fp.cria_posicao('d', 4)
        assert fp.posicao_para_str(fp.obtem_posicao_seguinte(tab, p, False)) == 'd3'

    def test_seguinte7(self):
        tab = fp.cria_tabuleiro_vazio(2)
        p = fp.cria_posicao('d', 3)
        assert fp.posicao_para_str(fp.obtem_posicao_seguinte(tab, p, False)) == 'd2'

    def test_seguinte8(self):
        tab = fp.cria_tabuleiro_vazio(2)
        p = fp.cria_posicao('d', 2)
        assert fp.posicao_para_str(fp.obtem_posicao_seguinte(tab, p, False)) == 'd1'

    def test_seguinte9(self):
        tab = fp.cria_tabuleiro_vazio(2)
        p = fp.cria_posicao('d', 1)
        assert fp.posicao_para_str(fp.obtem_posicao_seguinte(tab, p, False)) == 'c1'

    def test_seguinte10(self):
        tab = fp.cria_tabuleiro_vazio(2)
        p = fp.cria_posicao('c', 1)
        assert fp.posicao_para_str(fp.obtem_posicao_seguinte(tab, p, False)) == 'b1'

    def test_seguinte11(self):
        tab = fp.cria_tabuleiro_vazio(2)
        p = fp.cria_posicao('b', 1)
        assert fp.posicao_para_str(fp.obtem_posicao_seguinte(tab, p, False)) == 'a1'

    def test_seguinte12(self):
        tab = fp.cria_tabuleiro_vazio(2)
        p = fp.cria_posicao('a', 1)
        assert fp.posicao_para_str(fp.obtem_posicao_seguinte(tab, p, False)) == 'a2'


class TestPublicAdditionalFuns:
    def test_1(self):
        ib = tuple(fp.str_para_posicao(i) for i in ('c1','c2','d2','d3','d4'))
        ip = tuple(fp.str_para_posicao(i) for i in ('a3','a4','b1','b3','c3'))
        t = fp.cria_tabuleiro(2, ip, ib)
        assert (fp.eh_vencedor(t, fp.cria_pedra_preta()), fp.eh_vencedor(t, fp.cria_pedra_branca())) == (False, False)

    def test_2(self):
        ib = tuple(fp.str_para_posicao(i) for i in ('c1','c2','d2','d3','d4'))
        ip = tuple(fp.str_para_posicao(i) for i in ('a3','a4','b1','b3','c3'))
        t = fp.cria_tabuleiro(2, ip, ib)
        _ = fp.coloca_pedra(t, fp.cria_posicao('d',1), fp.cria_pedra_branca())    
        assert (fp.eh_vencedor(t, fp.cria_pedra_preta()), fp.eh_vencedor(t, fp.cria_pedra_branca())) == (False, True)
    
    def test_3(self):
        assert not fp.eh_fim_jogo(fp.cria_tabuleiro_vazio(2))
        
    def test_4(self):
        ib = tuple(fp.str_para_posicao(i) for i in ('c1','c2','d2','d3','d4'))
        ip = tuple(fp.str_para_posicao(i) for i in ('a3','a4','b1','b3','c3'))
        t = fp.cria_tabuleiro(2, ip, ib)
        _ = fp.coloca_pedra(t, fp.cria_posicao('d',1), fp.cria_pedra_branca())    
        assert fp.eh_fim_jogo(t)

    def test_5(self):
        ib = tuple(fp.str_para_posicao(i) for i in ('c1','c2','d2','d3','d4'))
        ip = tuple(fp.str_para_posicao(i) for i in ('a3','a4','b1','b3','c3'))
        t = fp.cria_tabuleiro(2, ip, ib)
        hyp_move, hyp_text = escolhe_movimento_manual_offline(t, 'd1\n')
        ref_text = "Escolha uma posicao livre:"
        ref_move =  'd1'
        assert fp.posicao_para_str(hyp_move) == ref_move and \
            ref_text == hyp_text
        
                
    def test_6(self):
        ib = tuple(fp.str_para_posicao(i) for i in ('c1','c2','d2','d3','d4'))
        ip = tuple(fp.str_para_posicao(i) for i in ('a3','a4','b1','b3','c3'))
        t = fp.cria_tabuleiro(2, ip, ib)
        hyp_move, hyp_text = escolhe_movimento_manual_offline(t, 'c1\nc3\nc4\n')
        ref_text = "Escolha uma posicao livre:Escolha uma posicao livre:Escolha uma posicao livre:"
        ref_move =  'c4'
        assert fp.posicao_para_str(hyp_move) == ref_move and \
            ref_text == hyp_text
        
    def test_7(self):
        ib = tuple(fp.str_para_posicao(i) for i in ('c1','c2','d2','d3','d4'))
        ip = tuple(fp.str_para_posicao(i) for i in ('a3','a4','b1','b3','c3'))
        t = fp.cria_tabuleiro(2, ip, ib)
        move_p = fp.escolhe_movimento_auto(t, fp.cria_pedra_preta(), 'facil')
        move_b = fp.escolhe_movimento_auto(t, fp.cria_pedra_branca(), 'facil')
        assert fp.posicao_para_str(move_p) == 'b2' and \
            fp.posicao_para_str(move_b) == 'b2' 
        
    
    def test_8(self):
        ib = tuple(fp.str_para_posicao(i) for i in ('c1','c2','d2','d3','d4'))
        ip = tuple(fp.str_para_posicao(i) for i in ('a3','a4','b1','b3','c3'))
        t = fp.cria_tabuleiro(2, ip, ib)
        move = fp.escolhe_movimento_auto(t, fp.cria_pedra_preta(), 'normal')
        assert fp.posicao_para_str(move) == 'd1'
        
    
    def test_9(self):
        ib = tuple(fp.str_para_posicao(i) for i in ('c1','c2','d2','d3','d4'))
        ip = tuple(fp.str_para_posicao(i) for i in ('a3','a4','b1','b3','c3'))
        t = fp.cria_tabuleiro(2, ip, ib)
        move = fp.escolhe_movimento_auto(t, fp.cria_pedra_branca(), 'normal')
        assert fp.posicao_para_str(move) == 'c4'
        
    def test_10(self):
        ib = tuple(fp.str_para_posicao(i) for i in ('c1','c2','d2','d3','d4'))
        ip = tuple(fp.str_para_posicao(i) for i in ('a3','a4','b1','b3','c3'))
        t = fp.roda_tabuleiro(fp.roda_tabuleiro(fp.cria_tabuleiro(2, ip, ib)))
        move = fp.escolhe_movimento_auto(t, fp.cria_pedra_preta(), 'normal')
        assert fp.posicao_para_str(move) == 'd3'
        
    
    def test_11(self):
        ib = tuple(fp.str_para_posicao(i) for i in ('c1','c2','d2','d3','d4'))
        ip = tuple(fp.str_para_posicao(i) for i in ('a3','a4','b1','b3','c3'))
        t = fp.roda_tabuleiro(fp.roda_tabuleiro(fp.cria_tabuleiro(2, ip, ib)))
        move = fp.escolhe_movimento_auto(t, fp.cria_pedra_branca(), 'normal')
        assert fp.posicao_para_str(move) == 'b1'
        
        
    def test_12(self):
        res, text = orbito_offline(2, 'facil', 'O',  JOGADA_PUBLIC_1)
        assert res == -1 and text == OUTPUT_PUBLIC_1

    def test_13(self):
        res, text = orbito_offline(2, 'normal', 'X', JOGADA_PUBLIC_2)
        assert res ==0 and text == OUTPUT_PUBLIC_2

    def test_14(self):
        res, text = orbito_offline(2, '2jogadores', 'X', JOGADA_PUBLIC_3)
        assert res == 1 and text == OUTPUT_PUBLIC_3


### AUXILIAR CODE NECESSARY TO REPLACE STANDARD INPUT 
class ReplaceStdIn:
    def __init__(self, input_handle):
        self.input = input_handle.split('\n')
        self.line = 0

    def readline(self):
        if len(self.input) == self.line:
            return ''
        result = self.input[self.line]
        self.line += 1
        return result

class ReplaceStdOut:
    def __init__(self):
        self.output = ''

    def write(self, s):
        self.output += s
        return len(s)

    def flush(self):
        return 


def escolhe_movimento_manual_offline(tab, input_jogo):
    oldstdin = sys.stdin
    sys.stdin = ReplaceStdIn(input_handle=input_jogo)
    
    oldstdout, newstdout = sys.stdout,  ReplaceStdOut()
    sys.stdout = newstdout

    try:
        res = fp.escolhe_movimento_manual(tab)
        text = newstdout.output
        return res, text
    except ValueError as e:
        raise e
    finally:
        sys.stdin = oldstdin
        sys.stdout = oldstdout


def orbito_offline(orbits, lvl, jog, input_jogo):
    oldstdin = sys.stdin
    sys.stdin = ReplaceStdIn(input_handle=input_jogo)
    
    oldstdout, newstdout = sys.stdout,  ReplaceStdOut()
    sys.stdout = newstdout

    try:
        res = fp.orbito(orbits, lvl, jog)
        text = newstdout.output
        return res, text
    except ValueError as e:
        raise e
    finally:
        sys.stdin = oldstdin
        sys.stdout = oldstdout

JOGADA_PUBLIC_1 = 'd1\nc1\nb1\nb4\n'
OUTPUT_PUBLIC_1 = \
"""Bem-vindo ao ORBITO-2.
Jogo contra o computador (facil).
O jogador joga com 'O'.
    a   b   c   d
01 [ ]-[ ]-[ ]-[ ]
    |   |   |   |
02 [ ]-[ ]-[ ]-[ ]
    |   |   |   |
03 [ ]-[ ]-[ ]-[ ]
    |   |   |   |
04 [ ]-[ ]-[ ]-[ ]
Turno do computador (facil):
    a   b   c   d
01 [ ]-[ ]-[ ]-[ ]
    |   |   |   |
02 [ ]-[ ]-[ ]-[ ]
    |   |   |   |
03 [ ]-[X]-[ ]-[ ]
    |   |   |   |
04 [ ]-[ ]-[ ]-[ ]
Turno do jogador.
Escolha uma posicao livre:    a   b   c   d
01 [ ]-[ ]-[O]-[ ]
    |   |   |   |
02 [ ]-[ ]-[ ]-[ ]
    |   |   |   |
03 [ ]-[ ]-[X]-[ ]
    |   |   |   |
04 [ ]-[ ]-[ ]-[ ]
Turno do computador (facil):
    a   b   c   d
01 [ ]-[O]-[ ]-[ ]
    |   |   |   |
02 [ ]-[ ]-[X]-[ ]
    |   |   |   |
03 [ ]-[X]-[ ]-[ ]
    |   |   |   |
04 [ ]-[ ]-[ ]-[ ]
Turno do jogador.
Escolha uma posicao livre:    a   b   c   d
01 [O]-[O]-[ ]-[ ]
    |   |   |   |
02 [ ]-[X]-[ ]-[ ]
    |   |   |   |
03 [ ]-[ ]-[X]-[ ]
    |   |   |   |
04 [ ]-[ ]-[ ]-[ ]
Turno do computador (facil):
    a   b   c   d
01 [O]-[ ]-[ ]-[ ]
    |   |   |   |
02 [O]-[X]-[X]-[ ]
    |   |   |   |
03 [ ]-[X]-[ ]-[ ]
    |   |   |   |
04 [ ]-[ ]-[ ]-[ ]
Turno do jogador.
Escolha uma posicao livre:    a   b   c   d
01 [O]-[ ]-[ ]-[ ]
    |   |   |   |
02 [O]-[X]-[ ]-[ ]
    |   |   |   |
03 [O]-[X]-[X]-[ ]
    |   |   |   |
04 [ ]-[ ]-[ ]-[ ]
Turno do computador (facil):
    a   b   c   d
01 [ ]-[ ]-[ ]-[ ]
    |   |   |   |
02 [O]-[X]-[X]-[ ]
    |   |   |   |
03 [O]-[X]-[X]-[ ]
    |   |   |   |
04 [O]-[ ]-[ ]-[ ]
Turno do jogador.
Escolha uma posicao livre:    a   b   c   d
01 [ ]-[ ]-[ ]-[ ]
    |   |   |   |
02 [ ]-[X]-[X]-[ ]
    |   |   |   |
03 [O]-[X]-[X]-[ ]
    |   |   |   |
04 [O]-[O]-[O]-[ ]
Turno do computador (facil):
    a   b   c   d
01 [ ]-[ ]-[ ]-[ ]
    |   |   |   |
02 [X]-[X]-[X]-[ ]
    |   |   |   |
03 [ ]-[X]-[X]-[ ]
    |   |   |   |
04 [O]-[O]-[O]-[O]
VITORIA
"""

JOGADA_PUBLIC_2 = "c2\na3\nb2\na2\na3\na2\nb1\n"
OUTPUT_PUBLIC_2 = \
"""Bem-vindo ao ORBITO-2.
Jogo contra o computador (normal).
O jogador joga com 'X'.
    a   b   c   d
01 [ ]-[ ]-[ ]-[ ]
    |   |   |   |
02 [ ]-[ ]-[ ]-[ ]
    |   |   |   |
03 [ ]-[ ]-[ ]-[ ]
    |   |   |   |
04 [ ]-[ ]-[ ]-[ ]
Turno do jogador.
Escolha uma posicao livre:    a   b   c   d
01 [ ]-[ ]-[ ]-[ ]
    |   |   |   |
02 [ ]-[X]-[ ]-[ ]
    |   |   |   |
03 [ ]-[ ]-[ ]-[ ]
    |   |   |   |
04 [ ]-[ ]-[ ]-[ ]
Turno do computador (normal):
    a   b   c   d
01 [ ]-[ ]-[ ]-[ ]
    |   |   |   |
02 [ ]-[O]-[ ]-[ ]
    |   |   |   |
03 [ ]-[X]-[ ]-[ ]
    |   |   |   |
04 [ ]-[ ]-[ ]-[ ]
Turno do jogador.
Escolha uma posicao livre:    a   b   c   d
01 [ ]-[ ]-[ ]-[ ]
    |   |   |   |
02 [ ]-[ ]-[ ]-[ ]
    |   |   |   |
03 [ ]-[O]-[X]-[ ]
    |   |   |   |
04 [X]-[ ]-[ ]-[ ]
Turno do computador (normal):
    a   b   c   d
01 [ ]-[ ]-[ ]-[ ]
    |   |   |   |
02 [ ]-[ ]-[X]-[ ]
    |   |   |   |
03 [ ]-[O]-[O]-[ ]
    |   |   |   |
04 [ ]-[X]-[ ]-[ ]
Turno do jogador.
Escolha uma posicao livre:    a   b   c   d
01 [ ]-[ ]-[ ]-[ ]
    |   |   |   |
02 [ ]-[X]-[O]-[ ]
    |   |   |   |
03 [ ]-[X]-[O]-[ ]
    |   |   |   |
04 [ ]-[ ]-[X]-[ ]
Turno do computador (normal):
    a   b   c   d
01 [ ]-[ ]-[ ]-[ ]
    |   |   |   |
02 [O]-[O]-[O]-[ ]
    |   |   |   |
03 [ ]-[X]-[X]-[ ]
    |   |   |   |
04 [ ]-[ ]-[ ]-[X]
Turno do jogador.
Escolha uma posicao livre:Escolha uma posicao livre:    a   b   c   d
01 [ ]-[ ]-[ ]-[ ]
    |   |   |   |
02 [ ]-[O]-[X]-[ ]
    |   |   |   |
03 [O]-[O]-[X]-[X]
    |   |   |   |
04 [X]-[ ]-[ ]-[ ]
Turno do computador (normal):
    a   b   c   d
01 [ ]-[ ]-[ ]-[ ]
    |   |   |   |
02 [ ]-[X]-[X]-[X]
    |   |   |   |
03 [O]-[O]-[O]-[ ]
    |   |   |   |
04 [O]-[X]-[ ]-[ ]
Turno do jogador.
Escolha uma posicao livre:    a   b   c   d
01 [ ]-[ ]-[ ]-[X]
    |   |   |   |
02 [ ]-[X]-[O]-[ ]
    |   |   |   |
03 [X]-[X]-[O]-[ ]
    |   |   |   |
04 [O]-[O]-[X]-[ ]
Turno do computador (normal):
    a   b   c   d
01 [ ]-[ ]-[X]-[ ]
    |   |   |   |
02 [O]-[O]-[O]-[ ]
    |   |   |   |
03 [ ]-[X]-[X]-[ ]
    |   |   |   |
04 [X]-[O]-[O]-[X]
Turno do jogador.
Escolha uma posicao livre:    a   b   c   d
01 [X]-[X]-[ ]-[ ]
    |   |   |   |
02 [ ]-[O]-[X]-[ ]
    |   |   |   |
03 [O]-[O]-[X]-[X]
    |   |   |   |
04 [ ]-[X]-[O]-[O]
Turno do computador (normal):
    a   b   c   d
01 [X]-[ ]-[ ]-[ ]
    |   |   |   |
02 [X]-[X]-[X]-[X]
    |   |   |   |
03 [O]-[O]-[O]-[O]
    |   |   |   |
04 [O]-[ ]-[X]-[O]
EMPATE
"""

JOGADA_PUBLIC_3 = "a1\nb2\na4\nc4\na4\nb3\nb4\na3\n"
OUTPUT_PUBLIC_3 = \
"""Bem-vindo ao ORBITO-2.
Jogo para dois jogadores.
    a   b   c   d
01 [ ]-[ ]-[ ]-[ ]
    |   |   |   |
02 [ ]-[ ]-[ ]-[ ]
    |   |   |   |
03 [ ]-[ ]-[ ]-[ ]
    |   |   |   |
04 [ ]-[ ]-[ ]-[ ]
Turno do jogador 'X'.
Escolha uma posicao livre:    a   b   c   d
01 [ ]-[ ]-[ ]-[ ]
    |   |   |   |
02 [X]-[ ]-[ ]-[ ]
    |   |   |   |
03 [ ]-[ ]-[ ]-[ ]
    |   |   |   |
04 [ ]-[ ]-[ ]-[ ]
Turno do jogador 'O'.
Escolha uma posicao livre:    a   b   c   d
01 [ ]-[ ]-[ ]-[ ]
    |   |   |   |
02 [ ]-[ ]-[ ]-[ ]
    |   |   |   |
03 [X]-[O]-[ ]-[ ]
    |   |   |   |
04 [ ]-[ ]-[ ]-[ ]
Turno do jogador 'X'.
Escolha uma posicao livre:    a   b   c   d
01 [ ]-[ ]-[ ]-[ ]
    |   |   |   |
02 [ ]-[ ]-[ ]-[ ]
    |   |   |   |
03 [ ]-[ ]-[O]-[ ]
    |   |   |   |
04 [X]-[X]-[ ]-[ ]
Turno do jogador 'O'.
Escolha uma posicao livre:    a   b   c   d
01 [ ]-[ ]-[ ]-[ ]
    |   |   |   |
02 [ ]-[ ]-[O]-[ ]
    |   |   |   |
03 [ ]-[ ]-[ ]-[ ]
    |   |   |   |
04 [ ]-[X]-[X]-[O]
Turno do jogador 'X'.
Escolha uma posicao livre:    a   b   c   d
01 [ ]-[ ]-[ ]-[ ]
    |   |   |   |
02 [ ]-[O]-[ ]-[ ]
    |   |   |   |
03 [ ]-[ ]-[ ]-[O]
    |   |   |   |
04 [ ]-[X]-[X]-[X]
Turno do jogador 'O'.
Escolha uma posicao livre:    a   b   c   d
01 [ ]-[ ]-[ ]-[ ]
    |   |   |   |
02 [ ]-[ ]-[ ]-[O]
    |   |   |   |
03 [ ]-[O]-[O]-[X]
    |   |   |   |
04 [ ]-[ ]-[X]-[X]
Turno do jogador 'X'.
Escolha uma posicao livre:    a   b   c   d
01 [ ]-[ ]-[ ]-[O]
    |   |   |   |
02 [ ]-[ ]-[O]-[X]
    |   |   |   |
03 [ ]-[ ]-[O]-[X]
    |   |   |   |
04 [ ]-[ ]-[X]-[X]
Turno do jogador 'O'.
Escolha uma posicao livre:    a   b   c   d
01 [ ]-[ ]-[O]-[X]
    |   |   |   |
02 [ ]-[O]-[O]-[X]
    |   |   |   |
03 [ ]-[ ]-[ ]-[X]
    |   |   |   |
04 [O]-[ ]-[ ]-[X]
VITORIA DO JOGADOR 'X'
"""