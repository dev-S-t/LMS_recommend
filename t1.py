import requests

# Define the base URL of the API
BASE_URL = "http://127.0.0.1:8000"

# Test the health check endpoint
def test_health_check():
    try:
        response = requests.get(f"{BASE_URL}/")
        if response.status_code == 200:
            print("Health Check Passed:", response.json())
        else:
            print("Health Check Failed:", response.status_code, response.text)
    except Exception as e:
        print("Error testing health check:", e)

# Test the recommend endpoint
def test_recommend():
    try:
        # Define a sample user profile payload
        payload = {
            "profile_details": {
                "interest": "data science",
                "goal": "become a data scientist",
                "experience": "beginner",
                "skills": "python, machine learning"
            }
        }
        
        # Make a POST request to the recommend endpoint
        response = requests.post(f"{BASE_URL}/recommend/", json=payload)
        
        if response.status_code == 200:
            print("Recommendation Test Passed:")
            print(response.json())
        else:
            print("Recommendation Test Failed:", response.status_code, response.text)
    except Exception as e:
        print("Error testing recommend endpoint:", e)

if __name__ == "__main__":
    print("Running API Tests...\n")
    test_health_check()
    print("\n")
    test_recommend()
