// Base Imports
import { useEffect, useState } from 'react';

// Third Party Imports
import 'leaflet/dist/leaflet.css';
import { MapContainer, TileLayer } from 'react-leaflet';
import axios from 'axios';

// Components
import Markers from '../components/Markers.tsx'
import WeatherChartsUI from "../components/WeatherChartsUI.tsx";

// Interfaces
import { CityData } from '../interfaces/CityData.ts';

const Map = () => {

    // Callbacks
    const fetchCityData = () => {
        axios.get(`${import.meta.env.VITE_API_BASE_URL}/city/`, {
            headers:{
                'X-API-KEY': import.meta.env.VITE_X_API_KEY
            }
        })
            .then(response => setCityData(response.data))
            .catch(error => console.error('Error fetching data:', error))
    }

    const handleMarkerClick = (marker: CityData) => setActiveCity(marker);
    const clearActiveCity = () => setActiveCity(null);

    // Hooks
    const [cityData, setCityData] = useState<CityData[]>([]);
    const [
        activeCity,
        setActiveCity
    ] = useState<CityData | null>(null);

    useEffect(() => fetchCityData(), []);

    return (
        <>
            <MapContainer
                className="map-container"
                minZoom={3}
                maxZoom={19}
                scrollWheelZoom={true}
                zoomControl={false}
            >
                <TileLayer
                    url="https://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}"
                />
                <Markers cityData={ cityData } onMarkerClick={ handleMarkerClick }></Markers>
                { !!activeCity && <WeatherChartsUI activeCity={ activeCity } clearActiveCity={ clearActiveCity } />}
            </MapContainer>

        </>

    )
}

export default Map;