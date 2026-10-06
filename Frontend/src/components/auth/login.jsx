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

    const handleSubmit =(e) =>{
        e.preventDefault();

        console.log(formdata)
    };

    return(
        <div>
        <h1>Login</h1>
        <form onSubmit={handleSubmit}>
            <div>
                <label>Email ID</label>
                <input type="email" name="emaill_id" placeholder = "email_id" onChange={handleChange} required />
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
