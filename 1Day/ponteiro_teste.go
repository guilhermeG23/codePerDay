package main;

import "fmt";

//Mexendo com ponteiros
func main() {

	//Variaveis de teste
	var teste1 string = "teste" //Original
	var teste2 string = teste1 //Copia do valor
	var teste3 *string = &teste1 //Ponteiro de memoria

	//Alterando o valor da variavel
	teste1 = "pastel"

	//Demonstrando
	fmt.Println(teste1) //Valor da variavel
	fmt.Println(teste2) //Valor da copia
	fmt.Println(*teste3) //Valor do ponteiro
}
