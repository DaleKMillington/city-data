// Base Imports
import { useEffect } from "react";

// Third Party Imports
import {Marker, Tooltip, useMap} from "react-leaflet";
import L from 'leaflet';

// Interfaces
import {CityData} from "../interfaces/CityData.ts";

const mapMarker = L.divIcon({
    className: 'map-marker',
    iconSize: [30, 30],
});

const Markers = ({ cityData }: { cityData: CityData[] }) => {
    const map = useMap(); // Get the map instance using useMap hook

    useEffect(() => {
        if (cityData.length > 0) {
            const bounds = cityData.map(marker => [marker.latitude, marker.longitude]);
            // @ts-ignore
            map.fitBounds(bounds);
        }
    }, [cityData, map]);

    return (
        <>
            {cityData.map(marker => (
                <Marker key={marker.id} position={[marker.latitude, marker.longitude]} icon={mapMarker}>
                    <Tooltip className="marker-tooltip">{marker.name}</Tooltip>
                </Marker>
            ))}
        </>
    );
};

export default Markers;