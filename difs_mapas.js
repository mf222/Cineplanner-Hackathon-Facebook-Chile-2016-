
GMaps.geocode({
  address: $('#address').val(),
  callback: function(results, status) {
    if (status == 'OK') {
      var latlng = results[0].geometry.location;
      var latitud = +latlng.lat();
      var longitud = +latlng.lng();
    }
  }
});