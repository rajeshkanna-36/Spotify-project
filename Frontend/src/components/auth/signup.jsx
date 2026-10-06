import { useState } from "react";

function Signup(){

    const[formdata,setformdata] = useState({
        user_name : "",
        email : "",
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

        console.log(formdata)

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
                    <input type="email" placeholder="email_id" name="email" onChange={handleChange} required/>
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