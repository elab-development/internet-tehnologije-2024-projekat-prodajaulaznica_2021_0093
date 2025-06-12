import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import MainPage from './pages/MainPage';
import Login from './components/Login';
import Register from './components/Register';
import KupljeneKarte from './components/KupljeneKarte';
import Navbar from './components/NavBar';
import { UserProvider } from './context/UserContext';
import './App.css';
import Kupovina from './components/Kupovina';
import UspesnaKupovina from './components/UspesnaKupovina';
import ErrorPage from './components/ErrorPage';




const App = () => {
  return (
    <UserProvider>
      <Router>
        <Navbar />
        <Routes>
          <Route path="/" element={<MainPage />} />
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
          <Route path="/kupljene-karte" element={<KupljeneKarte />} />
          <Route path="/kupovina/:matchId" element={<Kupovina />} />
          <Route path="/success" element={<UspesnaKupovina />} />
          <Route path="/greska" element={<ErrorPage />} />
        </Routes>
      </Router>
    </UserProvider>
  );
};

export default App;
