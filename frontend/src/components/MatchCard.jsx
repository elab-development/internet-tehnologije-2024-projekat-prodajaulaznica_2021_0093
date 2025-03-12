import React from 'react';
import './MatchCard.css';

const MatchCard = ({ match, onBuyTicket }) => {
  return (
    <li className="match-card">
      <img src={match.urlSlike} alt={`Utakmica protiv ${match.protivnik}`} width="330" height="180" />
      <div className="match-info">
        <span>Partizan VS {match.protivnik}</span>
        <span className="date">{new Date(match.datumVreme).toLocaleString('sr-RS')}</span>
      </div>
      <button onClick={() => onBuyTicket(match.id)}>Kupi karte</button>
    </li>
  );
};

export default MatchCard;
