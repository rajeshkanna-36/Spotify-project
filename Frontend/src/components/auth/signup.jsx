import { useState } from "react";

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

    const handleSubmit = async(e) =>{
        e.preventDefault();

        console.log("Sending:", formdata);

        const response = await fetch("http://localhost:8000/auth/signup", {
            method: "POST",
            headers: {
                    "Content-Type": "application/json"
                        },
            body: JSON.stringify(formdata)
                });

const result = await response.json();

console.log("status:", response.status);
console.log("result:", JSON.stringify(result, null, 2));

    }

    return(
        <div>
            <h1>SignUp</h1>
            <form onSubmit={handleSubmit}>
                <div>
                    <label>Username</label>
                    <input type="text" placeholder="Username" name="user_name" onChange={handleChange} required/>
                </div>
                <div>
                    <label>Email Id</label>
                    <input type="email" placeholder="email_id" name="email_id" onChange={handleChange} required/>
                </div>

                <div>
                    <label>Password</label>
                    <input type="password" placeholder="password" name="password" onChange={handleChange} required/>
                </div>

                <button type="submit">SignUp</button>
            </form>
        </div>
    );
}

export default Signup;