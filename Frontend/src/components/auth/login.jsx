import { useState } from "react";
import { useNavigate } from "react-router-dom";

function Login(){

     const[formdata,setformdata]= useState({
        email_id : "",
        password : ""
    });

    const handleChange =(e)=>{

        setformdata({
            ...formdata,
            [e.target.name] :e.target.value
    });

    };

    const navigate = useNavigate();

    const signup =(e)=>(
        navigate("/signup")
    );

    const handleSubmit = async (e) => {
    e.preventDefault();

     console.log("Sending:", formdata);

    const response = await fetch("http://localhost:8000/auth/login", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(formdata)
    });

    const result = await response.json();

    console.log("status:", response.status);
    console.log("result:", JSON.stringify(result, null, 2));

    if(response.ok){
        localStorage.setItem("access_token" , result.access_token);
        console.log("sucess");

    };
    }

    return(
        <div className="min-h-screen bg-black flex flex-col items-center justify-center px-4">

    <div className="w-full max-w-md bg-neutral-900 rounded-lg p-10">

        <h1 className="text-white text-3xl font-bold text-center mb-8">
            Log in to Spotify
        </h1>

        <form onSubmit={handleSubmit} className="space-y-5">

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

            <button
                type="submit"
                className="w-full bg-green-500 hover:bg-green-400 text-black font-bold py-3 rounded-full transition"
            >
                Log in
            </button>

        </form>

    </div>
    
    <div className="mt-8 flex flex-col items-center space-y-4">
        <h3 className="text-neutral-400 font-semibold">Don't have an account?</h3>
        <button onClick={signup} className="bg-black border border-neutral-500 hover:bg-white hover:text-black text-white font-bold py-3 px-10 rounded-full transition-colors duration-300">
            Sign up for Spotify
        </button>
    </div>
</div>)
};

export default Login;
