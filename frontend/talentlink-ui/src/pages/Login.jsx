import api from "../api";
import { useState } from "react";

export default function Login() {
  const [data, setData] = useState({});

  const login = async () => {
    const res = await api.post("login/", data);
    localStorage.setItem("token", res.data.access);
  };

  return (
    <>
      <input onChange={e=>setData({...data,username:e.target.value})}/>
      <input type="password" onChange={e=>setData({...data,password:e.target.value})}/>
      <button onClick={login}>Login</button>
    </>
  );
}
