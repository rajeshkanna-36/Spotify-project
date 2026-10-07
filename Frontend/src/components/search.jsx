import searchicon from "/src/assets/icons8-search (1).svg";

function Search() {
    return (
        <div className="w-80 h-12 bg-neutral-800 rounded-full px-5 flex items-center gap-3">
            <img
                src={searchicon}
                alt="search"
                className="w-6 h-6"
            />

            <input
                type="text"
                placeholder="Search for your Vibe"
                className="flex-1 bg-transparent outline-none text-white placeholder-neutral-400"
            />
        </div>
    );
}

export default Search;