<head>
<style>
#movList {
	border-radius: 0px 0px 0px 0px;
	-moz-border-radius: 0px 0px 0px 0px;
	-webkit-border-radius: 0px 0px 0px 0px;
	border: 10px solid #000000;
	opacity:0;
	transition: all 1s ease-in-out;
	z-index:1;
	position:relative;
	margin-top:0px;
}
#filtros {
	border-radius: 0px 0px 0px 0px;
	-moz-border-radius: 0px 0px 0px 0px;
	-webkit-border-radius: 0px 0px 0px 0px;
	border: 10px solid #000000;
	transition: all 3s ease-in-out;
	opacity:1;
	z-index:2;
	position:relative;
	margin-top:0px;
}
#changeButton {
	position:relative;
	z-index:3;
	transition: all 2s ease-in-out;
}
</style>
<script type="text/javascript">
function changeDiv() {
	var filt = document.getElementById("filtros");
	var res = document.getElementById("movList");
	var button = document.getElementById("changeButton");
	if (filt.style.opacity == "0") {
		button.innerHTML = "Filtrar";
		filt.style.opacity = "1";
		res.style.opacity = "0";
		button.style.marginTop = 0;
	} else {
		button.innerHTML = "Modificar Filtros";
		filt.style.opacity = "0";
		res.style.opacity = "1";
		button.style.marginTop = -filt.offsetHeight;
		res.style.marginTop = -(filt.offsetHeight-button.offsetHeight);
	}
}
</script>
</head>
<?php
require_once 'conn.php';
function getAllMovies($con) {
$allpels = pg_query($con, "SELECT * FROM pelicula, horarios, sucursales WHERE pelicula.idpelicula = horarios.idpelicula AND horarios.idsucursal = sucursales.idsucursal");
$pelist = array();
while ($row = pg_fetch_row($allpels)) {
	$hor = explode(" ",$row[4]);
	$rowi = array('name'=>$row[0],'dur'=>$row[1],'descr'=>$row[2],'hor'=>$hor,'suc'=>$row[5],'cine'=>$row[7],'dir'=>$row[8]);
	array_push($pelist,$rowi);
}
return $pelist;
}
$pellist = getAllMovies($con);
?>
<div id="filtros">
<?php
$allsuc = pg_query($con, "SELECT DISTINCT * FROM sucursales");
while($srow = pg_fetch_row($allsuc)){
	echo "<input type='checkbox' name='sucheck' value='".$srow[0]."'>".$srow[0]."</input>";
}
?>
<input type="radio" name="leng" value="">Doblada</input>
<input type="radio" name="leng" value="">Subtitulada</input>
<input type="radio" name="form" value="">Normal</input>
<input type="radio" name="form" value="">3D</input>
<input type="radio" name="form" value="">4D</input>
<input type="radio" name="form" value="">Premium</input>
<input type="radio" name="form" value="">IMAX</input>
</div>
<button id="changeButton" onclick="changeDiv();">
Filtrar
</button>
<?php
echo "<div id='movList'><table><thead><tr><th>Nombre</th><th>Duracion</th><th>Descripcion</th><th>Horarios</th><th>Sucursal</th><th>Cine</th><th>Direccion</th></thead><tbody>";
foreach ($pellist as $pel){
	$phor = "";
	foreach ($pel['hor'] as $hor){
		$phor = $phor." ".$hor;
	}
	echo "<tr><td>".$pel['name']."</td><td>".$pel['dur']."</td><td>".$pel['descr']."</td><td>".$phor."</td><td>".$pel['suc']."</td><td>".$pel['cine']."</td><td>".$pel['dir']."</td></tr>";
}
echo "</tbody></table></div>";
?>
<div id="abc">
</div>
<script type='text/javascript'>
var inter = "<?php echo $pellist[0]["descr"]; ?>";
document.getElementById('abc').innerHTML = inter;
</script>