import { useState } from "react";
import Sidebar from "../components/common/Sidebar";
import CurrentPlay from "../features/player/components/CurrentPlay";
import RecentSongs from "../features/history/components/RecentSongs";
import PlaylistDetail from "../features/playlist/components/PlaylistDetail";
import MyPlaylists from "../features/playlist/pages/MyPlaylists";
import Player from "../features/player/components/player";

function Home() {
    const [selectedPlaylist, setSelectedPlaylist] = useState(null);

    return (
        <div>
        <div className="mt-16 flex flex-1 gap-2 overflow-hidden h-120 p-2">
            <Sidebar className="hidden w-75 shrink-0 md:block">
                <MyPlaylists onSelectPlaylist={setSelectedPlaylist} />
            </Sidebar>

            <main className="flex-1 overflow-y-auto rounded-lg bg-neutral-900 p-6">
                {selectedPlaylist ? (
                    <PlaylistDetail playlist={selectedPlaylist} />
                ) : (
                    <RecentSongs />
                )}
            </main>

            <Sidebar className="hidden w-75 shrink-0 p-4 lg:block">
                <CurrentPlay />
            </Sidebar>
        </div>
        <div className="shrink-0 flex items-center justify-center h-20 p-3"> 
            <Player /> 
        </div>
        </div>

    );
}

export default Home;