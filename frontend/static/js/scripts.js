$('#cities-link').click(function() {
    $('#cities-content, #earthquakes-content, #nearest-earthquake-content, #search-history-content, #home-content').hide()
    $('#cities-content').show();

    $.ajax({
    url: "/apis/cities/",
    type: "GET",
    success: function(data) {
        $("#city-list").empty();
        $.each(data, function(index, city) {
        $("#city-list").append("<li>" + city.name + "</li>");
        });
    },
    error: function(jqXHR, textStatus, errorThrown) {
        console.log("Error to load the cities: " + textStatus, errorThrown);
    }
    });
});


$('#earthquakes-link').click(function() {
    $('#cities-content, #earthquakes-content, #nearest-earthquake-content, #search-history-content, #home-content').hide()
    $('#earthquakes-content').show();
});

$('#nearest-link').click(function() {
    $('#cities-content, #earthquakes-content, #nearest-earthquake-content, #search-history-content, #home-content').hide()
    $('#nearest-earthquake-content').show();

    $.ajax({
        url: "/apis/cities/",
        type: "GET",
        success: function(data) {
            $("#cities-dropdown").empty();
            $.each(data, function(index, city) {
                console.log(city.name)
                $("#cities-dropdown").append("<option value=" + city.name + ">"+city.name+"</option>");
            });
        },
        error: function(jqXHR, textStatus, errorThrown) {
            console.log("Error to load the cities: " + textStatus, errorThrown);
        }
        });
});

$('#history-link').click(function() {
    $('#cities-content, #earthquakes-content, #nearest-earthquake-content, #search-history-content, #home-content').hide()
    $('#search-history-content').show();

    $.ajax({
        url: "/apis/nearest-earthquake/",
        type: "GET",
        success: function(data) {
            $("#history-list").empty();
            
            $.each(data, function(index, history) {
            $("#history-list").append("<li> " + 
            
            "City: "+history.city +"</br>"+
            "Start Date: "+history.start_date +"</br>"+
            "End Date: "+history.end_date +"</br>"+
            "Nearest Earthquake: "+history.nearest_earthquake +"</br>"+
            "Nearest Earthquake Date: " + history.nearest_earthquake_date + "</br>" +
            "Distance to the Earthquake(km): "+history.distance_km +"</br>"+
            "</br></li>");
            });
        },
        error: function(jqXHR, textStatus, errorThrown) {
            console.log("Erro ao recuperar as cidades: " + textStatus, errorThrown);
        }
        });
});

$('#home').click(function() {
    $('#cities-content, #earthquakes-content, #nearest-earthquake-content, #search-history-content, #home-content').hide()
    $('#home-content').show();
});


$( document ).ready(function() {
    $('#cities-content, #earthquakes-content, #nearest-earthquake-content, #search-history-content, #home-content').hide()
    $('#home-content').show();
});