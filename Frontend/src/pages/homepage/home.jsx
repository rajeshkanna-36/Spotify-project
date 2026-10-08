import Navbar from "../../components/navbar";
import Current_play_info from "./currentplay";
import MyPlaylist from "./myplaylist";
import Recents from "./recent";

function Home(){
    return(
        <div>
        <Navbar/>
        <div className="flex ml-5 gap-5 py-2 ">
        <MyPlaylist/>
        <Recents/>
        <Current_play_info/>
        </div>
        </div>
    );
};

export default Home;