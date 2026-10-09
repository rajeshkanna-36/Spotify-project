import playlist_icon from "../assets/playlist.png"

function Playlistcard({playlist_data}) {
  return (
    
    <div className="flex w-full h-16 gap-5 rounded-md hover:bg-neutral-700 mt-5 p-2 items-center">
      <img src={playlist_icon} alt="playlist" className="w-12 h-full rounded-md"/>
      <h2>sample</h2>
    </div>
  )
}

export default Playlistcard