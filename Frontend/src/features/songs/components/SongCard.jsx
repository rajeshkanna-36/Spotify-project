

//song_card we have to use in homepage recentsongs


function SongCard({ song }) {

    return (
        <div className="flex w-full h-15 bg-neutral-700 gap-3 rounded-xl px-4 items-center font-bold text-white">
            <img
                src={song.song_cover_url}
                alt={song.song_name}
                className="w-10 h-10 rounded-md object-cover"
            />

            <h3 className="truncate">
                {song.song_name}
            </h3>
        </div>
    );
}

export default SongCard;