import Playlist_image from "../../assets/playlist.png";

function PlaylistDetail({playlist}) {
  return (
    <section>
        <img src={Playlist_image} className="w-30 h-30 rounded-md"/>
        <h1>{playlist.playlist_name}</h1>
    </section>
  )
}

export default PlaylistDetail;