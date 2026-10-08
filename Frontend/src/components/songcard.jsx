

//song_card we have to use in homepage recentsongs

function SongCard({song}){
    return(
        <div>
            <img src={song.song_cover_url} alt={song.song_name}/>
            <h3>{song.song_name}</h3>
        </div>
    );
}

export default SongCard;