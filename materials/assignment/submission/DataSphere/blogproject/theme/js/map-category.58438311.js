'use strict';

function createListingsMap(options) {

    var defaults = {
        markerPath: 'img/marker.svg',
        markerPathHighlight: 'img/marker-hover.svg',
        imgBasePath: 'img/photo/',
        mapPopupType: 'venue',
        useTextIcon: false,
        tileLayer: {tiles: 'https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png', attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>', subdomains: 'abcd'}
    }

    var settings = $.extend({}, defaults, options);

    var dragging = false,
        tap = false;

    if ($(window).width() > 700) {
        dragging = true;
        tap = true;
    }

    /* 
    ====================================================
      Create and center the base map
    ====================================================
    */

    var map = L.map(settings.mapId, {
        zoom: 14,
        scrollWheelZoom: false,
        dragging: dragging,
        tap: tap,
        scrollWheelZoom: false
    });

    map.once('focus', function () {
        map.scrollWheelZoom.enable();
    });

    L.tileLayer(settings.tileLayer.tiles, {
        attribution: settings.tileLayer.attribution,
        minZoom: 1,
        maxZoom: 19
    }).addTo(map);

    /* 
    ====================================================
      Load GeoJSON file with the data 
      about the listings
    ====================================================
    */

    $.getJSON(settings.jsonFile).done(function (json) {
            L.geoJSON(json, {
                pointToLayer: pointToLayer,
                onEachFeature: onEachFeature
            }).addTo(map);

            if (markersGroup) {
                var featureGroup = new L.featureGroup(markersGroup);
                map.fitBounds(featureGroup.getBounds());
            }

        })
        .fail(function (jqxhr, textStatus, error) {
            console.log(error);
        });

    /* 
    ====================================================
      Bind popup and highlighting features 
      to each marker
    ====================================================
    */

    var markersGroup = []

    var defaultIcon = L.icon({
        iconUrl: settings.markerPath,
        iconSize: [25, 37.5],
        popupAnchor: [0, -18],
        tooltipAnchor: [0, 19]
    });

    var highlightIcon = L.icon({
        iconUrl: settings.markerPathHighlight,
        iconSize: [25, 37.5],
        popupAnchor: [0, -18],
        tooltipAnchor: [0, 19]
    });

    function onEachFeature(feature, layer) {

        layer.on({
            mouseover: highlightMarker,
            mouseout: resetMarker
        });

        if (feature.properties && feature.properties.about) {
            layer.bindPopup(getPopupContent(feature.properties), {
                minwidth: 200,
                maxWidth: 600,
                className: 'map-custom-popup'
            });

            if (settings.useTextIcon) {
                layer.bindTooltip('<div id="customTooltip-' + feature.properties.id + '">$' + feature.properties.price + '</div>', {
                    direction: 'top',
                    permanent: true,
                    opacity: 1,
                    interactive: true,
                    className: 'map-custom-tooltip'
                });
            }

        }
        markersGroup.push(layer);
    }

    function pointToLayer(feature, latlng) {

        if (settings.useTextIcon) {
            var markerOpacity = 0
        } else {
            var markerOpacity = 1
        }

        return L.marker(latlng, {
            icon: defaultIcon,
            id: feature.properties.id,
            opacity: markerOpacity
        });
    }

    function highlightMarker(e) {
        highlight(e.target);
    };

    function resetMarker(e) {
        reset(e.target);
    };

    function highlight(marker) {
        marker.setIcon(highlightIcon);
        if (settings.useTextIcon) {
            findTooltip(marker).addClass('active');
        }
    }

    function reset(marker) {
        marker.setIcon(defaultIcon);
        if (settings.useTextIcon) {
            findTooltip(marker).removeClass('active');
        }
    }

    function findTooltip(marker) {
        var tooltip = marker.getTooltip()
        var id = $(tooltip._content).filter("div").attr("id")
        return $('#' + id).parents('.leaflet-tooltip')
    }

    /* 
    ====================================================
      Construct popup content based on the JSON data
      for each marker
    ====================================================
    */

    function getPopupContent(properties) {

        if (properties.name) {
            var title = '<h6><a href="' + properties.link + '">' + properties.name + '</a></h6>'
        } else {
            title = ''
        }

        if (properties.about) {
            var about = '<p class="">' + properties.about + '</p>'
        } else {
            about = ''
        }

        if (properties.image) {

            var imageClass = 'image';
            if (settings.mapPopupType == 'venue') {
                imageClass += ' d-none d-md-block'
            }

            var image = '<div class="' + imageClass + '" style="background-image: url(\'' + settings.imgBasePath + properties.image + '\')"></div>';
        } else {
            image = '<div class="image"></div>'
        }

        if (properties.address) {
            var address = '<p class="text-muted mb-1"><i class="fas fa-map-marker-alt fa-fw text-dark mr-2"></i>' + properties.address + '</p>'
        } else {
            address = ''
        }
        if (properties.email) {
            var email = '<p class="text-muted mb-1"><i class="fas fa-envelope-open fa-fw text-dark mr-2"></i><a href="mailto:' + properties.email + '" class="text-muted">' + properties.email + '</a></p>'
        } else {
            email = ''
        }
        if (properties.phone) {
            var phone = '<p class="text-muted mb-1"><i class="fa fa-phone fa-fw text-dark mr-2"></i>' + properties.phone + '</p>'
        } else {
            phone = ''
        }

        if (properties.stars) {
            var stars = '<div class="text-xs">'
            for (var step = 1; step <= 5; step++) {
                if (step <= properties.stars) {
                    stars += "<i class='fa fa-star text-warning'></i>"
                } else {
                    stars += "<i class='fa fa-star text-gray-300'></i>"
                }
            }
            stars += "</div>"
        } else {
            stars = ''
        }

        if (properties.url) {
            var url = '<a href="' + properties.url + '">' + properties.url + '</a><br>'

        } else {
            url = ''
        }

        var popupContent = '';

        if (settings.mapPopupType == 'venue') {
            popupContent =
                '<div class="popup-venue">' +
                image +
                '<div class="text">' +
                title +
                about +
                address +
                email +
                phone +
                '</div>' +
                '</div>';
        } else if (settings.mapPopupType == 'rental') {
            popupContent =
                '<div class="popup-rental">' +
                image +
                '<div class="text">' +
                title +
                stars +
                '</div>' +
                '</div>';
        }


        return popupContent;
    }
    /* 
    ====================================================
      Highlight marker when users hovers above
      corresponding .card in the listing
    ====================================================
    */

    L.Map.include({
        getMarkerById: function (id) {
            var marker = null;
            this.eachLayer(function (layer) {
                if (layer instanceof L.Marker) {
                    if (layer.options.id === id) {
                        marker = layer;
                    }
                }
            });
            return marker;
        }
    });

    $('[data-marker-id!=""][data-marker-id]').on('mouseenter', function () {
        var markerId = $(this).data('marker-id');
        var marker = map.getMarkerById(markerId);
        if (marker) {
            highlight(marker);
        }
    });
    $('[data-marker-id!=""][data-marker-id]').on('mouseleave', function () {
        var markerId = $(this).data('marker-id');
        var marker = map.getMarkerById(markerId);
        if (marker) {
            reset(marker);
        }
    });
}