type numero = number | string | object;
type string_numerica = string;

const limpar_numero = (numero:numero):string_numerica => {
  let numero_em_limpeza:string_numerica = "";
  let numero_limpo:string_numerica = "";

  if (typeof numero === 'object' && Array.isArray(numero) && numero.length !== 0) {
    for (let i of numero) {
        if (typeof i === 'string') {
          numero_em_limpeza += i;
        } else if (typeof i === 'number') {
            numero_em_limpeza += i.toString();
        };
    };
  } else if (typeof numero === 'number') {
    numero_em_limpeza = numero.toString();
  } else if (typeof numero === 'string') {
    if (numero.length === 0) {
        return numero_limpo;
    };
    numero_em_limpeza = numero;
  };

  for (let c of numero_em_limpeza) {
    if (c.charCodeAt(0) >= 48 && c.charCodeAt(0) <= 57) {
      numero_limpo += c
    }
  };

  return numero_limpo;
}

export default limpar_numero;
