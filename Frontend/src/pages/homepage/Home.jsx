import Navbar from "../../components/navbar";
import CurrentPlay from "./currentplay";
import MyPlaylist from "./MyPlaylist";
import HomeMain from "./HomeMain";
import { useState } from "react";

function Home() {
    const [selectedPlaylist, setSelectedPlaylist] = useState(null);
    return (
        <div className="h-screen w-screen overflow-hidden flex flex-col bg-black">
            <Navbar />
            <div className="flex flex-1 overflow-hidden p-2 gap-2 mt-16">
                
                {/* Left Sidebar - Navigation / Library */}
                <aside className="w-75 shrink-0 bg-neutral-900 rounded-lg overflow-y-auto hidden md:block">
                    <MyPlaylist onSelectPlaylist={setSelectedPlaylist} />
                </aside>

                {/* Main Content Area */}
                <main className="flex-1 bg-neutral-900 rounded-lg overflow-y-auto">
                    <HomeMain playlist={selectedPlaylist} />
                </main>

                {/* Right Sidebar - Now Playing / Activity */}
                <aside className="w-75 shrink-0 bg-neutral-900 rounded-lg overflow-y-auto hidden lg:block">
                    <CurrentPlay />
                </aside>
                
            </div>
        </div>
    );
}

export default Home;