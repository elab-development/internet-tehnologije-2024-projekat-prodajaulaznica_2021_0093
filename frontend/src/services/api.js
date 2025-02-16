import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000/api';  

const api = axios.create({
    baseURL: API_BASE_URL,
    headers: {
        'Content-Type': 'application/json',
    },
});

api.interceptors.request.use((config) => {
    const token = localStorage.getItem('token');  
    if (token) {
        config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
});

export const fetchMatches = async () => {
    try {
        const response = await api.get('/utakmice/');
        return response.data;
    } catch (error) {
        console.error('Došlo je do greške pri dobavljanju utakmica:', error);
        throw error;
    }
};

export const buyTicket = async (id) => {
    try {
        const response = await api.post(`/karte/kupi/${id}/`);
        return response.data;
    } catch (error) {
        console.error('Došlo je do greške pri kupovini karte:', error);
        throw error;
    }
};

export const loginUser = async (username, password) => {
    try {
        const response = await api.post('/token/', { username, password });
        return response.data;
    } catch (error) {
        console.error('Došlo je do greške pri prijavi:', error);
        throw error;
    }
};

export const logoutUser = () => {
    localStorage.removeItem('token');  
};