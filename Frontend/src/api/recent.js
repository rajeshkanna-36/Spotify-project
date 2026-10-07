import client from "./client"

export const Recent_home =()=>{
    return response = client.get("history/my_history");
}