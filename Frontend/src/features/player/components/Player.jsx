import { useState } from "react"
import play_icon from '../../../assets/play-icon.svg'
import pause_icon from '../../../assets/pause-icon.svg'
function Player() {

     const [play, setPlay] = useState(false);
      const handlePlay = () => { 
        setPlay(!play);
       };
        return ( 
        <section > 
           <button
    onClick={handlePlay}
    className="flex items-center justify-center rounded-full bg-neutral-100 p-2"
>
    <img
        src={play ? pause_icon : play_icon}
        alt={play ? "Pause" : "Play"}
        className="h-5 w-5"
    />
</button>
        </section> 
); }

export default Player