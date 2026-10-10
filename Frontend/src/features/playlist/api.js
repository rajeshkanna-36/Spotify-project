import client from "../../api/client";

// for get all playlist //
export const getMyPlaylists = async () => {
  const response = await client.get('/playlist/my_playlist');
  return response.data;
};

export const createPlaylist = async(formdata) => {
  const response = await client.post("/playlist/create_playlist", formdata);

  return response.data;
};