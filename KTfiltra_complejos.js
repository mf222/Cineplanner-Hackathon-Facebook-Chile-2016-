//Funcion recibe complejos_selectos, lista_peliculas

function filtrar_complejo(pels_totales, lis_complejos){
	function(d){if(lis_complejos.length ===0){return pels_totales;}
	pels_totales.forEach(function(peli){
		if (peli.complejo === comple){pels_complejas.push(peli);}
	function(d){return pels_complejas;}
	})}
}

function filtrar_tipo(pels_totales, tipo){
	var lista_filtradas = [];
	pels_totales.forEach(function(peli){if(peli.tipo === tipo){lista_filtradas.push(peli);}}),
	return lista_filtradas;
}