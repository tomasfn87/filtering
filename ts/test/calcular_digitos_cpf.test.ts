import obter_dvs from "../calcular_digitos_cpf";
import { calcular_dv, obter_lista_digitos } from "../calcular_digitos_cpf";
import { expect } from "chai";

describe('Calcular dígitos CPF', function() {
    it('../calcular_digitos_cpf.ts.calcular_dv - Calcular dígito verificador a partir de um número de CPF', function() {
        let result = calcular_dv([1,1,1,4,4,4,7,7,7]);
        expect(result).to.eql(3); // and it also works just fine here, so I'll be testing it #4
    });

    it('../calcular_digitos_cpf.ts.obter_lista_digitos - Obter Lista de dígitos de um número de CPF', function() {
        let result = obter_lista_digitos('111444777');
        expect(result).to.eql([1,1,1,4,4,4,7,7,7]); // needed to use chai .to.eql to compare arrays #1
    });

    it('../calcular_digitos_cpf.ts.obter_lista_digitos - Obter Lista de dígitos de um número de CPF', function() {
        let result = obter_lista_digitos(111444777);
        expect(result).to.eql([1,1,1,4,4,4,7,7,7]); // needed to use chai .to.eql to compare arrays #2
    });

    it('../calcular_digitos_cpf.ts.obter_dvs - Obter os 2 dígitos verificadores a partir de um número de CPF', function() {
        let result = obter_dvs('111444777');
        expect(result).to.eql([3, 5]); // needed to use chai .to.eql to compare arrays #3
    });
});
