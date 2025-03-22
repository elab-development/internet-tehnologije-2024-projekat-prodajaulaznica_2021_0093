import React from 'react';
import './NavBar.css';

const Navbar = ({ user, onLogout, onShowTickets }) => {
  return (
    <nav className="navbar">
      <div className="user-info">{user}</div>
      <div className="nav-buttons">
        <button onClick={onShowTickets}>Kupljene karte</button>
        <button onClick={onLogout}>Odjavi se</button>
      </div>
    </nav>
  );
};

export default Navbar;