import playlistIcon from "../../../assets/playlist-cover-placeholder.png";

function PlaylistCard({ playlist, onSelect }) {
  const title = playlist?.playlist_name || "Untitled Playlist";

      
  return (
    <button onClick={onSelect}
    className="mt-5 flex h-16 w-full items-center gap-5 rounded-md p-2 hover:bg-neutral-700" >
      <img
        src={playlistIcon}
        alt="playlist"
        className="h-full w-12 rounded-md"
      />
      <h2 className="text-sm font-medium text-white">{title}</h2>
    </button>
  );
}

export default PlaylistCard;