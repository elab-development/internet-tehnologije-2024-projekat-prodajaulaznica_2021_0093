import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';
import './Kupovina.css';

const Kupovina = () => {
  const { matchId } = useParams();
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchKupovina = async () => {
      try {
        const response = await axios.get(`http://127.0.0.1:8000/karte/api/kupovina/${matchId}/`);
        setData(response.data);
      } catch (err) {
        console.error("Greška pri učitavanju:", err);
        setError(err);
      } finally {
        setLoading(false);
      }
    };

    fetchKupovina();
  }, [matchId]);

  if (loading) return <div className="loading">Učitavanje...</div>;
  if (error) return <div className="error">Došlo je do greške.</div>;

  return (
    <div className="kupovina-page">
      <div className="header-info">
        <h1>{data.utakmica}</h1>
        <h3>Lokacija: {data.lokacija}</h3>
      </div>

      <div className="karte-info">
        {data.karte.map((item, index) => (
          <div key={index} className="kartica">
            <div><strong>{item.tip_karte}</strong></div>
            <div>Preostalo: {item.preostalo}</div>
            <div>Cena: {item.cena} RSD</div>
          </div>
        ))}
      </div>

      <div className="kupovina-forma">
        <form>
          <div className="form-group">
            <label>Tip karte:</label>
            <select>
              {data.karte.map((item, index) => (
                <option key={index} value={item.tip_karte}>{item.tip_karte}</option>
              ))}
            </select>
          </div>

          <div className="form-group">
            <label>Broj karata:</label>
            <select>
              {[1, 2, 3, 4].map(broj => (
                <option key={broj} value={broj}>{broj}</option>
              ))}
            </select>
          </div>

          <button type="submit">Kupi karte</button>
        </form>
      </div>
    </div>
  );
};

export default Kupovina;
