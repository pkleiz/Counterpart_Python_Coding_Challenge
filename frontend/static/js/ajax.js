$('#find-earthquakes').click(function () {
    var startDate = $("#start-date-input-earthquake").val();
    var endDate = $("#end-date-input-earthquake").val();
    $("#find-earthquakes").prop("disabled", true).html('Loading <i class="fa fa-spinner fa-spin"></i> ')
    $.ajax({
        url: "/apis/earthquakes/",
        type: "GET",
        data: {
            start_date: startDate,
            end_date: endDate
        },
        success: function (data) {
            if (data.length == 0) {
                $("#earthquake-list").empty();
                data = { 'title': 'Without results for these 2 dates.' }
                $("#earthquake-list").append("Message: " + data.title)
            }
            else {

                $("#earthquake-list").empty();
                $.each(data, function (index, earthquake) {
                    $("#earthquake-list").append("<li> " +

                        "Magnitude: " + earthquake.magnitude + "</br>" +
                        "Location: " + earthquake.location + "</br>" +
                        "Title: " + earthquake.title + "</br>" +
                        "Latitude: " + earthquake.latitude + "</br>" +
                        "Longitude: " + earthquake.longitude + "</br>" +
                        "Date: " + earthquake.date + "</br>" +
                        "</br></li>");
                });
            }
            $("#find-earthquakes").prop("disabled", false).html('Find Earthquakes')
        },
        error: function (jqXHR, textStatus, errorThrown) {
            console.log("Error to load the cities: " + textStatus, errorThrown);
            $("#find-earthquakes").prop("disabled", false).html('Error, try again')
        }
    });
});


$('#nearest-earthquake').click(function () {
    var startDate = $("#start-date-input-nearest").val();
    var endDate = $("#end-date-input-nearest").val();
    var selectedCity = $("#cities-dropdown option:selected").text()
    $("#nearest-earthquake").prop("disabled", true).html('Loading <i class="fa fa-spinner fa-spin"></i> ')



    $.ajax({
        url: "/apis/nearest-earthquake/",
        type: "GET",
        data: {
            start_date: startDate,
            end_date: endDate,
            city: selectedCity,
        },
        success: function (data) {
            if (data.length == 0) {
                $("#earthquake-list").empty();
                data = { 'title': 'Without results for these 2 dates.' }
                $("#earthquake-list").append("Message: " + data.title)
            }
            else {
                $("#nearest-list").empty();
                $.each(data, function (index, nearest) {
                    $("#nearest-list").append("<li> " +

                        "City: " + nearest.city + "</br>" +
                        "Start Date: " + nearest.start_date + "</br>" +
                        "End Date: " + nearest.end_date + "</br>" +
                        "Nearest Earthquake: " + nearest.nearest_earthquake + "</br>" +
                        "Nearest Earthquake Date: " + nearest.nearest_earthquake_date + "</br>" +
                        "Distance to the Earthquake(km): " + nearest.distance_km + "</br>" +
                        "</br></li>");
                });
            }
            $("#nearest-earthquake").prop("disabled", false).html('Nearest Earthquake')

        },
        error: function (jqXHR, textStatus, errorThrown) {
            console.log("Error to load the cities: " + textStatus, errorThrown);
        }
    });
});
