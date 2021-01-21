<?php

#Classe
class Teste 
{

    #Visibilidade dos valores 
    private $entrada = "";

    #Construtor
    public function __construct($entrada) 
    {
        $this->setValor($entrada);
    }

    #Set
    public function setValor($entrada)
    {
        $this->entrada = $this->tratamentoSimples($entrada);
    }

    #Get
    public function getValor(): string
    {
        return $this->entrada;
    }

    #Funcao simples
    public function tratamentoSimples($entrada): string
    {
        return "Pastel-{$entrada}";
    }

}

#Chamando a classe
$teste = New Teste("1");
echo $teste->getValor();
echo "\n";
echo $teste->tratamentoSimples("teste");
