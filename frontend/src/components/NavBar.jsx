import React, { useContext } from 'react';
import { UserContext } from '../context/UserContext';
import { Link, useNavigate } from 'react-router-dom';
import './NavBar.css';

const NavBar = () => {
  const { user, logout } = useContext(UserContext);
  const navigate = useNavigate();

  const handleLogout = () => {
    logout();
    navigate('/');
  };

  return (
    <div className="navbar">
      <div className="navbar-left">
        <Link to="/" className="logo">KKartizan</Link>
      </div>
      <div className="navbar-right">
        {user ? (
          <>
            <span className="username"> {user.username}</span>
            <button onClick={() => navigate('/kupljene-karte')}>Kupljene karte</button>
            <button onClick={handleLogout} className="logout">Odjavi se</button>
          </>
        ) : (
          <>
            <button onClick={() => navigate('/login')}>Login</button>
            <button onClick={() => navigate('/register')}>Register</button>
          </>
        )}
      </div>
    </div>
  );
};

export default NavBar;
