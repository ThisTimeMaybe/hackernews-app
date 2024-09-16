// src/App.js
import React from 'react';
import TopStories from './TopStories';
import './App.css'; // Keep this if you want to maintain the existing styles

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Top 10 HackerNews Stories</h1>
      </header>
      <TopStories />
    </div>
  );
}

export default App;
