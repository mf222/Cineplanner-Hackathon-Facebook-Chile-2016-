function transformar_horario(str_horario){
	var lis_horarios = str_horario.split(' ');
	var lis_hor_date = [];
	lis_horarios.forEach(function(hor){
		var hor = Date.parse(hor);
		lis_hor_date.push(hor);
	})
	return lis_hor_date;
}

//Retorna hora de termino de la película(según durac)//
function calcular_termino(empieza, durac){
	var termino = empieza + duracion;
	return termino;
}

//Retorna True si el horario de la palícula calza con la ventana//
function comparar(ven_emp, ven_fin, pel_emp, pel_fin){
	var a = 0;
	//comparacion empieza:
	function(ven_emp, pel_emp){if (ven_emp < pel_emp){a+=1;}};
	//comparacion finaliza:
	function(ven_fin, pel_fin){if(ven_fin>pel_fin){a+=1;}};
	//cierre:
	function(a){if(a===2){return True;}}
}

//Retorna lista de películas que calzan según horario//
function filtrar_pels(lista_pels, ven_emp, ven_fin){
	function(d){if()}
	var pels_calzan = []
	lista_pels.forEach(function(peli){
		peli.horario = transformar_horario(peli.horario);
		peli.duracion = Date.parse(peli.duracion);
		peli.horario.forEach(function(empieza){
			var termino = calcular_termino(empieza, peli.duracion);
			function(d){if(comparar(ven_emp, ven_fin, empieza, termino)==True){
				pels_calzan.push(peli);}}
	return pels_calzan;})

	})
}
