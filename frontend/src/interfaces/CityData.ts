// Interface representing single element from api/v1.0/city/
export interface CityData {
    creation_by: string,
    creation_date: string,
    id: number,
    last_update: string,
    last_update_by: string,
    latitude: number,
    longitude: number,
    name: string
}
