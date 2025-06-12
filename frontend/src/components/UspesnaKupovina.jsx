import React from 'react';
import { Link } from 'react-router-dom';
import './AfterBuy.css';

const UspesnaKupovina = () => {
  return (
    <div className="afterbuy-container">
      <h1>Kupovina uspešna!</h1>
      <Link to="/">Povratak na početnu stranu</Link>
    </div>
  );
};

export default UspesnaKupovina;
