import React from 'react';
import './SortButtons.css';

const SortButtons = ({ onSort }) => {
  return (
    <div className="sort-buttons">
      <button onClick={() => onSort('protivnik')}>Sortiraj po protivniku</button>
      <button onClick={() => onSort('datumVreme')}>Sortiraj po datumu</button>
      <button onClick={() => onSort('lokacija')}>Sortiraj po lokaciji</button>
    </div>
  );
};

export default SortButtons;
