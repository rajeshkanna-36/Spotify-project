import client from "../../api/client";

// for get all playlist //
export const getMyPlaylists = async () => {
  const response = await client.get('/playlist/my_playlist');
  return response.data;
};

export const createPlaylist = async (playlistName) => {
  const formData = new FormData();
  formData.append("playlist_name", playlistName);

  const response = await client.post("/playlist/create_playlist", formData, {
    headers: {
      "Content-Type": "multipart/form-data",
    },
  });

  return response.data;
};

export const getallplaylist_songs = async(playlist_id)=>{
    const response = await client.get(`/playlist/${playlist_id}/songs`);

    return response.data;
}