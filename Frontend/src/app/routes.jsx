import { Route, Routes } from "react-router-dom";
import Login from "../features/auth/pages/Login";
import Signup from "../features/auth/pages/Signup";
import Home from "../pages/Home";
import MainLayout from "../layouts/MainLayout";

function AppRoutes() {
    return (
        <Routes>
            <Route path="/login" element={<Login />} />
            <Route path="/signup" element={<Signup />} />
            <Route element={<MainLayout />}>
                <Route path="/home" element={<Home />} />
            </Route>
        </Routes>
    );
}

export default AppRoutes;