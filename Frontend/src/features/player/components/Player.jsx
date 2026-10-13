import albumPlaceholder from '../../../assets/playlist-cover-placeholder.png'
import playIcon from '../../../assets/play-icon.svg'
import pauseIcon from '../../../assets/pause-icon.svg'
import prevIcon from '../../../assets/previous-icon.svg'
import nextIcon from '../../../assets/next-icon.svg'
import { useEffect, useRef, useState } from 'react'
import { getStreamUrl } from '../api'

function Player({ song }) {
    const [isPlaying, setIsPlaying] = useState(false);
    const [currentTime, setCurrentTime] = useState(0);
    const [duration, setDuration] = useState(0);
    const [volume, setVolume] = useState(0.75);
    const audioRef = useRef(null);

    const streamUrl = song?.song_url || (song?.song_id ? getStreamUrl(song.song_id) : '');

    // Auto-play when song changes
    useEffect(() => {
        const audio = audioRef.current;
        if (!audio) return;

        if (song?.song_id) {
            audio.currentTime = 0;
            audio.load();
            const playPromise = audio.play();
            if (playPromise !== undefined) {
                playPromise
                    .then(() => setIsPlaying(true))
                    .catch((err) => {
                        console.log("Autoplay blocked or waiting for user interaction:", err);
                        setIsPlaying(false);
                    });
            }
        } else {
            audio.pause();
            setIsPlaying(false);
            setCurrentTime(0);
        }
    }, [song?.song_id]);

    const handlePlayPause = () => {
        const audio = audioRef.current;
        if (!audio || !song) return;

        if (audio.paused) {
            const playPromise = audio.play();
            if (playPromise !== undefined) {
                playPromise
                    .then(() => setIsPlaying(true))
                    .catch((err) => {
                        console.error("Playback failed:", err);
                        setIsPlaying(false);
                    });
            }
        } else {
            audio.pause();
            setIsPlaying(false);
        }
    };

    const handleTimeUpdate = () => {
        if (audioRef.current) {
            setCurrentTime(audioRef.current.currentTime);
        }
    };

    const handleLoadedMetadata = () => {
        if (audioRef.current) {
            setDuration(audioRef.current.duration);
        }
    };

    const handleEnded = () => {
        setIsPlaying(false);
        setCurrentTime(0);
    };

    const handleSeek = (e) => {
        if (!audioRef.current || !duration) return;
        const rect = e.currentTarget.getBoundingClientRect();
        const clickX = e.clientX - rect.left;
        const newTime = (clickX / rect.width) * duration;
        audioRef.current.currentTime = newTime;
        setCurrentTime(newTime);
    };

    const handleVolumeChange = (e) => {
        const rect = e.currentTarget.getBoundingClientRect();
        const clickX = Math.max(0, Math.min(e.clientX - rect.left, rect.width));
        const newVol = clickX / rect.width;
        setVolume(newVol);
        if (audioRef.current) {
            audioRef.current.volume = newVol;
        }
    };

    const formatTime = (seconds) => {
        if (!seconds || isNaN(seconds)) return "0:00";
        const mins = Math.floor(seconds / 60);
        const secs = Math.floor(seconds % 60);
        return `${mins}:${secs < 10 ? '0' : ''}${secs}`;
    };

    const progressPercentage = duration ? (currentTime / duration) * 100 : 0;

    return (
        <section className="w-full grid grid-cols-3 items-center px-4 py-2">

            {/* Left — Song Info */}
            <div className="flex items-center gap-3 min-w-0">
                <img
                    src={song?.song_cover_url || albumPlaceholder}
                    alt={song?.song_name || "Album art"}
                    className="w-14 h-14 rounded-md object-cover shadow-lg"
                />
                <div className="min-w-0">
                    <p className="text-sm font-semibold text-white truncate">
                        {song?.song_name || "No song playing"}
                    </p>
                    <p className="text-xs text-neutral-400 truncate">
                        {song?.artist_name || song?.artist || "Artist"}
                    </p>
                </div>
            </div>

            {/* Center — Playback Controls + Progress */}
            <div className="flex flex-col items-center gap-1">
                {/* Control buttons */}
                <div className="flex items-center gap-5">
                    <button className="hover:brightness-125 transition cursor-pointer">
                        <img src={prevIcon} alt="Previous" className="w-5 h-5" />
                    </button>

                    <button 
                        onClick={handlePlayPause} 
                        className="flex items-center justify-center w-9 h-9 bg-white rounded-full hover:scale-105 transition cursor-pointer"
                        title={isPlaying ? "Pause" : "Play"}
                    >
                        <img 
                            src={isPlaying ? pauseIcon : playIcon} 
                            alt={isPlaying ? "Pause" : "Play"} 
                            className="w-4 h-4" 
                        />
                    </button>

                    <button className="hover:brightness-125 transition cursor-pointer">
                        <img src={nextIcon} alt="Next" className="w-5 h-5" />
                    </button>
                </div>

                {/* Progress bar */}
                <div className="flex items-center gap-2 w-full max-w-md">
                    <span className="text-[11px] text-neutral-400 tabular-nums w-8 text-right">
                        {formatTime(currentTime)}
                    </span>
                    <div 
                        onClick={handleSeek}
                        className="relative flex-1 h-1 bg-neutral-600 rounded-full group cursor-pointer"
                    >
                        <div 
                            className="absolute inset-y-0 left-0 bg-white rounded-full group-hover:bg-green-500 transition-colors" 
                            style={{ width: `${progressPercentage}%` }}
                        />
                        <div 
                            className="absolute top-1/2 -translate-y-1/2 w-3 h-3 bg-white rounded-full opacity-0 group-hover:opacity-100 transition-opacity shadow" 
                            style={{ left: `${progressPercentage}%` }}
                        />
                    </div>
                    <span className="text-[11px] text-neutral-400 tabular-nums w-8">
                        {formatTime(duration)}
                    </span>
                </div>
            </div>

            {/* Right — Volume */}
            <div className="flex items-center justify-end gap-2">
                {/* Speaker icon (inline SVG so we control the color) */}
                <svg
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 24 24"
                    fill="currentColor"
                    className="w-4 h-4 text-neutral-400"
                >
                    <path d="M11.383 3.07A1 1 0 0 1 12 4v16a1 1 0 0 1-1.617.784L5.131 16H2a1 1 0 0 1-1-1V9a1 1 0 0 1 1-1h3.131l5.252-4.784a1 1 0 0 1 1 .07ZM14.293 8.293a1 1 0 0 1 1.414 0 5 5 0 0 1 0 7.072 1 1 0 1 1-1.414-1.415 3 3 0 0 0 0-4.242 1 1 0 0 1 0-1.415Zm3.536-2.828a1 1 0 0 1 1.414 0 9 9 0 0 1 0 12.728 1 1 0 1 1-1.414-1.414 7 7 0 0 0 0-9.9 1 1 0 0 1 0-1.414Z" />
                </svg>

                <div 
                    onClick={handleVolumeChange}
                    className="relative w-24 h-1 bg-neutral-600 rounded-full group cursor-pointer"
                >
                    <div 
                        className="absolute inset-y-0 left-0 bg-white rounded-full group-hover:bg-green-500 transition-colors" 
                        style={{ width: `${volume * 100}%` }}
                    />
                    <div
                        className="absolute top-1/2 -translate-y-1/2 w-3 h-3 bg-white rounded-full opacity-0 group-hover:opacity-100 transition-opacity shadow"
                        style={{ left: `${volume * 100}%` }}
                    />
                </div>
            </div>

            <audio 
                ref={audioRef} 
                src={streamUrl}
                preload="auto"
                onPlay={() => setIsPlaying(true)}
                onPause={() => setIsPlaying(false)}
                onTimeUpdate={handleTimeUpdate}
                onLoadedMetadata={handleLoadedMetadata}
                onEnded={handleEnded}
                onError={(e) => {
                    console.error("Audio error on playing stream:", e);
                    setIsPlaying(false);
                }}
            />

        </section>
    );
}

export default Player;