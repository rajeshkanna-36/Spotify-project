import Playlist from '/src/assets/playlist.png'

function Playlist_card({playlist}){

    return(
        <div className="flex items-center w-full h-15 hover:bg-neutral-700/90 rounded-md pl-2">
            <img src={Playlist} className="w-12 h-12 rounded-md"/>
            <h1>{playlist.playlist_name}</h1>
        </div>
    );
}

export default Playlist_card;