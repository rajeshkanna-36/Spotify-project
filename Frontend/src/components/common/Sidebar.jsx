function Sidebar({ children, className = "" }) {
    return (
        <aside className={`overflow-y-auto rounded-lg bg-neutral-900 ${className}`}>
            {children}
        </aside>
    );
}

export default Sidebar;