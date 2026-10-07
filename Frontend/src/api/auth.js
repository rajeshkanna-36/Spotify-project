import client from "./client";

export const signup =(data)=>{
    return client.post("/signup",data);
}

export const login =(data)=>{
    return client.post("/login",data);
}