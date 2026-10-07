import axios from "axios";

const client = axios.create({baseURL : "http://localhost:5173",
    headers : {
        "Content-Type" : "appication/json",
    },
});

export default client;