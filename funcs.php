<?php
function getAllOrderedMovies($con) {
$allpels = pg_query($con, "SELECT * FROM pelicula, horarios, sucursales WHERE pelicula.idpelicula = horarios.idpelicula AND pelicula.tipo = horarios.tipo AND horarios.idsucursal = sucursales.idsucursal");
$pelist = array();
while ($row = pg_fetch_row($allpels)) {
	$num = $row[5];
	$numa = array();
	$nums = "";
	for($i=0;$i<strlen($num);$i++){
		if($i%4 == 0){
			array_push($numa,$nums);
			$nums = $num[$i];
		} else {
			$nums = $nums.$num[$i];
		}
	}
	$rowi = array('name'=>$row[0],'dur'=>$row[1],'descr'=>$row[2],'hor'=>$numa,'suc'=>$row[6],'cine'=>$row[9],'dir'=>$row[10],'type'=>$row[8]);
	array_push($pelist,$rowi);
}
return $pelist;
}
?>