import React, { useState, useEffect, useContext } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import axios from 'axios';
import { UserContext } from '../context/UserContext';
import './Kupovina.css';

const Kupovina = () => {
  const { matchId } = useParams();
  const navigate = useNavigate();
  const { user } = useContext(UserContext);

  const [utakmica, setUtakmica] = useState(null);
  const [karte, setKarte] = useState([]);
  const [tipKarteId, setTipKarteId] = useState('');
  const [brojKarata, setBrojKarata] = useState(1);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get(`http://127.0.0.1:8000/karte/api/kupovina/${matchId}/`);
        setUtakmica(response.data);
        setKarte(response.data.karte);
      } catch (error) {
        console.error('Greška pri učitavanju:', error);
      }
    };
    fetchData();
  }, [matchId]);

  const handleSubmit = async (e) => {
    e.preventDefault();
  
    try {
      await axios.post('http://127.0.0.1:8000/karte/api/kupovina/kupi/', {
        utakmica_id: parseInt(matchId),
        tip_karte_id: parseInt(tipKarteId),
        broj_karata: parseInt(brojKarata),
        username: user.username
      });
  
      alert("Kupovina uspešna!");
      navigate('/');  // Ovde šaljemo na home page (početak)
    } catch (error) {
      console.error("Greška pri kupovini:", error);
      alert("Greška pri kupovini");
    }
  };


  return (
    <div className="kupovina-container">
      {utakmica ? (
        <>
          <h2>{utakmica.utakmica}</h2>
          <p><strong>Lokacija:</strong> {utakmica.lokacija}</p>

          {karte.map((karta) => (
            <div key={karta.id} className="karta-info">
              <p><strong>{karta.tip_karte}</strong></p>
              <p>Preostalo: {karta.preostalo}</p>
              <p>Cena: {parseFloat(karta.cena).toFixed(2)} RSD</p>
            </div>
          ))}

          <form onSubmit={handleSubmit} className="kupovina-form">
            <div className="form-group">
              <label>Izaberite tip karte:</label>
              <select value={tipKarteId} onChange={(e) => setTipKarteId(parseInt(e.target.value))} required>
              <option value="">-- Odaberite --</option>
                {karte.map((karta) => (
                  <option key={karta.id} value={karta.tip_karte_id}>
                    {karta.tip_karte} - {parseFloat(karta.cena).toFixed(2)} RSD
                  </option>
                ))}
              </select>
            </div>

            <div className="form-group">
              <label>Broj karata:</label>
              <select value={brojKarata} onChange={(e) => setBrojKarata(parseInt(e.target.value))}>
              {[1, 2, 3, 4].map(broj => (
                  <option key={broj} value={broj}>{broj}</option>
                ))}
              </select>
            </div>

            <button type="submit">Potvrdi kupovinu</button>
          </form>
        </>
      ) : (
        <p>Učitavanje podataka o utakmici...</p>
      )}
    </div>
  );
};

export default Kupovina;
