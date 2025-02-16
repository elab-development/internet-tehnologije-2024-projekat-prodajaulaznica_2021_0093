import React, { useEffect, useState } from 'react';
import { fetchMatches, buyTicket, loginUser, logoutUser } from './services/api';
import './App.css';

const App = () => {
    const [user, setUser] = useState(null);  // Stanje za korisnika
    const [matches, setMatches] = useState([]);  // Stanje za utakmice

    // Funkcija za dobavljanje utakmica sa backenda
    const fetchMatchesData = async () => {
        try {
            const data = await fetchMatches();
            setMatches(data);
        } catch (error) {
            console.error('Došlo je do greške pri dobavljanju utakmica:', error);
        }
    };

    // Pozovi funkciju za dobavljanje podataka prilikom učitavanja komponente
    useEffect(() => {
        fetchMatchesData();
    }, []);

    // Funkcija za logout
    const handleLogout = () => {
        logoutUser();
        setUser(null);  // Resetuj stanje korisnika
        console.log('Korisnik se odjavio');
    };

    // Funkcija za prikaz kupljenih karata
    const handleKupljeneKarte = () => {
        // Dodaj logiku za prikaz kupljenih karata
        console.log('Prikaz kupljenih karata');
    };

    // Funkcija za sortiranje
    const handleSort = (sortType) => {
        // Dodaj logiku za sortiranje
        console.log('Sortiraj po:', sortType);
    };

    // Funkcija za kupovinu karata
    const handleBuyTicket = async (id) => {
        try {
            await buyTicket(id);
            console.log('Kupovina karte za utakmicu sa ID:', id);
            // Osvježi podatke o utakmicama nakon kupovine
            fetchMatchesData();
        } catch (error) {
            console.error('Došlo je do greške pri kupovini karte:', error);
        }
    };

    // Funkcija za prijavu korisnika
    const handleLogin = async (username, password) => {
        try {
            const tokenData = await loginUser(username, password);
            localStorage.setItem('token', tokenData.access);  // Sačuvaj token
            setUser({ username });  // Postavi stanje korisnika
            console.log('Prijava uspešna!');
        } catch (error) {
            console.error('Došlo je do greške pri prijavi:', error);
        }
    };

    return (
        <div className="App">
            <h1>Kkartizan</h1>

            {/* Prikaz korisnika i dugmadi za logout i kupljene karte */}
            {user ? (
                <div className="korisnik">
                    <h2>Korisnik: {user.username}</h2>
                    <button className="menibtn" onClick={handleLogout}>
                        Logout
                    </button>
                    <button className="menibtn" onClick={handleKupljeneKarte}>
                        Kupljene karte
                    </button>
                </div>
            ) : (
                <div>
                    <h2>Prijavi se</h2>
                    <button onClick={() => handleLogin('korisnik123', 'lozinka123')}>
                        Prijavi se (mock)
                    </button>
                </div>
            )}

            {/* Dugmad za sortiranje */}
            <div className="sort-buttons">
                <button onClick={() => handleSort('protivnik')}>Sortiraj po protivniku</button>
                <button onClick={() => handleSort('datumVreme')}>Sortiraj po datumu</button>
                <button onClick={() => handleSort('lokacija')}>Sortiraj po lokaciji</button>
            </div>

            {/* Lista utakmica */}
            <ul>
                {matches.map((match) => (
                    <li key={match.id}>
                        <img src={match.urlSlike} alt="Utakmica" width="330" height="180" />
                        <div className="match-info">
                            <span>Partizan VS {match.protivnik}</span>
                            <span className="date">
                                {new Date(match.datumVreme).toLocaleString()}
                            </span>
                        </div>
                        <button onClick={() => handleBuyTicket(match.id)}>Kupi karte</button>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default App;