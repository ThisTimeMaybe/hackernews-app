from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import httpx
from datetime import datetime

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this as needed to restrict origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

HACKERNEWS_API_URL = "https://hacker-news.firebaseio.com/v0/newstories.json?print=pretty"

async def fetch_top_stories():
    async with httpx.AsyncClient() as client:
        response = await client.get(HACKERNEWS_API_URL)
        response.raise_for_status()
        story_ids = response.json()[:10]  # Get top 10 story IDs
        return story_ids

async def fetch_story_details(story_id):
    async with httpx.AsyncClient() as client:
        url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json?print=pretty"
        response = await client.get(url)
        response.raise_for_status()
        return response.json()

@app.get("/top-stories")
async def get_top_stories():
    try:
        story_ids = await fetch_top_stories()
        stories = []
        for story_id in story_ids:
            story = await fetch_story_details(story_id)
            stories.append({
                "title": story.get("title"),
                "author": story.get("by"),
                "url": f"https://news.ycombinator.com/item?id={story_id}",
                "score": story.get("score"),
                "time": datetime.fromtimestamp(story.get("time")).strftime('%Y-%m-%d %H:%M:%S')
            })
        return stories
    except httpx.RequestError as e:
        raise HTTPException(status_code=500, detail=str(e))
