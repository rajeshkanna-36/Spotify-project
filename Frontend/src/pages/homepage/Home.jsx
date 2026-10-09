import Navbar from "../../components/navbar";
import CurrentPlay from "./currentplay";
import MyPlaylist from "./MyPlaylist";
import HomeMain from "./HomeMain";

function Home() {
    return (
        <div className="h-screen w-screen overflow-hidden flex flex-col bg-black">
            <Navbar />
            <div className="flex flex-1 overflow-hidden p-2 gap-2 mt-16">
                
                {/* Left Sidebar - Navigation / Library */}
                <aside className="w-[300px] flex-shrink-0 bg-neutral-900 rounded-lg overflow-y-auto hidden md:block">
                    <MyPlaylist />
                </aside>

                {/* Main Content Area */}
                <main className="flex-1 bg-neutral-900 rounded-lg overflow-y-auto">
                    <HomeMain />
                </main>

                {/* Right Sidebar - Now Playing / Activity */}
                <aside className="w-[300px] flex-shrink-0 bg-neutral-900 rounded-lg overflow-y-auto hidden lg:block">
                    <CurrentPlay />
                </aside>
                
            </div>
        </div>
    );
}

export default Home;