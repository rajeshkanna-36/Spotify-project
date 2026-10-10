import PlaylistDetail from "./PlaylistDetail";
import Recent from "./Recent";


function HomeMain({playlist}) {
    return (
        <div className="p-6">
            {/* Main scrollable content goes here, grouped in semantic sections */}
            {playlist ?( <PlaylistDetail playlist={playlist}/>) : <Recent/>}
        </div>
    );
}

export default HomeMain;