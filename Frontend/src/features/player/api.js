import client from "../../api/client";

export const getsongplayback= async(song_id)=>{

    const response = await client.get(`/stream/song/${song_id}`);

    return response.data;
};