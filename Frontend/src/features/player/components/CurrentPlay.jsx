import dummyimage from '../../../assets/playlist-cover-placeholder.png'

function CurrentPlay() {
    return (
        <section className="p-4">
            <h2 className="text-white text-xl font-bold mb-6">Now Playing</h2>
            <img src={dummyimage} alt="song" className="w-full h-60 rounded-md"/>
            <h1 className="font-bold text-3xl mt-2">Song Name</h1>
        </section>
    );
}

export default CurrentPlay;