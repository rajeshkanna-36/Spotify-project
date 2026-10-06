import { useState } from "react";

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

    const handleSubmit = async(e) =>{
        e.preventDefault();

        const response = await fetch("http://localhost:8000/auth/login", {
            method : "POST",
            headers : {
                "Content-Type": "application/json"
            },

            body : JSON.stringify(formdata)
        });

        const result = await response.json();

        console.log("status:", response.status);
        console.log("result:", JSON.stringify(result, null, 2));
    };

    return(
        <div>
        <h1>Login</h1>
        <form onSubmit={handleSubmit}>
            <div>
                <label>Email ID</label>
                <input type="text" name="email_id" placeholder = "email_id" onChange={handleChange} required />
            </div>

            <div>
                <lable>Password</lable>
                <input type="password" name="password" placeholder = "password" onChange={handleChange} required />
            </div>

            <button type="submit"> login </button>
        </form>
        </div>
    );
};

export default Login;
