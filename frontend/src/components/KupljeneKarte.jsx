import React, { useEffect, useState } from 'react';
import axiosInstance from '../axiosInstance';
import './KupljeneKarte.css';

const KupljeneKarte = () => {
  const [karte, setKarte] = useState([]);

  useEffect(() => {
    const fetchKarte = async () => {
      try {
        const response = await axiosInstance.get('/karte/api/moje-karte/');
        setKarte(response.data);
      } catch (error) {
        console.error("Greška pri učitavanju kupljenih karata:", error);
      }
    };

    fetchKarte();
  }, []);

  const handleDownload = async (id) => {
    try {
      const response = await axiosInstance.get(`/karte/api/karte/preuzmi/${id}/`, {
        responseType: 'blob',
      });

      const url = window.URL.createObjectURL(new Blob([response.data]));
      const link = document.createElement('a');
      link.href = url;
      link.setAttribute('download', `karta_${id}.pdf`);
      document.body.appendChild(link);
      link.click();
      link.remove();
    } catch (error) {
      console.error("Greška pri preuzimanju karte:", error);
    }
  };

  return (
    <div className="kupljene-container">
      <h2 className="kupljene-naslov">Kupljene karte</h2>
      {karte.length === 0 ? (
        <p>Nemate nijednu kupljenu kartu.</p>
      ) : (
        <ul>
          {karte.map((karta) => (
            <li key={karta.id} className="karta-blok">
              <p><strong>Utakmica:</strong> {karta.utakmica}</p>
              <p><strong>Tip karte:</strong> {karta.tip_karte.naziv}</p>
              <p><strong>Cena:</strong> {karta.cena} RSD</p>
              <button className="download-btn" onClick={() => handleDownload(karta.id)}>
                Preuzmi PDF
              </button>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default KupljeneKarte;

