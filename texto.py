
class Texto:
    def adicionar_separador(numero, posicao_do_final=4, separador="-"):
        numero = str(numero)
        if len(numero) <= posicao_do_final:
            return numero + separador
        else:      
            texto_separado = ""
            for i in range(0, len(numero)):
                texto_separado += numero[i]
                if i == len(numero) - (posicao_do_final + 1):
                    texto_separado += separador
        return texto_separado

    def conectar(lista_de_itens, conjuncao="e"):
        conjuncao = str(conjuncao)
        texto = ""
        for i in range(0, len(lista_de_itens)):
            texto += str(lista_de_itens[i])
            if i == len(lista_de_itens) - 1:
                return texto
            elif i == len(lista_de_itens) - 2:
                texto += (" " + conjuncao + " ")
            else:
                texto += ", "

    def qual(lista):
        return Texto.conectar(lista, "ou") + "?"

    def parear_listas(lista_1, lista_2, impressao_formula=False, a="(", d=")", e=" "):
        lista, item = [], ""
        for i in range(0, len(lista_1)):
            item_L_1, item_L_2 = str(lista_1[i]), str(lista_2[i])
            if impressao_formula == False:
                item += (item_L_1 + e
                        + a + item_L_2 + d)
            else:
                item += (a + item_L_1 + d
                        + e + item_L_2)
            lista.append(item)
            item = ""
        return lista

    def reter_numeros(texto, literal=False):
        tipo = type(texto)
        if tipo == int or tipo == bool:
            return texto
        inteiro = ""
        for c in str(texto):
            if 48 <= ord(c) <= 57:
                inteiro += c
        if inteiro == "":
            return texto
        elif inteiro[0] == "0" and len(inteiro) != 1 or literal == True:
            return inteiro
        return int(inteiro)
    
    def obter_lista_digitos(numero, limite=False):
        numero = str(numero)
        if limite == False:
            limite = len(numero)
        lista_digitos = []
        for i in range(0, limite):
            lista_digitos.append(int(numero[i]))
        return lista_digitos
    
class Quimica:
    def imprimir_formula(formula):
        impressao_formula = ""
        assert type(formula) == str
        for c in formula:
            if ord(c) == 48: #0
                impressao_formula += "\U00002080"
            elif ord(c) == 49: #1
                impressao_formula += "\U00002081"
            elif ord(c) == 50: #2
                impressao_formula += "\U00002082"
            elif ord(c) == 51: #3
                impressao_formula += "\U00002083"
            elif ord(c) == 52: #4
                impressao_formula += "\U00002084"
            elif ord(c) == 53: #5
                impressao_formula += "\U00002085"
            elif ord(c) == 54: #6
                impressao_formula += "\U00002086"
            elif ord(c) == 55: #7
                impressao_formula += "\U00002087"
            elif ord(c) == 56: #8
                impressao_formula += "\U00002088"
            elif ord(c) == 57: #9
                impressao_formula += "\U00002089"
            else:
                impressao_formula += c.upper()
        return impressao_formula