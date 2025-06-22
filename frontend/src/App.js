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
import ProtectedRoute from './components/ProtectedRoute';

const App = () => {
  return (
    <UserProvider>
      <Router>
        <Navbar />
        <Routes>
          <Route path="/" element={<MainPage />} />
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />

          <Route
            path="/kupljene-karte"
            element={
              <ProtectedRoute>
                <KupljeneKarte />
              </ProtectedRoute>
            }
          />

          <Route
            path="/kupovina/:matchId"
            element={
              <ProtectedRoute>
                <Kupovina />
              </ProtectedRoute>
            }
          />

          <Route path="/success" element={<UspesnaKupovina />} />
          <Route path="/error" element={<ErrorPage />} />
        </Routes>
      </Router>
    </UserProvider>
  );
};

export default App;