import { BrowserRouter, Routes, Route } from "react-router-dom";

import Login from "./components/auth/login"
import Signup from "./components/auth/signup"
import Home from "./components/home/home";



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
 