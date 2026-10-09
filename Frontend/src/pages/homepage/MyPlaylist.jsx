import Playlist_card from "../../components/playlistcard";

function MyPlaylist() {
    return (
        <section className="p-4">
            <h2 className="text-white text-xl font-bold mb-6">Your Library</h2>
            <Playlist_card/>
        </section>
    );
}

export default MyPlaylist;