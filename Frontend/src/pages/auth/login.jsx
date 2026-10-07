import { useState } from "react";
import { useNavigate } from "react-router-dom";
import Button from "../../components/button";
import { login } from "../../api/auth";

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


    const handleSubmit = async(e) =>{
        e.preventDefault();

        try{

            const response = await login(formdata);

            localStorage.setItem("access_token", response.data.access_token);

            navigate("/home")
        }catch(error){
            const errormsg = error.response?.data?.detail;
            alert(errormsg || "login failed");
        }

    };

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

            <Button type="submit"> Login </Button>

        </form>

    </div>
    <div >
        <h3>Don't have account?</h3>
    <Button variant="outline" onClick={signup}>Signup</Button>
    </div>
</div>)
};

export default Login;
