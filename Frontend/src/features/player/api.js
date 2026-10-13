const API_BASE = "http://localhost:8000";

export const getStreamUrl = (songId) => {
    if (!songId) return "";
    const token = localStorage.getItem("access_token");
    if (token && token !== "null" && token !== "undefined") {
        return `${API_BASE}/stream/song/${songId}?token=${encodeURIComponent(token)}`;
    }
    return `${API_BASE}/stream/song/${songId}`;
};