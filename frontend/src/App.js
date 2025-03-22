import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route, useNavigate, useLocation } from 'react-router-dom';
import axios from 'axios';
import Navbar from './components/NavBar';
import SortButtons from './components/SortButtons';
import MatchCard from './components/MatchCard';
import Login from './components/Login';
import Register from './components/Register';
import './App.css';

// Glavna komponenta koja koristi useLocation
const MainApp = () => {
  const location = useLocation(); // Koristi useLocation ovde
  const [matches, setMatches] = useState([]);
  const [user, setUser] = useState(null);
  const API_URL = "http://127.0.0.1:8000/api/utakmice/";
  const LOGIN_API_URL = "http://127.0.0.1:8000/accounts/login/";
  const REGISTER_API_URL = "http://127.0.0.1:8000/accounts/register/";

  useEffect(() => {
    const fetchMatches = async () => {
      try {
        const response = await axios.get(API_URL);
        setMatches(response.data);
      } catch (error) {
        console.error("Error loading matches:", error);
      }
    };

    fetchMatches();
  }, []);

  const handleSort = (criteria) => {
    const sortedMatches = [...matches].sort((a, b) => {
      if (criteria === "protivnik") {
        return a.protivnik?.localeCompare(b.protivnik || '') || 0;
      }
      if (criteria === "datumVreme") {
        return new Date(a.datumVreme) - new Date(b.datumVreme);
      }
      if (criteria === "lokacija") {
        return a.lokacija?.localeCompare(b.lokacija || '') || 0;
      }
      return 0;
    });
    setMatches(sortedMatches);
  };

  const handleLogin = async (username, password) => {
    try {
      const response = await axios.post(LOGIN_API_URL, { username, password });
      if (response.data.success) {
        setUser(response.data.user);
        localStorage.setItem('user', JSON.stringify(response.data.user));
        return true;
      }
    } catch (error) {
      console.error("Login error:", error);
    }
    return false;
  };

  const handleRegister = async (username, password, email, brojKartice) => {
    try {
      const response = await axios.post(REGISTER_API_URL, { username, password, email, brojKartice });
      if (response.data.success) {
        setUser({ username });
        localStorage.setItem('user', JSON.stringify({ username }));
        return true;
      }
    } catch (error) {
      console.error("Registration error:", error);
    }
    return false;
  };

  const handleLogout = () => {
    setUser(null);
    localStorage.removeItem('user');
  };

  const handleShowTickets = () => {
    console.log("Prikaz kupljenih karata");
    // Dodaj logiku za prikaz kupljenih karata
  };

  useEffect(() => {
    const storedUser = localStorage.getItem('user');
    if (storedUser) {
      setUser(JSON.parse(storedUser));
    }
  }, []);

  const MatchList = () => {
    const navigate = useNavigate();

    const handleBuyTicket = (matchId) => {
      if (user) {
        navigate(`/kupovina/${matchId}`);
      } else {
        navigate('/login');
      }
    };

    return (
      <ul className="match-list">
        {matches.map(match => (
          <MatchCard 
            key={match.id} 
            match={match} 
            onBuyTicket={handleBuyTicket} 
          />
        ))}
      </ul>
    );
  };

  const isLoginOrRegisterPage = location.pathname === '/login' || location.pathname === '/register';

  return (
    <div className="app">
      {user && <Navbar user={user.username} onLogout={handleLogout} onShowTickets={handleShowTickets} />}
      <header className="header">
        <h1>KKartizan</h1>
      </header>
      {!isLoginOrRegisterPage && <SortButtons onSort={handleSort} />}
      <Routes>
        <Route path="/" element={<MatchList />} />
        <Route path="/kupovina/:matchId" element={<div>Page for purchasing ticket</div>} />
        <Route path="/login" element={<Login onLogin={handleLogin} />} />
        <Route path="/register" element={<Register onRegister={handleRegister} />} />
      </Routes>
    </div>
  );
};

// Glavna App komponenta koja omotava MainApp u <Router>
const App = () => {
  return (
    <Router>
      <MainApp />
    </Router>
  );
};

export default App;