/**
 * Created by Artur on 11.05.17.
 */

function initMap() {
    var uluru = {lat: 55.752167229735626, lng: 37.67096339817806};
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 16,
        center: uluru
    });
    var marker = new google.maps.Marker({
        position: uluru,
        map: map
    });
}