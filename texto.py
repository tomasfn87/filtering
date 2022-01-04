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

    def reter_numeros(numero, literal=False, accept_float=False):
        real = False
        tipo = type(numero)
        assert tipo in [int, float, str]
        if tipo in [int, float]:
            return numero
        texto_numerico = ""
        for d in numero:
            if texto_numerico == "" and d == "-":
                texto_numerico += d
            if 48 <= ord(d) <= 57:
                texto_numerico += d
            elif d in [".", ","] and not real and accept_float:
                texto_numerico += "."
                real = True
        if texto_numerico in ["", "-", "."]:
            return numero
        if literal:
            return texto_numerico
        if real:
            return float(texto_numerico)
        return int(texto_numerico)

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
        if len(numero) == 0:
            return False
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
                    if real == False:
                        real = True
                    else:
                        return False
                    numero_preparado += "."
                else:
                    numero_preparado += c
        if real == True:
            return float(numero_preparado)
        return int(numero_preparado)

    def cleanSpacesOutside(text):
        ''' Receives a text and removes all spaces outside of simple
        or double brackets ('', ""), so as to minify without
        altering string contents. Example:
        "[  { 'text': 'any text' }  ]" returns "[{'text':'any text'}]"
        '''
        assert type(text) == str
        cleanText, endStringChar = "", ""
        for i in range(0, len(text)):
            if endStringChar and text[i] == endStringChar:
                cleanText += endStringChar
                endStringChar = ""
            elif text[i] in ['"', "'"]:
                if not endStringChar:
                    endStringChar = text[i]
                    cleanText += endStringChar
                else:
                    cleanText += text[i]
            elif text[i] == " " and not endStringChar or\
                text[i] in ["\n", "\t"]:
                pass
            else:
                cleanText += text[i]
        return cleanText
    
    def turnIntoEnglishOrdinalNumber(input_number):
        ''' Receives a string, a float or an int: if it's a string, function
        "Texto.reter_numeros()" will be called to try to obtain a number; if
        it's not possible to obtain a number, the original string will be
        returned; if it's a float, it will be turned into an int; if "number"
        receives an int different from zero, if will be turned into a string
        and the appropriate English language ordinal number suffix in
        superscript format will be concatenated: "st" for 1, "nd" for 2, "rd"
        for 3 or "th" for the remaining cases. Also works for negative ints.
        '''
        assert type(input_number) in [str, float, int]
        if type(input_number) == str:
            assert len(input_number) > 0
            number = Texto.reter_numeros(input_number)
            if number == input_number:
                return number
        elif type(input_number) == float:
            number = int(input_number)
        else:
            number = input_number
        if not number:
            return "0"
        ordinal = str(number)
        if ordinal in ["1", "-1"]: 
            ordinal += chr(738)      # Superscript "s"
            ordinal += chr(7511)     # Superscript "t"  
        elif ordinal in ["2", "-2"]:
            ordinal += chr(8319)     # Superscript "n"
            ordinal += chr(7496)     # Superscript "d"
        elif ordinal in ["3", "-3"]: 
            ordinal += chr(691)      # Superscript "r"
            ordinal += chr(7496)     # Superscript "d"
        else:                        
            ordinal += chr(7511)     # Superscript "t"
            ordinal += chr(688)      # Superscript "h"
        return ordinal

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
