// src/components/Register.js
import React, { useState } from 'react';
import api from '../services/api';

const Register = () => {
    const [formData, setFormData] = useState({
        username: '',
        email: '',
        password: '',
    });

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await api.post('/register/', formData);
            console.log("Registracija uspešna!", response.data);
        } catch (error) {
            console.error("Došlo je do greške pri registraciji!", error);
        }
    };

    return (
        <div>
            <h1>Registracija</h1>
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    placeholder="Korisničko ime"
                    value={formData.username}
                    onChange={(e) => setFormData({ ...formData, username: e.target.value })}
                />
                <input
                    type="email"
                    placeholder="Email"
                    value={formData.email}
                    onChange={(e) => setFormData({ ...formData, email: e.target.value })}
                />
                <input
                    type="password"
                    placeholder="Lozinka"
                    value={formData.password}
                    onChange={(e) => setFormData({ ...formData, password: e.target.value })}
                />
                <button type="submit">Registruj se</button>
            </form>
        </div>
    );
};

export default Register;