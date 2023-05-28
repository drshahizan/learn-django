'use strict';

function createDetailMap(options) {
    var defaults = {
        mapId: 'detailMap',
        mapZoom: 16,
        mapCenter: [51.505, -0.09],
        markerShow: true,
        markerPosition: [51.505, -0.09],
        markerPath: 'img/marker.svg',
        circleShow: false,
        circleColour: '#4E66F8',
        circleFill: '#8798fa',
        circleOpacity: .5,
        circleRadius: 500,
        circlePosition: [51.505, -0.09],
        tileLayer: {tiles: 'https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png', attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>', subdomains: 'abcd'},
    };

    var settings = $.extend({}, defaults, options);

    var icon = L.icon({
        iconUrl: settings.markerPath,
        iconSize: [25, 37.5],
        popupAnchor: [0, -18],
        tooltipAnchor: [0, 19]
    });

    var dragging = false,
        tap = false;

    if ($(window).width() > 700) {
        dragging = true;
        tap = true;
    }

    var detailMap = L.map(settings.mapId, {
        center: settings.mapCenter,
        zoom: settings.mapZoom,
        dragging: dragging,
        tap: tap,
        scrollWheelZoom: false
    });

    detailMap.once('focus', function () {
        detailMap.scrollWheelZoom.enable();
    });

    L.tileLayer(settings.tileLayer.tiles, {
        attribution: settings.tileLayer.attribution,
        minZoom: 1,
        maxZoom: 19
    }).addTo(detailMap);

    if (settings.circleShow) {
        L.circle(settings.circlePosition, {
            color: settings.circleColour,
            weight: 1,
            fillColor: settings.circleFill,
            fillOpacity: settings.circleOpacity,
            radius: settings.circleRadius
        }).addTo(detailMap);
    }

    if (settings.markerShow) {
        L.marker(settings.markerPosition, {
            icon: icon
        }).addTo(detailMap);
    }
}