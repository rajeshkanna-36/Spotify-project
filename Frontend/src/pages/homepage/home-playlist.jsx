import { useEffect, useState } from "react";
import {getRecentHistory} from '/src/api/recent.js';
import SongCard from "../../components/songcard";

function HomePlaylist() {

    
    const [recentSongs, setRecentSongs] = useState([]);

    useEffect(() => {

        const loadRecentSongs = async () => {
            try {
                const response = await getRecentHistory();

                setRecentSongs(response.data);
                console.log("History response:", response.data);
            } catch (error) {
                console.error("Failed to load recently played:", error);
            }
        };

        loadRecentSongs();

    }, []);

    return (
        <div className="bg-neutral-800 h-[560px] w-[640px] rounded-xl ml-80 p-6">

    <h1 className="text-white text-2xl font-bold mb-6">
        Recent
    </h1>

    <div className="grid grid-cols-2 gap-4">
        {recentSongs.slice(0, 8).map((song) => (
            <SongCard
                key={song.song_id}
                song={song}
            />
        ))}
    </div>

</div>
    )}

export default HomePlaylist;