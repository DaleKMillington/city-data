// Base Imports
import { useEffect } from "react";

// Third Party Imports
import {Marker, Tooltip, useMap} from "react-leaflet";
import L from 'leaflet';

// Interfaces
import {CityData} from "../interfaces/CityData.ts";
interface MarkersProps {
    cityData: CityData[];
    onMarkerClick: (marker: CityData) => void
}

const Markers = ({ cityData, onMarkerClick }: MarkersProps) => {

    // Hooks
    const map = useMap();

    useEffect(() => {
        if (cityData.length > 0) {
            const bounds = cityData.map(marker => [marker.latitude, marker.longitude]);
            // @ts-ignore
            map.fitBounds(bounds);
        }
    }, [cityData, map]);

    // Marker Styles
    const mapMarker = L.divIcon({
        className: 'map-marker',
        iconSize: [30, 30],
    });

    return (
        <>
            {cityData.map(marker => (
                <Marker
                    key={marker.id}
                    position={[marker.latitude, marker.longitude]}
                    icon={mapMarker}
                    eventHandlers={{
                        click: () => onMarkerClick(marker)
                    }}
                >
                    <Tooltip className="marker-tooltip">{marker.name}</Tooltip>
                </Marker>
            ))}
        </>
    );
};

export default Markers;