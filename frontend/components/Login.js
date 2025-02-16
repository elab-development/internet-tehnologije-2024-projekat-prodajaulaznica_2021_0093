// src/components/Login.js
import React, { useState } from 'react';
import api from '../services/api';

const Login = () => {
    const [formData, setFormData] = useState({
        username: '',
        password: '',
    });

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await api.post('/token/', formData);  // JWT autentifikacija
            localStorage.setItem('token', response.data.access);  // Sačuvaj token
            console.log("Prijava uspešna!", response.data);
        } catch (error) {
            console.error("Došlo je do greške pri prijavi!", error);
        }
    };

    return (
        <div>
            <h1>Prijava</h1>
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    placeholder="Korisničko ime"
                    value={formData.username}
                    onChange={(e) => setFormData({ ...formData, username: e.target.value })}
                />
                <input
                    type="password"
                    placeholder="Lozinka"
                    value={formData.password}
                    onChange={(e) => setFormData({ ...formData, password: e.target.value })}
                />
                <button type="submit">Prijavi se</button>
            </form>
        </div>
    );
};

export default Login;