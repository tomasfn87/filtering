from id import Cpf

def calcular_digitos(cpf):
    assert len(str(cpf)) >= 9
    
    cpf_informado = "{}.{}.{}".format(
        cpf[0:3], cpf[3:6], cpf[6:9]
    )

    digitos = Cpf.obter_dvs(cpf)

    resultado1 = "CPF informado: {}".format(
        cpf_informado
    )
    
    resultado2 = "Dígitos:       {}, {}".format(
        digitos[0], digitos[1]
    )
    
    resultado3 = "CPF completo:  {}".format(
        Cpf.marcar(int(str(cpf[:9]) + str(digitos[0]) + str(digitos[1])))
    )
    return resultado1, resultado2, resultado3

if __name__ == "__main__":
    import sys
    cpf = str(sys.argv[1])
    for resultado in calcular_digitos(cpf):
        print(resultado)
