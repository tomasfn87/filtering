type numero_cpf = string | number
type digitos_cpf = number[]
type digito_verificador_cpf = number
type digitos_verificadores_cpf = number[]

// const meuCpf:numero_cpf = 111444777
const Cpf:numero_cpf = process.argv[2]

const obter_lista_digitos = (numero_cpf: numero_cpf):digitos_cpf => {
    if (typeof numero_cpf === 'number') {
        numero_cpf = numero_cpf.toString()
    }
    let digitos_cpf:digitos_cpf = []
    for (let i = 0; i < numero_cpf.length; i++) {
        digitos_cpf.push(parseInt(numero_cpf[i]))
    }

    return digitos_cpf
}

let lista_digitos_cpf:digitos_cpf = obter_lista_digitos(Cpf)

const calcular_dv = (digitos_cpf:digitos_cpf):digito_verificador_cpf => {
    let multiplicador:number = digitos_cpf.length + 1
    let calculo_dv = []
    for (let i of digitos_cpf) {
        i *= multiplicador
        calculo_dv.push(i)
        multiplicador -= 1
    }
    let dv = 0
    for (let j of calculo_dv) {
        dv += j
        dv %= 11
    }
    if (dv < 2) {
        return 0
    }
    return 11 - dv
}

const obter_dvs = (numero_cpf:numero_cpf):digitos_verificadores_cpf => {
    let digitos_cpf:digitos_cpf = obter_lista_digitos(numero_cpf)
    let primeiro_dv_cpf:digito_verificador_cpf = calcular_dv(digitos_cpf)
    digitos_cpf.push(primeiro_dv_cpf)
    return [primeiro_dv_cpf, calcular_dv(digitos_cpf)]
}

console.log(obter_dvs(Cpf))
