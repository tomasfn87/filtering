import pytest
import texto

class TestTexto:
    @pytest.fixture
    def T(self):
        return texto.Texto
    @pytest.fixture
    def C(self):
        return texto.Cpf

# Class Texto
    @pytest.mark.parametrize("numero, resultado", [
        (987654321,   "98765-4321"),
        (999123456,   "99912-3456"),
        (12345,       "1-2345"),
        ("987654321", "98765-4321"),
        ("999123456", "99912-3456"),
        ("12345",     "1-2345"),
        ("1234",      "1234-"),
        (1234,        "1234-"),
        (123,         "123-"),
        ("321",       "321-")
    ])
    def test_T_adicionar_separador_simples(self, numero, resultado, T):
        # Simples, pois não são passados nem o segundo nem o terceiro parâmetro
        assert T.adicionar_separador(numero) == resultado

    @pytest.mark.parametrize("numero, posicao, resultado", [
        (987654321,    4, "98765-4321"),
        ("987654321",  4, "98765-4321"),
        (12345,        4, "1-2345"),
        (12345,        3, "12-345"),
        (12345,        2, "123-45"),
        (12345,        5, "12345-"),
        (12345,        6, "12345-"),
        (14900800,     3, "14900-800"),
        (13200300,     3, "13200-300"),
        (12100200,     3, "12100-200"),
        ("0800123456", 6, "0800-123456"),
        ("0800122436", 6, "0800-122436"),
        ("0800112244", 6, "0800-112244")
    ])
    def test_T_adicionar_separador_intermediario(self, numero, posicao, resultado, T):
        # Intermediário, pois não é passado o terceiro parâmetro
        assert T.adicionar_separador(numero, posicao) == resultado
    
    @pytest.mark.parametrize("numero, posicao, separador, resultado", [
        ("0800123456", 6, " ", "0800 123456"),
        ("0800122436", 6, ".", "0800.122436"),
        ("0800112244", 6, "-", "0800-112244"),
        ("0800122436", 6, " ", "0800 122436"),
        ("0800122436", 6, ".", "0800.122436"),
        ("0800112244", 6, "-", "0800-112244"),
        ("tomas.nallealumni.usp.br", 13, "@@@", "tomas.nalle@@@alumni.usp.br"),
        ("tomas.nallealumni.usp.br", 13, "@",   "tomas.nalle@alumni.usp.br"),
        ("tomasfnalle@gmailcom",     3,  "...", "tomasfnalle@gmail...com"),
        ("tomasfnalle@gmailcom",     3,  ".",   "tomasfnalle@gmail.com")
    ])
    def test_T_adicionar_separador_completo(self, numero, posicao, separador, resultado, T):
        assert T.adicionar_separador(numero, posicao, separador) == resultado

    @pytest.mark.parametrize("lista, conjuncao, resultado", [
        (['Chocolate', 'manteiga',  'farinha', 'torta de morango', 'leite condensado', 'bala de goma'], "e", "Chocolate, manteiga, farinha, torta de morango, leite condensado e bala de goma"),
        ([1.1, 1.22, 1.333, 1.4444], "e", '1.1, 1.22, 1.333 e 1.4444'),
        ([1, 2, 3, 4],               "e", '1, 2, 3 e 4'),
        (['a',  'a', 'a', 'a'],      "e", 'a, a, a e a'),
        (['a', 'b', 'b', 'a', 'a'],  "e", 'a, b, b, a e a'),
        (['Chocolate', 'manteiga',  'farinha', 'torta de morango', 'leite condensado', 'bala de goma'], "ou", "Chocolate, manteiga, farinha, torta de morango, leite condensado ou bala de goma"),
        ([1.1, 1.22, 1.333, 1.4444], "ou", '1.1, 1.22, 1.333 ou 1.4444'),
        ([1, 2, 3, 4],               "ou", '1, 2, 3 ou 4'),
        (['a', 'a', 'a', 'a'],       "ou", 'a, a, a ou a'),
        (['a', 'b', 'b', 'a', 'a'],  "ou", 'a, b, b, a ou a')
    ])
    def test_T_conectar(self, lista, conjuncao, resultado, T):
        assert T.conectar(lista, conjuncao) == resultado

    @pytest.mark.parametrize("lista, resultado", [
        (['Chocolate', 'manteiga',   'farinha', 'torta de morango', 'leite condensado', 'bala de goma'], "Chocolate, manteiga, farinha, torta de morango, leite condensado ou bala de goma?"),
        ([1.1, 1.22, 1.333, 1.4444], '1.1, 1.22, 1.333 ou 1.4444?'),
        ([1, 2, 3, 4],               '1, 2, 3 ou 4?'),
        (['a',  'a', 'a', 'a'],      'a, a, a ou a?'),
        (['a', 'b', 'b', 'a', 'a'],  'a, b, b, a ou a?'),
        (["Morango", "banana"],      "Morango ou banana?"),
        (["Abacaxi"], "Abacaxi?")
    ])
    def test_T_qual(self, lista, resultado, T):
        assert T.qual(lista) == resultado

    @pytest.mark.parametrize("lista_1, lista_2, resultado", [
        (["laranja", "pera", "banana"],               [2, 3, 4],                                ['laranja (2)', 'pera (3)', 'banana (4)']),
        (["eu", "tu", "ela"],                         ["meu", "teu", "dela"],                   ['eu (meu)', 'tu (teu)', 'ela (dela)']),
        ([2, 3],                                      [20, 30],                                 ['2 (20)', '3 (30)']),
        (["iPhone", "iPad", "Macbook"],               [2000, 700, 900],                         ['iPhone (2000)', 'iPad (700)', 'Macbook (900)']),
        (["tomate", "berinjela", "batata", "cebola"], ["R$4,59", "R$3,89", "R$5,23", "R$2,54"], ['tomate (R$4,59)', 'berinjela (R$3,89)', 'batata (R$5,23)', 'cebola (R$2,54)'])
    ])
    def test_T_lista_parenteses(self, lista_1, lista_2, resultado, T):
        assert T.lista_parenteses(lista_1, lista_2) == resultado
    
    @pytest.mark.parametrize("texto, resultado", [
        ("123.456.789-01",                 12345678901),
        ("+55(11)98765-4321)",             5511987654321),
        ("!S01234567890E~^",               "01234567890"),
        ("afduhas3fdiuha2sduf1hasdjfhasd", 321),
        ("papagaio",                       "papagaio"),
        ({"nome": "arara", "tipo": "ave"}, {"nome": "arara", "tipo": "ave"}),
        ({"nome": "arara", "peso-kg": 12}, 12),
        (0,                                0),
        (1,                                1),
        (True,                             True),
        (False,                            False)
    ])
    def test_T_reter_numeros_simples(self, texto, resultado, T):
        assert T.reter_numeros(texto) == resultado
    
    @pytest.mark.parametrize("texto, literal, resultado", [
        ("1234", True,  "1234"),
        ("0123", True,  "0123"),
        ("0123", False, "0123"),
        ("0",    False, 0)
    ])
    def test_T_reter_numeros_completo(self, texto, literal, resultado, T):
        assert T.reter_numeros(texto, literal) == resultado

    
    @pytest.mark.parametrize("numero, resultado", [
        ("111444777",   [1, 1, 1, 4, 4, 4, 7, 7, 7]),
        ("11144477735", [1, 1, 1, 4, 4, 4, 7, 7, 7, 3, 5]),
        ("11144477799", [1, 1, 1, 4, 4, 4, 7, 7, 7, 9, 9]) 
    ])
    def test_T_obter_digitos_simples(self, numero, resultado, T):
        assert T.obter_digitos(numero) == resultado

    @pytest.mark.parametrize("numero, limite, resultado", [
        ("111444777",   9,  [1, 1, 1, 4, 4, 4, 7, 7, 7]),
        ("11144477735", 9,  [1, 1, 1, 4, 4, 4, 7, 7, 7]),
        ("11144477799", 11, [1, 1, 1, 4, 4, 4, 7, 7, 7, 9, 9])
    ])
    def test_T_obter_digitos_completo(self, numero, limite, resultado, T):
        assert T.obter_digitos(numero, limite) == resultado

# Class Cpf
    @pytest.mark.parametrize("cpf, resultado", [
        ("11144477799", "111.444.777-99"),
        ("11144477735", "111.444.777-35"),
        ("111444777999", False)
    ])
    def test_C_marcar(self, cpf, resultado, C):
        assert C.marcar(cpf) == resultado
    
    @pytest.mark.parametrize("digitos_cpf, resultado", [
        ([1, 1, 1, 4, 4, 4, 7, 7, 7], 3),
        ([1, 1, 1, 4, 4, 4, 7, 7, 7, 3], 5)
    ])
    def test_C_calcular_dv(self, digitos_cpf, resultado, C):
        assert C.calcular_dv(digitos_cpf) == resultado
    
    @pytest.mark.parametrize("cpf, resultado", [
        (11144477735, (3, 5)),
        (11144477799, (3, 5)),
    ])
    def test_C_obter_dvs(self, cpf, resultado, C):
        assert C.obter_dvs(cpf) == resultado
    
    @pytest.mark.parametrize("cpf, resultado", [
        (11144477735, True),
        (11144477799, False)
    ])
    def test_C_verificar(self, cpf, resultado, C):
        assert C.verificar(cpf) == resultado