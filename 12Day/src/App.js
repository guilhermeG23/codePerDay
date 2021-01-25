import React, { Component } from "react";
import TituloH1 from "./components/TituloH1"; //Importando a classe criada
import { TituloH2 } from "./components/TituloH2"; //Importando a classe criada sem default, necessita do {} para ser chamada

//O Render só consegue trabalhar com um unico elemento, isso significa que deve haver uma estrutura que deriva internamente dentro do elemento pai, no caso a div contem tudo a trabalhar
class App extends Component {	
	render() {
		return (
			<div>
				<TituloH1/>
				<TituloH2/>
			</div>
		);}
}

export default App;
