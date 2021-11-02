
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

    def conectar(lista_de_itens, espacador_1=" e ", espacador_2=", "):
        assert type(espacador_1) == str \
            and  type(espacador_2) == str
        texto = ""
        for i in range(0, len(lista_de_itens)):
            texto += str(lista_de_itens[i])
            if i == len(lista_de_itens) - 1:
                return texto
            elif i == len(lista_de_itens) - 2:
                texto += espacador_1
            else:
                texto += espacador_2

    def qual(lista):
        return Texto.conectar(lista, " ou ") + "?"

    def parear_listas(lista_1, lista_2, pre=False, antes="(", depois=")", \
        entre=" "):
        lista, item = [], ""
        for i in range(0, len(lista_1)):
            item_L_1, item_L_2 = str(lista_1[i]), str(lista_2[i])
            if pre == False:
                item += (item_L_1 + entre
                        + antes + item_L_2 + depois)
            else:
                item += (antes + item_L_1 + depois
                        + entre + item_L_2)
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
    
    def trocar_caracter(texto_entrada, sai=".", entra=","):
        assert len(sai) == 1 and len(entra) == 1
        texto_entrada = str(texto_entrada)
        texto_saida = ""
        for c in texto_entrada:
            if c == sai:
                texto_saida += entra
            else:
                texto_saida += c
        return texto_saida
    
    def espacar(n):
        espaco = ""
        while len(espaco) < n:
            espaco += " "
        return espaco
    
    def verificar_numero(numero):
        numero = str(numero)
        caracteres_permitidos = [
            "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ".", ","
        ]
        real = False
        numero_preparado = ""
        for c in numero:
            if c not in caracteres_permitidos:
                return False
            if c in caracteres_permitidos:
                if c in [",", "."]:
                    real = True
                    numero_preparado += "."
                else:
                    numero_preparado += c
        if real == True:
            return float(numero_preparado)
        return int(numero_preparado)

class Quimica:
    def imprimir_formula(formula):
        assert type(formula) == str
        impressao_formula = ""
        for c in range(0, len(formula)):
            codigo = ord(formula[c])
            if codigo == 48: #0
                impressao_formula += "\U00002080"
            elif codigo == 49: #1
                impressao_formula += "\U00002081"
            elif codigo == 50: #2
                impressao_formula += "\U00002082"
            elif codigo == 51: #3
                impressao_formula += "\U00002083"
            elif codigo == 52: #4
                impressao_formula += "\U00002084"
            elif codigo == 53: #5
                impressao_formula += "\U00002085"
            elif codigo == 54: #6
                impressao_formula += "\U00002086"
            elif codigo == 55: #7
                impressao_formula += "\U00002087"
            elif codigo == 56: #8
                impressao_formula += "\U00002088"
            elif codigo == 57: #9
                impressao_formula += "\U00002089"
            else:
                impressao_formula += formula[c]
        return impressao_formula