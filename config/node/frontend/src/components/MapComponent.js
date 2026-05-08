import React, {useRef, useEffect} from 'react';

import Map from "ol/Map";
import View from "ol/View";
import TileLayer from "ol/layer/Tile"
import {useGeographic} from 'ol/proj'

import OSM from 'ol/source/OSM'
import {TileWMS} from 'ol/source'

import './MapComponent.css';


function MapComponent() {

    const mapRef = useRef(null);

    useGeographic();

    useEffect(() => {
        const map = new Map(
            {
                target: mapRef.current,
                layers: [
                    new TileLayer({
                        source: new OSM(),

                    }),

                    new TileLayer({
                        source: new TileWMS({
                            url: 'http://localhost:9000/geoserver/prge/wms?',
                            params: {
                                'LAYERS': 'prge:AEC015_clip',
                                'TILED': true
                            },
                            serverType: 'geoserver',
                            transition: 0
                        })
                    })
                ],

                view: new View(
                    {
                        center: [21, 52.23], zoom: 6
                    }
                )

            }
        )
        return () => map.setTarget(null)

    }, []);

    return (
        <div className='mapComponent' ref={mapRef}></div>
    );
}

export default MapComponent;