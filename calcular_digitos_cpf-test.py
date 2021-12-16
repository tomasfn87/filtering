import pytest
import calcular_digitos_cpf

# calcular_digitos_cpf.calcular_digitos("111444777")

class TestCalcularDigitosCpf:
    @pytest.fixture
    def calcular_digitos(self):
        return calcular_digitos_cpf.calcular_digitos

    @pytest.mark.parametrize("numero_cpf, resultado", [
        ("111444777", ("CPF informado: 111.444.777", "Dígitos:       3, 5", "CPF completo:  111.444.777-35")),
        ("11144477799", ("CPF informado: 111.444.777", "Dígitos:       3, 5", "CPF completo:  111.444.777-35")),
        ("11144477735", ("CPF informado: 111.444.777", "Dígitos:       3, 5", "CPF completo:  111.444.777-35")),
    ])
    def test_calcular_digitos(self, numero_cpf, resultado, calcular_digitos):
        assert calcular_digitos(numero_cpf) == resultado
