import { BrowserRouter, Routes, Route } from "react-router-dom";

import Login from "./pages/auth/login";
import Signup from "./pages/auth/signup";
import Home from "./pages/homepage/home";



function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/login" element ={<Login/>}/>
        <Route path="/signup" element = {<Signup/>}/>
        <Route path="/home" element = {<Home/>}/>
      </Routes>
      
    </BrowserRouter>
  )
}

export default App
 