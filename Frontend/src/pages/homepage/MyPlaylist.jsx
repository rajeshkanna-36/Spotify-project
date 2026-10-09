import { useEffect, useState } from "react";
import Playlist_card from "../../components/playlistcard";
import { getmyplaylist } from "../../api/playlist";

function MyPlaylist() {

    const[myplaylist,setmyplaylist] = useState([]);

    useEffect(() => {
            const loadrecentplaylist = async () => {
                try {
                    const response = await getmyplaylist();
                    setmyplaylist(response.data);
                    console.log("History response:", response.data);
                } catch (error) {
                    console.error("Failed to load recently played:", error);
                }
            };
    
            loadrecentplaylist();
        }, []);

    return (
        <section className="p-4">
            <h2 className="text-white text-xl font-bold mb-6">Your Library</h2>
            {myplaylist.map((playlist) => (
                    <Playlist_card
                        key={song.song_id}
                        song={song}
                    />
                ))}
        </section>
    );
}

export default MyPlaylist;