
import albumPlaceholder from "../../../assets/playlist-cover-placeholder.png";

function CurrentPlay({ song }) {
    return (
        <section className="p-4 flex flex-col gap-4">
            <h2 className="text-white text-xl font-bold">Now Playing</h2>
            {song ? (
                <div className="flex flex-col gap-3">
                    <img
                        src={song.song_cover_url || albumPlaceholder}
                        alt={song.song_name || "Song cover"}
                        className="w-full aspect-square object-cover rounded-xl shadow-lg"
                    />
                    <div>
                        <h3 className="text-base font-bold text-white truncate">
                            {song.song_name}
                        </h3>
                        <p className="text-xs text-neutral-400 truncate mt-0.5">
                            {song.artist_name || song.artist || "Artist"}
                        </p>
                    </div>
                </div>
            ) : (
                <p className="text-neutral-400 text-sm">Select a song to play</p>
            )}
        </section>
    );
}

export default CurrentPlay;