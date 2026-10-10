import { useEffect, useState } from "react";
import playlistImage from "../../../assets/playlist-cover-placeholder.png";
import { getallplaylist_songs } from "../api";
import SongCard from "../../songs/components/SongCard";

function PlaylistDetail({playlist}) {
  const[PlaylistSongs,setPlaylistSongs] = useState([]);

  useEffect(() => { if (!playlist?.playlist_id) return; 
    const getPlaylistDetails = async () => { 
      try { const response = await getallplaylist_songs( playlist.playlist_id ); 
        setPlaylistSongs(response); 
      } catch (error) { 
        console.error("Failed to fetch playlist songs:", error); 
      } 
    }; getPlaylistDetails(); 
  }, [playlist?.playlist_id]);


  return (
    <section>
      <div className="flex text-7xl font-bold items-center gap-4">
        <img src={playlistImage} alt="" className="w-30 h-30 rounded-md" />
        <h1>{playlist.playlist_name}</h1>
      </div>
      
      <div>
      {PlaylistSongs.map((song) => (
         <SongCard key={song.song_id} 
         song={song} /> 
         )
        )}
      </div>
    </section>
  )
}

export default PlaylistDetail;