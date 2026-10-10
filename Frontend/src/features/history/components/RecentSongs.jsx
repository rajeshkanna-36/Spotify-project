import { useEffect, useState } from "react";
import { getRecentHistory } from "../api";
import SongCard from "../../songs/components/SongCard";

function RecentSongs() {
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
        <section className="mb-8">
            <h2 className="text-white text-2xl font-bold mb-6">
                Recently Played
            </h2>

            <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5 gap-4">
                {recentSongs.slice(0, 8).map((song) => (
                    <SongCard
                        key={song.song_id}
                        song={song}
                    />
                ))}
            </div>
        </section>
    );
}

export default RecentSongs;