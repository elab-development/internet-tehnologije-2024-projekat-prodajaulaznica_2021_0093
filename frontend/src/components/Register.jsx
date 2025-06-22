import React, { useState, useContext } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import { UserContext } from '../context/UserContext';
import './Login.css';

const Register = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [email, setEmail] = useState('');
  const [brojKartice, setBrojKartice] = useState('');
  const [error, setError] = useState('');
  const navigate = useNavigate();
  const { login } = useContext(UserContext);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post(
        'http://127.0.0.1:8000/api/register/',
        {
          username,
          password,
          email,
          brojKartice
        },
        {
          headers: {
            'Content-Type': 'application/json'
          }
        }
      );

      const userData = {
        username: response.data.username,
        email: response.data.email
      };

      const accessToken = response.data.access;
      const refreshToken = response.data.refresh;

      // ✅ Poziv login sa sva 3 parametra
      login(userData, accessToken, refreshToken);

      navigate('/');
    } catch (err) {
      console.error(err);
      setError("Greška pri registraciji: " + (err.response?.data?.error || "Nepoznata greška"));
    }
  };

  return (
    <div className="login-container">
      <div className="container">
        <h2>Registracija</h2>
        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label htmlFor="username">Username:</label>
            <input type="text" id="username" value={username} onChange={(e) => setUsername(e.target.value)} required />
          </div>
          <div className="form-group">
            <label htmlFor="password">Lozinka:</label>
            <input type="password" id="password" value={password} onChange={(e) => setPassword(e.target.value)} required />
          </div>
          <div className="form-group">
            <label htmlFor="email">Email:</label>
            <input type="email" id="email" value={email} onChange={(e) => setEmail(e.target.value)} required />
          </div>
          <div className="form-group">
            <label htmlFor="brojKartice">Broj kartice:</label>
            <input type="text" id="brojKartice" value={brojKartice} onChange={(e) => setBrojKartice(e.target.value)} required />
          </div>
          {error && <p className="error">{error}</p>}
          <button type="submit">Registracija</button>
        </form>
      </div>
    </div>
  );
};

export default Register;
