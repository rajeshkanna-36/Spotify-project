import client from './client';

// for get all playlist //
export const getMyPlaylists = async () => {
  const response = await client.get('/playlist/my_playlist');
  return response.data;
};

// for create playlist //
export const createPlaylist = async (playlistName) => {
  const formData = new FormData();
  formData.append('playlist_name', playlistName);
  // Placeholder image; backend expects a file. Adjust as needed.
  const emptyBlob = new Blob([''], { type: 'image/png' });
  formData.append('playlist_cover_image', emptyBlob, 'placeholder.png');
  const response = await client.post('/playlist/create_playlist', formData, {
    headers: { 'Content-Type': 'multipart/form-data' },
  });
  return response.data;
};

// for add songs at playlist//
export const addSongToPlaylist = async (playlistId, songId, position = 0) => {
  const payload = { playlist_id: playlistId, song_id: songId, position };
  const response = await client.put('/playlist/add_song', payload);
  return response.data;
};

export const getPlaylistSongs = async (playlistId) => {
  const response = await client.get(`/playlist/${playlistId}/songs`);
  return response.data;
};
