import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import axios from 'axios';
import Navbar from './components/NavBar';
import SortButtons from './components/SortButtons';
import MatchCard from './components/MatchCard';
import './App.css';

const App = () => {
  const [matches, setMatches] = useState([]);
  const [user] = useState('test_korisnik'); // Kasnije možeš dohvatiti pravog korisnika
  const API_URL = "http://127.0.0.1:8000/api/utakmice/"; // Pravi API za utakmice

  useEffect(() => {
    const fetchMatches = async () => {
      try {
        const response = await axios.get(API_URL);
        setMatches(response.data);
      } catch (error) {
        console.error("Greška pri učitavanju utakmica:", error);
      }
    };

    fetchMatches();
  }, []);

  const handleSort = (criteria) => {
    console.log("Sortiram po:", criteria);
    const sortedMatches = [...matches].sort((a, b) => {
      if (criteria === "protivnik") return a.protivnik.localeCompare(b.protivnik);
      if (criteria === "datumVreme") return new Date(a.datumVreme) - new Date(b.datumVreme);
      if (criteria === "lokacija") return a.lokacija.localeCompare(b.lokacija);
      return 0;
    });
    setMatches(sortedMatches);
  };

  const handleBuyTicket = (matchId) => {
    console.log("Kupujem kartu za utakmicu ID:", matchId);
    // Ovde možeš dodati logiku kupovine (npr. POST zahtev na backend)
  };

  return (
    <Router>
      <div className="app">
        <Navbar 
          user={user} 
          onLogout={() => console.log("Odjavi se")} 
          onShowTickets={() => console.log("Kupljene karte")} 
        />
        <header className="header">
          <h1>KKartizan</h1>
        </header>
        <SortButtons onSort={handleSort} />
        <Routes>
          <Route 
            path="/" 
            element={
              <ul className="match-list">
                {matches.map(match => (
                  <MatchCard key={match.id} match={match} onBuyTicket={handleBuyTicket} />
                ))}
              </ul>
            } 
          />
        </Routes>
      </div>
    </Router>
  );
};

export default App;
