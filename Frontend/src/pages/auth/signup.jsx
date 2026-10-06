import { useState } from "react";
import { useNavigate } from "react-router-dom";
import Button from "../../components/button";

function Signup(){

    const[formdata,setformdata] = useState({
        user_name : "",
        email_id : "",
        password : ""
    });

    const handleChange = (e) => {
        setformdata({
            ...formdata,
            [e.target.name] : e.target.value
    });
    };

    const navigate = useNavigate();
    const login =(e) =>{
        navigate("/login")
    };

    const handleSubmit = async(e) =>{
        e.preventDefault();

        const response = await fetch("http://localhost:8000/auth/signup", {
            method: "POST",
            headers: {
                    "Content-Type": "application/json"
                        },
            body: JSON.stringify(formdata)
                });

        const result = await response.json();
        
        if(response.ok){
            navigate("/home")
        } else {
            const errorMsg = Array.isArray(result.detail) ? result.detail[0].msg : result.detail;
            alert(errorMsg || "Signup failed");
        }
    };

    return(
        <div className="min-h-screen bg-black flex flex-col items-center justify-center px-4">

        <div className="w-full max-w-md bg-neutral-900 rounded-lg p-10">

        <h1 className="text-white text-3xl font-bold text-center mb-8">
            Sign up for Spotify
        </h1>

        <form onSubmit={handleSubmit} className="space-y-5">

            <div>
                <label
                    htmlFor="user_name"
                    className="block text-white text-sm font-bold mb-2"
                >
                    Username
                </label>

                <input
                    id="user_name"
                    type="text"
                    name="user_name"
                    placeholder="Username"
                    onChange={handleChange}
                    required
                    className="w-full bg-neutral-800 border border-neutral-600 rounded-md px-4 py-3 text-white placeholder-neutral-400 outline-none focus:border-white"
                />
            </div>

            <div>
                <label
                    htmlFor="email_id"
                    className="block text-white text-sm font-bold mb-2"
                >
                    Email address
                </label>

                <input
                    id="email_id"
                    type="email"
                    name="email_id"
                    placeholder="Email address"
                    onChange={handleChange}
                    required
                    className="w-full bg-neutral-800 border border-neutral-600 rounded-md px-4 py-3 text-white placeholder-neutral-400 outline-none focus:border-white"
                />
            </div>

            <div>
                <label
                    htmlFor="password"
                    className="block text-white text-sm font-bold mb-2"
                >
                    Password
                </label>

                <input
                    id="password"
                    type="password"
                    name="password"
                    placeholder="Password"
                    onChange={handleChange}
                    required
                    className="w-full bg-neutral-800 border border-neutral-600 rounded-md px-4 py-3 text-white placeholder-neutral-400 outline-none focus:border-white"
                />
            </div>

            <Button type="submit">Signup</Button>

        </form>

    </div>
    
    <div >
        <h3>Already have a account?</h3>
    <Button variant="outline" onClick={login}>Login</Button>
    </div>
</div>
    );
}

export default Signup;