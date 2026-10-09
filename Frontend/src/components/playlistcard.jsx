import Playlist from '/src/assets/playlist.png';
import { getMyPlaylists, createPlaylist, getPlaylistSongs } from '../api/playlists';
import { useState, useEffect } from 'react';

function Playlist_card() {
  const [playlists, setPlaylists] = useState([]);
  const [newName, setNewName] = useState('');
  const [songs, setSongs] = useState({}); // {playlistId: [song...]}

  // Load playlists on mount
  useEffect(() => {
    const fetchPlaylists = async () => {
      try {
        const data = await getMyPlaylists();
        setPlaylists(data);
      } catch (err) {
        console.error('Failed to load playlists', err);
      }
    };
    fetchPlaylists();
  }, []);

  const handleCreate = async () => {
    if (!newName) return;
    try {
      const result = await createPlaylist(newName);
      // prepend new playlist to list (backend returns id only)
      setPlaylists(prev => [{ playlist_id: result.playlist_id, playlist_name: newName }, ...prev]);
      setNewName('');
    } catch (err) {
      console.error('Create playlist error', err);
    }
  };

  const loadSongs = async (playlistId) => {
    try {
      const data = await getPlaylistSongs(playlistId);
      setSongs(prev => ({ ...prev, [playlistId]: data }));
    } catch (err) {
      console.error('Load songs error', err);
    }
  };

  return (
    <div className="space-y-4 p-4">
      {/* Create playlist */}
      <div className="flex gap-2 items-center">
        <input
          type="text"
          placeholder="New playlist name"
          value={newName}
          onChange={e => setNewName(e.target.value)}
          className="px-2 py-1 rounded bg-gray-800 text-white"
        />
        <button
          onClick={handleCreate}
          className="px-3 py-1 bg-indigo-600 hover:bg-indigo-500 rounded text-white"
        >
          Create
        </button>
      </div>

      {/* Playlist list */}
      {playlists.map(pl => (
        <div key={pl.playlist_id} className="flex flex-col">
          <div className="flex items-center w-full h-15 hover:bg-neutral-700/90 rounded-md pl-2">
            <img src={Playlist} className="w-12 h-12 rounded-md" alt="playlist" />
            <h1 className="ml-2 flex-1">{pl.playlist_name}</h1>
            <button
              onClick={() => loadSongs(pl.playlist_id)}
              className="text-sm text-blue-400 hover:underline"
            >
              Show Songs
            </button>
          </div>
          {/* Recently played songs preview */}
          {songs[pl.playlist_id] && (
            <ul className="ml-14 mt-2 text-sm space-y-1">
              {songs[pl.playlist_id].slice(0, 5).map(song => (
                <li key={song.song_id}>🎵 {song.song_name}</li>
              ))}
            </ul>
          )}
        </div>
      ))}
    </div>
  );
}

export default Playlist_card;