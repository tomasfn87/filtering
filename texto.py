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

    def lista_parenteses(lista_1, lista_2):
        lista_parenteses = []
        item = ""
        for i in range(0, len(lista_1)):
            item += (str(lista_1[i]) + " ("
            + str(lista_2[i]) + ")")
            lista_parenteses.append(item)
            item = ""
        return lista_parenteses
    
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
        elif inteiro[0] == "0" or literal == True:
            return inteiro
        return int(inteiro)
    
    def obter_digitos(numero, limite=False):
        numero = str(numero)
        if limite == False:
            limite = len(numero)
        lista_digitos = []
        for i in range(0, limite):
            lista_digitos.append(int(numero[i]))
        return lista_digitos

class Cpf:
    def marcar(cpf):
        n_cpf = Texto.reter_numeros(cpf)
        assert type(n_cpf) == int
        n_cpf = str(n_cpf)
        if len(n_cpf) != 11:
            return False
        n_cpf = Texto.adicionar_separador(n_cpf, 2)
        n_cpf = Texto.adicionar_separador(n_cpf, 6, ".")
        return Texto.adicionar_separador(n_cpf, 10, ".")
  
    def calcular_dv(digitos_cpf):
        multiplicador = len(digitos_cpf) + 1
        calculo_dv = []
        for i in digitos_cpf:
            i *= multiplicador
            calculo_dv.append(i)
            multiplicador -= 1
        dv = 0
        for j in calculo_dv:
            dv += j
            dv = dv % 11
        if dv < 2:
            return 0
        return 11 - dv
    
    def obter_dvs(cpf):
        digitos_cpf = Texto.obter_digitos(cpf, 9)
        primeiro_dv_cpf = Cpf.calcular_dv(digitos_cpf)
        digitos_cpf.append(primeiro_dv_cpf)
        segundo_dv_cpf = Cpf.calcular_dv(digitos_cpf)
        return primeiro_dv_cpf, segundo_dv_cpf
    
    def verificar(cpf):
        cpf = str(cpf)
        dvs = Cpf.obter_dvs(cpf)
        if int(cpf[-1]) == dvs[-1] and int(cpf[-2]) == dvs[-2]:
            return True
        return False