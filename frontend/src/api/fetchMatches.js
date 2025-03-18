import axios from 'axios';

const API_URL = "http://127.0.0.1:8000/api/utakmice/";

export const fetchMatches = async () => {
  try {
    const response = await axios.get(API_URL, {
      headers: {
        "Content-Type": "application/json",
      },
    });
    return response.data; 
  } catch (error) {
    console.error("Greška pri učitavanju utakmica:", error.response ? error.response.data : error.message);
    return [];
  }
};
