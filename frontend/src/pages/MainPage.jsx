import React, { useState, useEffect, useContext } from 'react';
import axios from 'axios';
import MatchCard from '../components/MatchCard';
import SortButtons from '../components/SortButtons';
import { UserContext } from '../context/UserContext';
import { useNavigate } from 'react-router-dom';

const MainPage = () => {
  const [matches, setMatches] = useState([]);
  const { user } = useContext(UserContext);
  const navigate = useNavigate();

  const API_URL = "http://127.0.0.1:8000/api/utakmice/";

  useEffect(() => {
    axios.get(API_URL)
      .then(res => setMatches(res.data))
      .catch(err => console.error(err));
  }, []);

  const handleSort = (criteria) => {
    const sortedMatches = [...matches].sort((a, b) => {
      if (criteria === "protivnik") return a.protivnik.localeCompare(b.protivnik);
      if (criteria === "datumVreme") return new Date(a.datumVreme) - new Date(b.datumVreme);
      if (criteria === "lokacija") return a.lokacija.localeCompare(b.lokacija);
      return 0;
    });
    setMatches(sortedMatches);
  };

  const handleBuyTicket = (matchId) => {
    if (!user) {
      alert("Morate biti ulogovani da biste kupili kartu.");
      navigate('/login');
    } else {
      navigate(`/kupovina/${matchId}`);
    }
  };

  return (
    <div className="app">
      <SortButtons onSort={handleSort} />
      <ul className="match-list">
        {matches.map(match => (
          <MatchCard key={match.id} match={match} onBuyTicket={handleBuyTicket} />
        ))}
      </ul>
    </div>
  );
};

export default MainPage;
