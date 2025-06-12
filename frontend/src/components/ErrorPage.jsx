import React from 'react';
import { Link } from 'react-router-dom';
import './AfterBuy.css';

const ErrorPage = () => {
  return (
    <div className="afterbuy-container">
      <h1>Greška pri kupovini!</h1>
      <h2>Nema dovoljno karata na raspolaganju.</h2>
      <Link to="/">Povratak na početnu stranu</Link>
    </div>
  );
};

export default ErrorPage;
