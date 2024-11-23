# **API Documentation: Course Recommendation System**

## **Base URL**  
*(This API is hosted on rander so except latency and cold reboots)*  
`https://lms-recommend.onrender.com`  

---

## **Endpoints**

### **1. GET /**
Health check endpoint to verify the API is running successfully.

---

### **2. POST /recommend/**
Provides personalized course recommendations based on user profile details.

---

## **Request Details**

### **Headers**
| Key            | Value                |
|----------------|----------------------|
| `Content-Type` | `application/json`   |

### **Body (JSON)**
| Parameter       | Type   | Description                                                                  |
|-----------------|--------|------------------------------------------------------------------------------|
| `profile_details` | Object | Flexible schema containing user details, such as interests, skills, goals, and experience. |

#### **Example Payload**
```json
{
  "profile_details": {
    "interest": "data science",
    "goal": "become a data scientist",
    "experience": "beginner",
    "skills": "python, machine learning"
  }
}
```

---

## **Response Details**

### **Success (200 OK)**  
Returns a list of recommended courses based on the user's profile.

#### **Response Body (JSON)**
| Key               | Type    | Description                                                               |
|-------------------|---------|---------------------------------------------------------------------------|
| `recommendations` | Array   | List of top 5 courses, including title, URL, price, and match score.      |

#### **Example Response**
```json
{
  "recommendations": [
    {
      "course_title": "Data Science for Beginners",
      "url": "https://example.com/course1",
      "price": "Free",
      "match_score": 5
    },
    {
      "course_title": "Python for Data Science",
      "url": "https://example.com/course2",
      "price": "$19.99",
      "match_score": 4
    }
  ]
}
```

---

### **Error (500 Internal Server Error)**  
Returned when an error occurs while processing the request.

#### **Example Error Response**
```json
{
  "detail": "An error occurred while processing your request."
}
```

---

## **Usage Examples**

### **Using cURL**
```bash
curl -X POST "http://<your-api-url>/recommend/" \
-H "Content-Type: application/json" \
-d '{
  "profile_details": {
    "interest": "data science",
    "goal": "become a data scientist",
    "experience": "beginner",
    "skills": "python, machine learning"
  }
}'
```

---

### **Using Python Requests**
```python
import requests

url = "http://<your-api-url>/recommend/"
payload = {
    "profile_details": {
        "interest": "data science",
        "goal": "become a data scientist",
        "experience": "beginner",
        "skills": "python, machine learning"
    }
}
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)
print(response.json())
```

---

### **Using JavaScript Fetch**
```javascript
fetch("http://<your-api-url>/recommend/", {
  method: "POST",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    profile_details: {
      interest: "data science",
      goal: "become a data scientist",
      experience: "beginner",
      skills: "python, machine learning"
    }
  })
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error("Error:", error));
```

---

## **Notes for Developers**
- **Flexible Input:** The `profile_details` field is highly adaptable; users can provide any combination of attributes.
- **Recommendation Logic:** Basic keyword matching is used for recommendations because of lack of time , logic will be improved in further versions
- **Error Handling:** Always check for the HTTP status code and the `detail` field in the response to handle failures effectively.
- **Scalability:** Ensure the API can handle concurrent requests. Optimize the CSV loading process for large datasets. 

---

Feel free to reach out for queries
