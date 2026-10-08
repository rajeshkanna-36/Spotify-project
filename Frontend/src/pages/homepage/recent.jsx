import { useEffect, useState } from "react";
import {getRecentHistory} from '/src/api/recent.js';
import SongCard from "../../components/songcard";

function Recents() {

    
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
        <div className="bg-neutral-800 h-[570px] w-[620px] rounded-xl p-6">

    <h1 className="text-white text-xl font-bold mb-6">
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

export default Recents;