export interface WeatherData {
    city: number;
    creation_by: string;
    creation_date: string;
    date_time: string;
    humidity: number;
    id: number;
    last_update: string;
    last_update_by: string;
    precipitation: number | null;
    temperature: number | null;
    wind_speed: number | null;
}