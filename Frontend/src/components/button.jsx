
function Button({children,type = "button",onClick,variant = "primary"}) {

    const variants = {
        primary:
            "bg-green-500 hover:bg-green-400 text-black",

        secondary:
            "bg-white hover:bg-neutral-200 text-black",

        outline:
            "bg-transparent border border-white hover:bg-white hover:text-black text-white",

        danger:
            "bg-red-500 hover:bg-red-400 text-white"
    };

    return (
        <button
            type={type}
            onClick={onClick}
            className={`w-full font-bold py-3 rounded-full transition ${variants[variant]}`}
        >
            {children}
        </button>
    );
}

export default Button;