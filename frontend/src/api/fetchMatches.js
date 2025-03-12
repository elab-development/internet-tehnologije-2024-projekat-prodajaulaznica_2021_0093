import axios from 'axios';

const API_URL = "http://127.0.0.1:8000/api/utakmice/";

export const fetchMatches = async () => {
  try {
    const response = await axios.get(API_URL);
    return response.data; // Ovo je niz utakmica u JSON formatu
  } catch (error) {
    console.error("Greška pri učitavanju utakmica:", error);
    return [];
  }
};
