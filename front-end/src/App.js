import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [cities, setCities] = useState([]);
  const [selectedCity, setSelectedCity] = useState('');
  const [insertCity, setInsertCity] = useState('');
  const [startDate, setStartDate] = useState('');
  const [endDate, setEndDate] = useState('');

  useEffect(() => {
    getCities();
  }, []);

  const basicAuth = {
    username: 'pkleiz',
    password: '123'
  };

  const getCities = async () => {
    const response = await axios.get('http://127.0.0.1:2020/apis/cities/');
    setCities(response.data);
  };

  function handleInsertCityChange(event) {
    setInsertCity(event.target.value);
  }

  const handleCitySubmit = async () => {
    await axios.post('http://127.0.0.1:2020/apis/cities/', { name: insertCity }, { auth: basicAuth });
    getCities();
  };


  const handleStartDateChange = (event) => {
    setStartDate(event.target.value);
  };

  const handleEndDateChange = (event) => {
    setEndDate(event.target.value);
  };


  const handleSearch = async () => {
    if (selectedCity && startDate && endDate) {
      await axios.get(`http://127.0.0.1:2020/apis/nearest-earthquake/?city=${selectedCity}&start_date=${startDate}&end_date=${endDate}`);
    } else if (startDate && endDate) {
      await axios.get(`http://127.0.0.1:2020/apis/earthquakes/?start_date=${startDate}&end_date=${endDate}`);
    }
  };

  return (
    <div className="container">
      <div className="sidebar">
        <div className="city-input">
          City
          <input type="text" value={insertCity} onChange={handleInsertCityChange}/>
          <button onClick={handleCitySubmit}>Add</button>
        </div>
        <ul>
          {cities.map((city) => (
            <li key={city.id}>{city.name}</li>
          ))}
        </ul>
      </div>
      
      <div className="content">
        <div className="search-fields">
          <select value={selectedCity} onChange={(e) => setSelectedCity(e.target.value)}>
            <option value="">Select a city</option>
            {cities.map((city) => (
              <option key={city.id} value={city.name}>
                {city.name}
              </option>
            ))}
          </select>
      <label htmlFor="start-date">Data de início:</label>
      <input
        type="date"
        id="start-date"
        name="start-date"
        value={startDate}
        onChange={handleStartDateChange}
      />

      <label htmlFor="end-date">Data de fim:</label>
      <input
        type="date"
        id="end-date"
        name="end-date"
        value={endDate}
        onChange={handleEndDateChange}
      />

      <button onClick={handleSearch}>Pesquisar</button>
        </div>
        <div className="map"></div>
      </div>
    </div>
  );
}

export default App;
