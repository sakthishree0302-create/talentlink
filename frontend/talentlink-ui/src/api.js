import axios from "axios";

const api = axios.create({
  baseURL: "https://talentlink-backend-cngj.onrender.com/api/",
});

export default api;
