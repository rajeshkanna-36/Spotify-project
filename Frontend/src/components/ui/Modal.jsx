function Modal({ children, onClose }) {
    const handleBackdropClick = (event) => {
        if (event.target === event.currentTarget) {
            onClose?.();
        }
    };

    return (
        <div
            className="fixed inset-0 z-50 flex items-center justify-center bg-black/60"
            onMouseDown={handleBackdropClick}
        >
            <div
                role="dialog"
                aria-modal="true"
                aria-labelledby="create-playlist-title"
                className="rounded-xl bg-neutral-800 shadow-xl"
            >
                {children}
            </div>
        </div>
    );
}

export default Modal;