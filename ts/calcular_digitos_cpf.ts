type numero_cpf = string | number
type lista_digitos_cpf = number[]
type digito_verificador_cpf = number
type digitos_verificadores_cpf = number[]

// const Cpf:numero_cpf = 111444777
const Cpf:numero_cpf = process.argv[2]

const obter_lista_digitos = (numero_cpf: numero_cpf):lista_digitos_cpf => {
    if (typeof numero_cpf === 'number') {
        numero_cpf = numero_cpf.toString()
    }
    let lista_digitos_cpf:lista_digitos_cpf = []
    for (let i = 0; i < numero_cpf.length; i++) {
        lista_digitos_cpf.push(parseInt(numero_cpf[i]))
    }
    if (lista_digitos_cpf.length > 9) {
        console.warn(
            `Foi recebido um número de CPF com ${lista_digitos_cpf.length} dígitos: só os 9 primeiros serão utilizados`
        )
        return lista_digitos_cpf.slice(0, 9)
    }
    return lista_digitos_cpf
}

const calcular_dv = (lista_digitos_cpf:lista_digitos_cpf):digito_verificador_cpf => {
    let multiplicador:number = lista_digitos_cpf.length + 1
    let calculo_dv = []
    for (let i of lista_digitos_cpf) {
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

const obter_dvs = (Cpf:numero_cpf):digitos_verificadores_cpf => {
    let digitos_cpf:lista_digitos_cpf = obter_lista_digitos(Cpf)
    if (digitos_cpf.length < 9) {
        console.error(
            `Foi recebido um número de CPF com apenas ${digitos_cpf.length} dígitos: o CPF deve ter ao menos 9 dígitos`
        )
        return []
    }
    let cpf_informado = `${digitos_cpf.slice(0,3).join("")}`
    cpf_informado += `.${digitos_cpf.slice(3,6).join("")}`
    cpf_informado += `.${digitos_cpf.slice(6,9).join("")}`
    console.log(`CPF informado: ${cpf_informado}`)
    let dv_1:digito_verificador_cpf = calcular_dv(digitos_cpf)
    let dv_2:digito_verificador_cpf = digitos_cpf.push(dv_1)
    dv_2 = calcular_dv(digitos_cpf)
    console.log(`CPF completo: ${cpf_informado}-${dv_1}${dv_2}`)
    return [dv_1, dv_2]
}

console.log(obter_dvs(Cpf))
