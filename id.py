import texto as T

class Cpf:
    def marcar(cpf):
        n_cpf = T.Texto.reter_numeros(cpf)
        assert type(n_cpf) == int
        n_cpf = str(n_cpf)
        if len(n_cpf) != 11:
            return False
        n_cpf = T.Texto.adicionar_separador(n_cpf, 2)
        n_cpf = T.Texto.adicionar_separador(n_cpf, 6, ".")
        return T.Texto.adicionar_separador(n_cpf, 10, ".")
  
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
        digitos_cpf = T.Texto.obter_digitos(cpf, 9)
        primeiro_dv_cpf = Cpf.calcular_dv(digitos_cpf)
        digitos_cpf.append(primeiro_dv_cpf)
        return primeiro_dv_cpf, Cpf.calcular_dv(digitos_cpf)
    
    def verificar(cpf):
        cpf, dvs = str(cpf), Cpf.obter_dvs(cpf)
        if int(cpf[-1]) == dvs[-1] and int(cpf[-2]) == dvs[-2]:
            return True
        return False