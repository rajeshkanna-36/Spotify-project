import Search from './search';
import logo from '/src/assets/image.png';
import home from '/src/assets/home.svg'

function Navbar(){

    return(
        <div >
            <nav className= "fixed top-0 left-0 w-full bg-black h-16 flex items-center gap-4 px-5 py-3">
                <img src={logo} alt='logo' className=" h-9 w-9 "/>
                <button className="w-12 h-12 bg-neutral-800/50 rounded-full flex justify-center items-center">
                    <img src={home} alt='logo' className=" h-7 w-7 "/>
                </button>
                <Search/>
                <a className = "h-9 w-9 bg-pink-600 rounded-full flex justify-center items-center">
                    R
                </a>
            </nav>

        </div>
    );
}

export default Navbar;