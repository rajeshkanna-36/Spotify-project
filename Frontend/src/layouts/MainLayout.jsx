import { Outlet } from "react-router-dom";
import Navbar from "../components/common/Navbar";

function MainLayout() {
    return (
        <div className="flex h-screen w-screen flex-col overflow-hidden bg-black">
            <Navbar />
            <Outlet />
        </div>
    );
}

export default MainLayout;