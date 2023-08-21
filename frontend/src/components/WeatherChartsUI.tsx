// Base Imports
import { useEffect, useState } from 'react';

// Third Party Imports
import { useMap } from 'react-leaflet';
import axios from "axios";

// Components
import WeatherChart from "./WeatherChart.tsx";

// Interfaces
import { CityData } from '../interfaces/CityData.ts';
import { WeatherData } from '../interfaces/WeatherData.ts';
interface WeatherChartsUIProps {
    activeCity: CityData | null;
    clearActiveCity: () => void;
}



const WeatherChartsUI = ({ activeCity, clearActiveCity }: WeatherChartsUIProps) => {

    // CALLBACKS
    const fetchWeatherData = () => {
        axios.get(`${import.meta.env.VITE_API_BASE_URL}/weather/${activeCity?.name}/`, {
            headers:{
                'X-API-KEY': import.meta.env.VITE_X_API_KEY
            }
        })
            .then(response => setWeatherData(response.data))
            .catch(error => console.error('Error fetching data:', error))
    }

    // HOOKS
    const [
        weatherData,
        setWeatherData
    ] = useState<WeatherData[]>([]);

    const map = useMap();

    useEffect(() => {
        map.dragging.disable();
        map.doubleClickZoom.disable();
        map.boxZoom.disable();
        map.keyboard.disable();
        map.scrollWheelZoom.disable();
        return () => {
            map.dragging.enable();
            map.doubleClickZoom.enable();
            map.boxZoom.enable();
            map.keyboard.enable();
            map.scrollWheelZoom.enable();
        };
    }, [activeCity]);

    useEffect(() => fetchWeatherData(), []);

    return (
        <div className="map-barrier">
            <div className="chart-row chart-row--header">
                <div className="chart-title-element chart-title-element--left">{ activeCity?.name }</div>
                <div className="chart-title-element chart-title-element--right">
                    <button className="chart-back" onClick={ clearActiveCity }>
                        <span className="chart-back__icon">&larr;</span>
                    </button>
                </div>
            </div>
            { weatherData.length > 0 && (
                <>
                    <div className="chart-row chart-row--main">
                        <WeatherChart
                            weatherData={ weatherData }
                            metricKey="humidity"
                            metricUnits="%"
                            metricColor="#008B8B"
                            position="left-1"
                        />
                        <WeatherChart
                            weatherData={ weatherData }
                            metricKey="precipitation"
                            metricUnits="%"
                            metricColor="#8884d8"
                            position="right-1"
                        />
                    </div>
                    <div className="chart-row chart-row--main">
                        <WeatherChart
                            weatherData={ weatherData }
                            metricKey="temperature"
                            metricUnits="K"
                            metricColor="#FFA500"
                            position="left-2"
                        />
                        <WeatherChart
                            weatherData={ weatherData }
                            metricKey="wind_speed"
                            metricUnits="m/s"
                            metricColor="#008000"
                            position="right-2"
                        />
                    </div>
                </>
            )}
        </div>
    )
}

export default WeatherChartsUI;