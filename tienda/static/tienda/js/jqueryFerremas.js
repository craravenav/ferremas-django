$(document).ready(function() {
    
    //Selector Region de Destino
    var selectDestinoRegion = $('#countySelectDestinoRegion');

    // Llamada a la API de Chilexpress para obtener las regiones
    $.ajax({
        url: 'https://testservices.wschilexpress.com/georeference/api/v1.0/regions',
        type: 'GET',
        headers: {
            'Cache-Control': 'no-cache',
            'Ocp-Apim-Subscription-Key': 'f22dc08fafc448ae97fecf72b43bd9d9'
        },
        success: function(response) {
            // Itera sobre la respuesta y agrega las opciones al select
            response.regions.forEach(function(area) {
                var option = $('<option>', {
                    value: area.regionId,
                    text: area.regionName
                });
                selectDestinoRegion.append(option);

            });
        },
        error: function(err) {
            console.error(err);
        }
    });

    //Selector Comuna de Destino
    var selectDestinoComuna = $('#countySelectDestinoComuna');

    //En base a la Region seleccionada se actualiza el listado de comunas
    $('#countySelectDestinoRegion').change(function() {
        selectDestinoComuna.empty();
        var selectedOption = $(this).val();
        console.log("REGION:" + selectedOption);
        var url_region = 'https://testservices.wschilexpress.com/georeference/api/v1.0/coverage-areas?RegionCode=' + selectedOption + '&type=0';

        $.ajax({
            url: url_region,
            type: 'GET',
            headers: {
                'Cache-Control': 'no-cache',
                'Ocp-Apim-Subscription-Key': 'f22dc08fafc448ae97fecf72b43bd9d9'
            },
            success: function(response) {
                // Itera sobre la respuesta y agrega las opciones al select
                response.coverageAreas.forEach(function(area) {
                    var option = $('<option>', {
                        value: area.countyCode,
                        text: area.coverageName
                    });
                    selectDestinoComuna.append(option);
                    selectDestinoComuna.prop('disabled', false);
                });
            },
            error: function(err) {
                console.error(err);
            }
        });
    });

    //En base a la Region seleccionada se actualiza el listado de comunas
    $('#countySelectDestinoComuna').change(function() {
        $('#btnCalcularEnvio').prop('disabled', false);
    });

    // LLAMADA PARA CALCULAR ENVIO
    $('#btnCalcularEnvio').click(function() {
        // Datos de la solicitud
        console.log("ENTRE");
        var comunaDestino = $('#countySelectDestinoComuna').val();
        var pesoCarrito = $('#inputPesoCarrito').val();
        console.log(comunaDestino);
        console.log(pesoCarrito);
        var requestData = {
            // FIJAMOS SANTIAGO COMO ORIGEN
            "originCountyCode": "STGO",
            // DESTINO SE OBTIENE POR PARAMETRO
            "destinationCountyCode": comunaDestino,
            "package": {
                "weight": pesoCarrito,
                "height": "1",
                "width": "1",
                "length": "1"
            },
            "productType": 3,
            "contentType": 1,
            "declaredWorth": "2333",
            "deliveryTime": 0
        };

        // Convertir los datos a formato JSON
        var jsonData = JSON.stringify(requestData);

        // URL de la API
        var apiUrl = 'http://testservices.wschilexpress.com/rating/api/v1.0/rates/courier';

        // Clave secreta
        var secretKey = '471fa8f23ece405d809ea8a876782a71';

        // Encabezados de la solicitud
        var headers = {
            'Content-Type': 'application/json',
            'Ocp-Apim-Subscription-Key': secretKey
        };

        // Realizar la petición AJAX
        $.ajax({
            url: apiUrl,
            type: 'POST',
            headers: headers,
            data: jsonData,
            success: function(response) {
                console.log("llamada exitosa");
                // Dejamos fijo el servicio 2 PRIORITARIO 3 EXPRESS 43 LEJOS
                var servicioEncontrado = response.data.courierServiceOptions.find(function(servicio) {
                    return servicio.serviceTypeCode === 43 || servicio.serviceTypeCode === 3 || servicio.serviceTypeCode === 2;
                });

                console.log("servicio encontrado:"+servicioEncontrado.serviceValue);

                if (servicioEncontrado) {
                    $('#envio-subtotal').text("$"+servicioEncontrado.serviceValue);
                    carritoSubtotal = $('#carrito-subtotal').text();
                    var valorNumerico = carritoSubtotal.replace(/\$|,/g, '');
                    var monto = parseFloat(valorNumerico);
                    var envio = parseFloat(servicioEncontrado.serviceValue);
                    console.log(monto);
                    console.log(envio);
                    subTotal = monto + envio;
                    $('#carrito-total').text("$"+subTotal);
                } else {
                    console.log("No se encontró ningún servicio con serviceTypeCode 43.");
                }
            },
            error: function(xhr, status, error) {
                // Manejar errores aquí
                console.error(xhr.responseText);
            }
        });
    });


    
});