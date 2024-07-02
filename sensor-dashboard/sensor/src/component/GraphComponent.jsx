import React, { useEffect, useState } from 'react';
import { Line } from 'react-chartjs-2';
import axios from 'axios';
import 'chart.js/auto';
import './GraphComponent.css'; // Import CSS file for additional styling

const GraphComponent = () => {
  const [temperatureData, setTemperatureData] = useState({
    labels: [],
    datasets: [
      {
        label: 'Temperature (°C)',
        data: [],
        borderColor: 'rgba(255, 99, 132, 1)',
        borderWidth: 2,
        fill: false,
      },
    ],
  });

  const [humidityData, setHumidityData] = useState({
    labels: [],
    datasets: [
      {
        label: 'Humidity (%)',
        data: [],
        borderColor: 'rgba(54, 162, 235, 1)',
        borderWidth: 2,
        fill: false,
      },
    ],
  });

  const [combinedData, setCombinedData] = useState({
    labels: [],
    datasets: [
      {
        label: 'Temperature (°C)',
        data: [],
        borderColor: 'rgba(255, 99, 132, 1)',
        borderWidth: 2,
        fill: false,
      },
      {
        label: 'Humidity (%)',
        data: [],
        borderColor: 'rgba(54, 162, 235, 1)',
        borderWidth: 2,
        fill: false,
      },
    ],
  });

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('http://0.0.0.0:8088/sensor-data/data/');
        const responseData = response.data;

        const newLabels = responseData.map(item => new Date(item.timestamp).toLocaleTimeString());
        const newTemperatureData = responseData.map(item => item.temperature);
        const newHumidityData = responseData.map(item => item.humidity);

        setTemperatureData({
          labels: newLabels.slice(-20), 
          datasets: [
            { ...temperatureData.datasets[0], data: newTemperatureData.slice(-20) },
          ],
        });

        setHumidityData({
          labels: newLabels.slice(-20), 
          datasets: [
            { ...humidityData.datasets[0], data: newHumidityData.slice(-20) },
          ],
        });

        setCombinedData({
          labels: newLabels.slice(-20), 
          datasets: [
            { ...combinedData.datasets[0], data: newTemperatureData.slice(-20) },
            { ...combinedData.datasets[1], data: newHumidityData.slice(-20) },
          ],
        });
      } catch (error) {
        console.error('Error fetching data', error);
      }
    };

    const intervalId = setInterval(fetchData, 1000); // Fetch data every 5 seconds

    return () => clearInterval(intervalId);
  }, [temperatureData.datasets, humidityData.datasets, combinedData.datasets]);

  return (
    <div className="graph-container">
      <h2>Temperature and Humidity Data</h2>
      <div className="chart-container">
        <div className="chart">
          <h3>Temperature (°C)</h3>
          <Line data={temperatureData} options={{ responsive: true, maintainAspectRatio: false }} />
        </div>
        <div className="chart">
          <h3>Humidity (%)</h3>
          <Line data={humidityData} options={{ responsive: true, maintainAspectRatio: false }} />
        </div>
      </div>
    </div>
  );
};

export default GraphComponent;
