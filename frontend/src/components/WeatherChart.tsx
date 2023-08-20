// Base Imports

// Third Party Imports
import { AreaChart, Area, XAxis, YAxis, Label, Tooltip, ResponsiveContainer } from 'recharts';

// Interfaces
import { WeatherData } from '../interfaces/WeatherData.ts';
interface WeatherChartProps {
    weatherData: WeatherData[];
    metricKey: string;
    metricUnits: string;
    metricColor: string;
    position: string;
}

const WeatherChart = ({ weatherData, metricKey, metricUnits, metricColor, position }: WeatherChartProps) => {

    const containerClasses = `chart-container-element chart-container-element--${position}`;

    return (
        <div className={ containerClasses }>
            <div className="chart-container-element__title">
                { metricKey.replace('_', ' ') }
            </div>
            <div className="chart-container-element__chart">
                <ResponsiveContainer height={ "100%" } width={"100%"}>
                    <AreaChart data={ weatherData } margin={{ top: 20, right: 30, left: 20, bottom: 40 }}>
                        <defs>
                            <linearGradient id={metricKey} x1="0" y1="0" x2="0" y2="1">
                                <stop offset="5%" stopColor={ metricColor } stopOpacity={ 0.8 }/>
                                <stop offset="95%" stopColor={ metricColor } stopOpacity={ 0.2 }/>
                            </linearGradient>
                        </defs>
                        <YAxis tick={{ fontSize: 14, fill: "#f7f7f7" }}>
                            <Label
                                value={ metricUnits }
                                angle={ -90 }
                                position="center"
                                dx={ -20 }
                                style={{
                                    fontSize: 16,
                                    fontWeight: "bold",
                                    fill: "#f7f7f7"
                                }}
                            />
                        </YAxis>
                        <XAxis dataKey="date_time" hide />
                        <Tooltip
                            contentStyle={{
                                backgroundColor: "white",
                                borderRadius: "5px",
                                fontSize: "18px",
                                fontWeight: "bold",
                                border: "none",
                                opacity: "0.8",
                                boxShadow: "0 2px 4px rgba(0, 0, 0, 0.1)",
                            }}
                            labelStyle={{
                                color: "#333",
                                fontWeight: "bold",
                                fontSize: "18px",
                            }}
                            labelFormatter={(value) => {
                                return new Date(value).toLocaleString("en-GB", {
                                    year: "numeric",
                                    month: "long",
                                    day: "numeric",
                                    hour: "numeric",
                                    minute: "numeric"
                                })
                            }}
                        />
                        <Area
                            type="monotone"
                            dataKey={ metricKey }
                            stroke={ metricColor }
                            fillOpacity={ 1 }
                            fill={ `url(#${metricKey})` }
                        />
                    </AreaChart>
                </ResponsiveContainer>
            </div>
        </div>
    )
}

export default WeatherChart;