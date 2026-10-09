import plus_icon from "../../assets/plus.svg"
import Playlistcard from "../../components/Playlist_card";


function MyPlaylist() {

    const handleCreatePlaylist =()=>{

    }
return ( <section className="pl-5 pt-4 pr-5">
     <div className="flex items-center justify-between"> 
        <h2 className="text-white text-xl font-bold">Your Playlists </h2>

            <button
                type="button"
                aria-label="Create playlist"
                className="flex items-center justify-center w-8 h-8 rounded-full bg-neutral-700 hover:bg-neutral-500" onClick={handleCreatePlaylist}
            >
                <img src={plus_icon} alt="" className="w-5 h-5" />
            </button>

            
        </div>
        <Playlistcard/>
    </section>
);

}

export default MyPlaylist;
