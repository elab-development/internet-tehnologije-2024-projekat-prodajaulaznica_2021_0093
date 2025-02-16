// src/components/UtakmiceList.js
import React, { useEffect, useState } from 'react';
import api from '../services/api';

const UtakmiceList = () => {
    const [utakmice, setUtakmice] = useState([]);

    useEffect(() => {
        api.get('/utakmice/')
            .then(response => {
                setUtakmice(response.data);
            })
            .catch(error => {
                console.error("Došlo je do greške pri dobavljanju utakmica!", error);
            });
    }, []);

    return (
        <div>
            <h1>Utakmice</h1>
            <ul>
                {utakmice.map(utakmica => (
                    <li key={utakmica.id}>{utakmica.naziv} - {utakmica.datum}</li>
                ))}
            </ul>
        </div>
    );
};

export default UtakmiceList;