// src/TopStories.js

import React, { useEffect, useState } from 'react';
import axios from 'axios';

const TopStories = () => {
  const [stories, setStories] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchStories = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:8000/top-stories');
        setStories(response.data);
      } catch (error) {
        console.error('Error fetching stories:', error);
        setError('Error fetching stories.');
      }
    };

    fetchStories();
  }, []);

  return (
    <div>
      <h1>Top 10 HackerNews Stories</h1>
      {error && <p>{error}</p>}
      <ul>
        {stories.length === 0 ? (
          <p>Loading stories...</p>
        ) : (
          stories.map((story, index) => (
            <li key={index}>
              <a href={story.url} target="_blank" rel="noopener noreferrer">{story.title}</a>
              <p>Author: {story.author}</p>
              <p>Score: {story.score}</p>
              <p>Time: {story.time}</p>
            </li>
          ))
        )}
      </ul>
    </div>
  );
};

export default TopStories;
