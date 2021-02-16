//Uso de um valor default no construtor -> Valido para outras funções tambem

class Teste {
    constructor(entrada="entrada padrão") {
        this.valor = entrada;
    }
    getValor() {
        return this.valor
    }
}

t1 = new Teste();
console.log(t1.getValor())


t2 = new Teste(1);
console.log(t2.getValor())

