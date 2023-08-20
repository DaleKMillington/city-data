// Base Imports
import { useEffect } from 'react';

// Third Party Imports
import { useMap } from 'react-leaflet';
import L from 'leaflet';

// Interfaces
import { CityData } from '../interfaces/CityData.ts';
interface WeatherChartsProps {
    activeCity: CityData | null;
    clearActiveCity: () => void;
}

const WeatherCharts = ({ activeCity, clearActiveCity }: WeatherChartsProps) => {

    const map = useMap();

    useEffect(() => {
        map.dragging.disable();
        map.doubleClickZoom.disable();
        map.boxZoom.disable();
        map.keyboard.disable();
        map.scrollWheelZoom.disable();
        map.eachLayer(layer => {
            if (layer instanceof L.Marker) {
                layer.unbindTooltip();
            }
        });
        return () => {
            map.dragging.enable();
            map.doubleClickZoom.enable();
            map.boxZoom.enable();
            map.keyboard.enable();
            map.scrollWheelZoom.enable();
        };
    }, [activeCity]);


    return (
        <>
            <div className="map-barrier">
                <div className="chart-row chart-row--header">
                    <div className="chart-title-element chart-title-element--left">{ activeCity?.name }</div>
                    <div className="chart-title-element chart-title-element--right">
                        <button className="chart-back" onClick={ clearActiveCity }>
                            <span className="chart-back__icon">&larr;</span>
                        </button>
                    </div>
                </div>
                <div className="chart-row chart-row--main">
                    <div className="chart-container-element chart-container-element--left-1"></div>
                    <div className="chart-container-element chart-container-element--right-1"></div>
                </div>
                <div className="chart-row chart-row--main">
                    <div className="chart-container-element chart-container-element--left-2"></div>
                    <div className="chart-container-element chart-container-element--right-2"></div>
                </div>
            </div>
            <p onClick={clearActiveCity}>{activeCity?.name}</p>
        </>
    )
}

export default WeatherCharts;