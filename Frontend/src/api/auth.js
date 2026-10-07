import client from "./client";

export const signup =(data)=>{
    return client.post("/auth/signup",data);
}

export const login =(data)=>{
    return client.post("/auth/login",data);
}