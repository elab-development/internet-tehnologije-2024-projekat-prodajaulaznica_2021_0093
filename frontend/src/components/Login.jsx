import React, { useState, useContext } from 'react';
import { useNavigate } from 'react-router-dom';
import axiosInstance from '../axiosInstance';
import { UserContext } from '../context/UserContext';
import './Login.css';

const Login = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const navigate = useNavigate();
  const { login } = useContext(UserContext); // koristi login iz konteksta

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axiosInstance.post('/api/token/', {
        username,
        password,
      });

      const { access, refresh } = response.data;
      login({ username }, access, refresh); // koristi context login
      navigate('/');
    } catch (error) {
      console.error('Greška pri loginu:', error);
      setError('Pogrešno korisničko ime ili lozinka.');
    }
  };

  return (
    <div className="login-container">
      <div className="container">
        <h2>Login korisnika</h2>
        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label htmlFor="username">Username:</label>
            <input
              type="text"
              id="username"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              required
            />
          </div>
          <div className="form-group">
            <label htmlFor="password">Lozinka:</label>
            <input
              type="password"
              id="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
            />
          </div>
          {error && <p className="error">{error}</p>}
          <button type="submit">Login</button>
        </form>
        <p>Nemate nalog? <a href="/register">Kliknite ovde za registraciju</a></p>
      </div>
    </div>
  );
};

export default Login;
