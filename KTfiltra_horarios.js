function transformar_horario(str_horario){
	var lis_horarios = str_horario.split(' ');
	var lis_hor_date = [];
	lis_horarios.forEach(function(hor){
		var hor = Date.parse(hor);
		lis_hor_date.push(hor);
	})
	return lis_hor_date;
}
function calcular_termino(empieza, durac){
	var termino = empieza + duracion;
	return termino;
}
function comparar(ven_emp, ven_fin, pel_emp, pel_fin){
	var a = 0;
	//comparacion empieza:
	function(ven_emp, pel_emp){if (ven_emp < pel_emp){a+=1;}};
	//comparacion finaliza:
	function(ven_fin, pel_fin){if(ven_fin>pel_fin){a+=1;}};
	//cierre:
	function(a){if(a===2){return True;}}
}

function filtrar_pels(lista_pels, ven_emp, ven_fin){
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
