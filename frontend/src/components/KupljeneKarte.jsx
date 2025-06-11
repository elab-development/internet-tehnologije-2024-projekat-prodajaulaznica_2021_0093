import React, { useContext, useEffect, useState } from 'react';
import { UserContext } from '../context/UserContext';
import axios from 'axios';

const KupljeneKarte = () => {
  const { user } = useContext(UserContext);
  const [karte, setKarte] = useState([]);

  useEffect(() => {
    axios.get(`http://127.0.0.1:8000/api/karte/kupljene/${user.username}/`)
      .then(res => setKarte(res.data))
      .catch(err => console.error(err));
  }, [user]);

  const handlePreuzmi = (id) => {
    window.open(`http://127.0.0.1:8000/api/karte/export-pdf/${id}/`, '_blank');
  };

  return (
    <div>
      <h2>Kupljene karte za: {user.username}</h2>
      <ul>
        {karte.map((karta) => (
          <li key={karta.id}>
            {karta.tip_karte} | {karta.utakmica} | {karta.cena} RSD
            <button onClick={() => handlePreuzmi(karta.id)}>Preuzmi kartu</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default KupljeneKarte;
