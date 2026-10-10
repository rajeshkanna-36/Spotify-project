import playlistImage from "../../../assets/playlist-cover-placeholder.png";

function PlaylistDetail({playlist}) {
  return (
    <section>
        <img src={playlistImage} alt="" className="w-30 h-30 rounded-md" />
        <h1>{playlist.playlist_name}</h1>
    </section>
  )
}

export default PlaylistDetail;