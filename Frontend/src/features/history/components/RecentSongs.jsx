import { useEffect, useState } from "react";
import { getRecentHistory } from "../api";
import SongCard from "../../songs/components/SongCard";
import client from "../../../api/client";

function RecentSongs({ onPlaySong }) {
    const [recentSongs, setRecentSongs] = useState([]);

    useEffect(() => {
        const loadRecentSongs = async () => {
            try {
                const response = await getRecentHistory();
                if (response.data && response.data.length > 0) {
                    setRecentSongs(response.data);
                } else {
                    const fallback = await client.get("/song/");
                    setRecentSongs(fallback.data || []);
                }
            } catch (error) {
                try {
                    const fallback = await client.get("/song/");
                    setRecentSongs(fallback.data || []);
                } catch (fallbackError) {
                    console.error("Failed to load songs:", fallbackError);
                }
            }
        };

        loadRecentSongs();
    }, []);

    return (
        <section className="mb-8">
            <h2 className="text-white text-2xl font-bold mb-6">
                Recently Played
            </h2>

            <div className="grid grid-cols-2 xl:grid-cols-5 gap-4">
                {recentSongs.slice(0, 8).map((song) => (
                    <SongCard
                        key={song.song_id}
                        song={song}
                        onPlay={onPlaySong}
                    />
                ))}
            </div>
        </section>
    );
}

export default RecentSongs;