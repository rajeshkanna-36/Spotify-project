import { useEffect, useState } from "react";

import plus_icon from "../../assets/plus.svg";
import Playlistcard from "../../components/Playlist_card";

import { createPlaylist, getMyPlaylists } from "../../api/playlist";

function MyPlaylist({ onSelectPlaylist }) {
    const [playlistname, setPlaylistname] = useState("");
    const [showForm, setShowForm] = useState(false);
    const [playlist_data, setplaylist_data] = useState([]);
    const [isCreating, setIsCreating] = useState(false);

    const refreshPlaylists = async () => {
        try {
            const data = await getMyPlaylists();

            setplaylist_data(data || []);

            console.log("Playlists:", data);
        } catch (error) {
            console.error(
                "Failed to load playlists:",
                error.response?.data?.detail || error.message
            );
        }
    };

    // Load playlists when the component mounts
    useEffect(() => {
        let isMounted = true;

        const loadPlaylists = async () => {
            try {
                const data = await getMyPlaylists();

                if (isMounted) {
                    setplaylist_data(data || []);
                }
            } catch (error) {
                console.error(
                    "Failed to load playlists:",
                    error.response?.data?.detail || error.message
                );
            }
        };

        loadPlaylists();

        return () => {
            isMounted = false;
        };
    }, []);

    // Open the create playlist modal
    const handleCreatePlaylist = () => {
        setShowForm(true);
    };

    // Submit the create playlist form
    const handleSubmit = async (e) => {
        e.preventDefault();

        const name = playlistname.trim();

        if (!name || isCreating) {
            return;
        }

        try {
            setIsCreating(true);

            const response = await createPlaylist(name);

            console.log("Playlist created:", response);

            setPlaylistname("");
            setShowForm(false);

            // Refresh the playlist list
            await refreshPlaylists();
        } catch (error) {
            const errorMsg =
                error.response?.data?.detail ||
                "Failed to create playlist";

            alert(errorMsg);
        } finally {
            setIsCreating(false);
        }
    };

    return (
        <section className="pl-5 pt-4 pr-5">
            {/* Playlist heading */}
            <div className="flex items-center justify-between">
                <h2 className="text-white text-xl font-bold">
                    Your Playlists
                </h2>

                <button
                    type="button"
                    aria-label="Create playlist"
                    onClick={handleCreatePlaylist}
                    className="flex h-8 w-8 items-center justify-center rounded-full bg-neutral-700 hover:bg-neutral-500"
                >
                    <img
                        src={plus_icon}
                        alt=""
                        className="h-5 w-5"
                    />
                </button>
            </div>

            {/* Render playlists */}
            {playlist_data.map((playlist) => (
                <Playlistcard
                    key={playlist.playlist_id}
                    playlist={playlist}
                    onSelect={() => onSelectPlaylist(playlist)}
                />
            ))}

            {/* Create Playlist Modal */}
            {showForm && (
                <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/60">
                    <form
                        onSubmit={handleSubmit}
                        className="w-80 rounded-xl bg-neutral-800 p-6 shadow-xl"
                    >
                        <h2 className="mb-4 text-xl font-bold text-white">
                            Create Playlist
                        </h2>

                        <label
                            htmlFor="playlistname"
                            className="mb-2 block text-sm text-neutral-300"
                        >
                            Playlist name
                        </label>

                        <input
                            id="playlistname"
                            type="text"
                            value={playlistname}
                            onChange={(e) =>
                                setPlaylistname(e.target.value)
                            }
                            placeholder="Enter playlist name"
                            maxLength={100}
                            autoFocus
                            className="w-full rounded-md border border-neutral-600 bg-neutral-700 p-3 text-white outline-none focus:border-green-500"
                        />

                        <div className="mt-5 flex justify-end gap-3">
                            <button
                                type="button"
                                disabled={isCreating}
                                onClick={() => {
                                    setShowForm(false);
                                    setPlaylistname("");
                                }}
                                className="rounded-full px-4 py-2 text-sm text-white hover:bg-neutral-700 disabled:opacity-50"
                            >
                                Cancel
                            </button>

                            <button
                                type="submit"
                                disabled={!playlistname.trim() || isCreating}
                                className="rounded-full bg-green-500 px-4 py-2 text-sm font-bold text-black hover:bg-green-400 disabled:cursor-not-allowed disabled:opacity-50"
                            >
                                {isCreating ? "Creating..." : "Create"}
                            </button>
                        </div>
                    </form>
                </div>
            )}
        </section>
    );
}

export default MyPlaylist;