
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

    def parear_listas(lista_1, lista_2, pre=False, a="(", d=")", e=" "):
        lista, item = [], ""
        for i in range(0, len(lista_1)):
            item_L_1, item_L_2 = str(lista_1[i]), str(lista_2[i])
            if pre == False:
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