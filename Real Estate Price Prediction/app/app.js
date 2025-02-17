function getBathValue() {
    var uiBathrooms = document.getElementsByName("uiBathrooms");
    for (var i = 0; i < uiBathrooms.length; i++) {
        if (uiBathrooms[i].checked) {
            return parseInt(uiBathrooms[i].value);
        }
    }
    return -1; // Invalid Value
}

function getBHKValue() {
    var uiBHK = document.getElementsByName("uiBHK");
    for (var i = 0; i < uiBHK.length; i++) {
        if (uiBHK[i].checked) {
            return parseInt(uiBHK[i].value);
        }
    }
    return -1; // Invalid Value
}

function getFloorsValue() {
    var uiFloors = document.getElementsByName("uiFloors");
    for (var i = 0; i < uiFloors.length; i++) {
        if (uiFloors[i].checked) {
            return parseInt(uiFloors[i].value);
        }
    }
    return -1;
}

function getConditionsValue() {
    var uiCondition = document.getElementsByName("uiCondition");
    for (var i = 0; i < uiCondition.length; i++) {
        if (uiCondition[i].checked) {
            return parseInt(uiCondition[i].value);
        }
    }
    return -1;
}

function onClickedEstimatePrice() {
    console.log("Estimate price button clicked");
    var sqft = document.getElementById("uiSqft");
    var bhk = getBHKValue();
    var bathrooms = getBathValue();
    var floors = getFloorsValue();
    var condition = getConditionsValue();
    var location = document.getElementById("uilocations");
    var estPrice = document.getElementById("uiEstimatedPrice");

    var url = "http://127.0.0.1:5000/predict_home_price";
    //var url = "/api/predict_home_price"

    $.post(url, {
        bedrooms: bhk,
        bathrooms: bathrooms,
        sqft_living: parseFloat(sqft.value),
        floors: floors,
        condition: condition,
        city: location.value
    }, function (data, status) {
        console.log(data.estimated_price);
        estPrice.innerHTML = "<h2>" + data.estimated_price.toString() + "$</h2>";
        console.log(status);
    });
}

function onPageLoad() {
    console.log("document loaded");
    var url = "http://127.0.0.1:5000/get_location_names";
    //var url = "/api/get_location_names"
    $.get(url, function (data, status) {
        console.log("got response for get_location_names request");
        if (data) {
            var locations = data.locations;
            $('#uilocations').empty();
            for (var i = 0; i < locations.length; i++) {
                var opt = new Option(locations[i]);
                $('#uilocations').append(opt);
            }
        }
    });
}

window.onload = onPageLoad;
