$('#find-earthquakes').click(function() {
    var startDate = $("#start-date-input-earthquake").val();
    var endDate = $("#end-date-input-earthquake").val();

    $.ajax({
        url: "/apis/earthquakes/",
        type: "GET",
        data: {
            start_date: startDate,
            end_date: endDate
        },
        success: function(data) {
            $("#earthquake-list").empty();
            $.each(data, function(index, earthquake) {
            $("#earthquake-list").append("<li> " + 
            
            "Magnitude: "+earthquake.magnitude +"</br>"+
            "Location: "+earthquake.location +"</br>"+
            "Title: "+earthquake.title +"</br>"+
            "Latitude: "+earthquake.latitude +"</br>"+
            "Longitude: "+earthquake.longitude +"</br>"+
            "Date: "+earthquake.date +"</br>"+
            "</br></li>");
            });
        },
        error: function(jqXHR, textStatus, errorThrown) {
            console.log("Error to load the cities: " + textStatus, errorThrown);
        }
    });
});


$('#nearest-earthquak').click(function() {
    var startDate = $("#start-date-input-nearest").val();
    var endDate = $("#end-date-input-nearest").val();
    var selectedCity = $("#cities-dropdown").val();

    $.ajax({
        url: "/apis/nearest-earthquake/",
        type: "GET",
        data: {
            start_date: startDate,
            end_date: endDate,
            city: selectedCity
        },
        success: function(data) {
            $("#nearest-list").empty();
            $.each(data, function(index, nearest) {
            $("#nearest-list").append("<li> " + 
            
            "City: "+nearest.city +"</br>"+
            "Start Date: "+nearest.start_date +"</br>"+
            "End Date: "+nearest.end_date +"</br>"+
            "Nearest Earthquake: "+nearest.nearest_earthquake +"</br>"+
            "Distance to the Earthquake(km): "+nearest.distance_km +"</br>"+
            "</br></li>");
            });
        },
        error: function(jqXHR, textStatus, errorThrown) {
            console.log("Error to load the cities: " + textStatus, errorThrown);
        }
    });
});
