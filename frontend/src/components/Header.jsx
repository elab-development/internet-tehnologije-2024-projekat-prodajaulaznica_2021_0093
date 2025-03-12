// Header.js
import React from "react";
import "./Header.css";

const Header = () => {
  return (
    <header className="header">
      <h1>KKartizan</h1>
      <div className="sort-buttons">
        <a href="?sort=protivnik" className="sort-link">Sortiraj po protivniku</a> |
        <a href="?sort=datumVreme" className="sort-link">Sortiraj po datumu</a> |
        <a href="?sort=lokacija" className="sort-link">Sortiraj po lokaciji</a>
      </div>
    </header>
  );
};

export default Header;
