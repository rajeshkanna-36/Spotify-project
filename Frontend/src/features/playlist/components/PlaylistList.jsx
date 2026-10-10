import PlaylistCard from "./PlaylistCard";

function PlaylistList({ playlists, onSelectPlaylist }) {
    return playlists.map((playlist) => (
        <PlaylistCard
            key={playlist.playlist_id}
            playlist={playlist}
            onSelect={() => onSelectPlaylist(playlist)}
        />
    ));
}

export default PlaylistList;