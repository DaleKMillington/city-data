// Base Imports
import { useEffect, useState } from 'react';

// Third Party Imports
import 'leaflet/dist/leaflet.css';
import { MapContainer, TileLayer } from 'react-leaflet';
import axios from 'axios';

// Components
import Markers from '../components/Markers.tsx'

// Interfaces
import { CityData } from '../interfaces/CityData.ts';


const Map = () => {

    const fetchCityData = () => {
        axios.get('http://localhost:8000/api/v1.0/city/', {
            headers:{
                'X-API-KEY': import.meta.env.VITE_X_API_KEY
            }
        })
            .then(response => setCityData(response.data))
            .catch(error => console.error('Error fetching data:', error))
    }

    // Hooks
    const [cityData, setCityData] = useState<CityData[]>([]);

    useEffect(() => fetchCityData(), []);

    return (
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
            <Markers cityData={ cityData }></Markers>
        </MapContainer>
    )
}

export default Map;