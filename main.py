from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import logging
from typing import Dict

# Initialize logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI()

# Global variable to hold the courses data
courses_df = None

# Load CSV file on startup
@app.on_event("startup")
async def load_courses():
    global courses_df
    try:
        file_path = "merged1_udemy_courses_cleaned.csv"  # Path to your uploaded file
        courses_df = pd.read_csv(file_path)

        # Fill missing course_content with empty strings
        if 'course_content' not in courses_df.columns or courses_df['course_content'].isnull().all():
            logger.warning("'course_content' column is missing or empty. Filling with empty strings.")
            courses_df['course_content'] = ""

        logger.info("Courses CSV loaded successfully.")
    except Exception as e:
        logger.error(f"Error loading courses CSV: {e}")
        raise RuntimeError("Failed to load courses data.")

# Define the request model
class UserProfile(BaseModel):
    profile_details: Dict[str, str]

@app.post("/recommend/")
async def recommend_courses(user_profile: UserProfile):
    global courses_df
    if courses_df is None:
        logger.error("Courses data is not loaded.")
        raise HTTPException(status_code=500, detail="Courses data is not available.")

    try:
        # Extract user profile details
        profile = user_profile.profile_details
        logger.info(f"Received user profile: {profile}")

        # Simple recommendation logic based on keyword matching in course titles and content
        keywords = " ".join(profile.values()).lower()
        logger.info(f"Generated keywords from profile: {keywords}")

        # Compute a simple match score
        courses_df['match_score'] = courses_df.apply(
            lambda row: sum([
                1 for word in keywords.split()
                if word in str(row['course_title']).lower() or word in str(row['course_content']).lower()
            ]),
            axis=1
        )

        # Sort courses by match_score and return the top 5
        top_courses = courses_df.sort_values(by="match_score", ascending=False).head(5)

        # Prepare response
        recommendations = top_courses[["course_title", "url", "price", "match_score"]].to_dict(orient="records")
        logger.info(f"Top 5 recommendations: {recommendations}")

        return {"recommendations": recommendations}

    except Exception as e:
        logger.error(f"Error in recommendation logic: {e}")
        raise HTTPException(status_code=500, detail="An error occurred while processing the request.")

# Health check endpoint
@app.get("/")
async def health_check():
    return {"status": "API is running successfully"}
