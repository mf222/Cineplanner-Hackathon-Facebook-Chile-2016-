<head>
<link rel="stylesheet" type="text/css" href="css.css" media="screen" />
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
require_once 'funcs.php';
$pellist = getAllOrderedMovies($con);
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
echo "<div id='movList'><table><thead><tr><th>Nombre</th><th>Duracion</th><th>Descripcion</th><th>Horarios</th><th>Sucursal</th><th>Cine</th><th>Direccion</th><th>Tipo</th></tr></thead><tbody>";
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
<section id="wrapper">
Click the allow button to let the browser find your location.

<script type="text/javascript" src="http://maps.google.com/maps/api/js?sensor=true"></script>
    <article>

    </article>
<script>
function success(position) {
  var mapcanvas = document.createElement('div');
  mapcanvas.id = 'mapcontainer';
  mapcanvas.style.height = '400px';
  mapcanvas.style.width = '600px';

  document.querySelector('article').appendChild(mapcanvas);

  var coords = new google.maps.LatLng(position.coords.latitude, position.coords.longitude);
  
  var options = {
    zoom: 15,
    center: coords,
    mapTypeControl: false,
    navigationControlOptions: {
    	style: google.maps.NavigationControlStyle.SMALL
    },
    mapTypeId: google.maps.MapTypeId.ROADMAP
  };
  var map = new google.maps.Map(document.getElementById("mapcontainer"), options);

  var marker = new google.maps.Marker({
      position: coords,
      map: map,
      title:"You are here!"
  });
}

if (navigator.geolocation) {
  navigator.geolocation.getCurrentPosition(success);
} else {
  error('Geo Location is not supported');
}

</script>
</section>
<script>

</script>
<?php
pg_close($conn);
?>