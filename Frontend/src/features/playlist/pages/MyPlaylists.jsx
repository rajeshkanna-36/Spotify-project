import { useEffect, useState } from "react";

import addIcon from "../../../assets/add-icon.svg";
import Modal from "../../../components/ui/Modal";
import PlaylistList from "../components/PlaylistList";

import { createPlaylist, getMyPlaylists } from "../api";

function MyPlaylists({ onSelectPlaylist }) {
    const [playlistName, setPlaylistName] = useState("");
    const [showForm, setShowForm] = useState(false);
    const [playlists, setPlaylists] = useState([]);
    const [isCreating, setIsCreating] = useState(false);

    const refreshPlaylists = async () => {
        try {
            const data = await getMyPlaylists();

            setPlaylists(data || []);

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
                    setPlaylists(data || []);
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

        const name = playlistName.trim();

        if (!name || isCreating) {
            return;
        }

        try {
            setIsCreating(true);

            const response = await createPlaylist(name);

            console.log("Playlist created:", response);

            setPlaylistName("");
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
                    <img src={addIcon} alt="" className="h-5 w-5" />
                </button>
            </div>

            {/* Render playlists */}
            <PlaylistList
                playlists={playlists}
                onSelectPlaylist={onSelectPlaylist}
            />

            {/* Create Playlist Modal */}
            {showForm && (
                <Modal onClose={() => setShowForm(false)}>
                    <form
                        onSubmit={handleSubmit}
                        className="w-80 p-6"
                    >
                        <h2
                            id="create-playlist-title"
                            className="mb-4 text-xl font-bold text-white"
                        >
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
                            value={playlistName}
                            onChange={(e) =>
                                setPlaylistName(e.target.value)
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
                                    setPlaylistName("");
                                }}
                                className="rounded-full px-4 py-2 text-sm text-white hover:bg-neutral-700 disabled:opacity-50"
                            >
                                Cancel
                            </button>

                            <button
                                type="submit"
                                disabled={!playlistName.trim() || isCreating}
                                className="rounded-full bg-green-500 px-4 py-2 text-sm font-bold text-black hover:bg-green-400 disabled:cursor-not-allowed disabled:opacity-50"
                            >
                                {isCreating ? "Creating..." : "Create"}
                            </button>
                        </div>
                    </form>
                </Modal>
            )}
        </section>
    );
}

export default MyPlaylists;