// src/components/KarteList.js
import React, { useEffect, useState } from 'react';
import api from '../services/api';

const KarteList = () => {
    const [karte, setKarte] = useState([]);

    useEffect(() => {
        api.get('/karte/')
            .then(response => {
                setKarte(response.data);
            })
            .catch(error => {
                console.error("Došlo je do greške pri dobavljanju karata!", error);
            });
    }, []);

    return (
        <div>
            <h1>Karte</h1>
            <ul>
                {karte.map(karta => (
                    <li key={karta.id}>{karta.naziv} - {karta.cena}</li>
                ))}
            </ul>
        </div>
    );
};

export default KarteList;