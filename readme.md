# Homework Assignment App - API Documentation

## Overview

This app allows **students** to post their homework assignments, while **solvers** can browse, request to complete, and track the status of assignments. The following API endpoints allow students and solvers to interact with the app.

---

## API Endpoints

### 1. **POST /students/addhomework/**

**Description**: Allows students to post a new homework assignment.

#### Sample Request:
```bash
POST /students/addhomework/
Content-Type: application/json

{
  "title": "Math Assignment",
  "description": "Solve the integration problems",
  "subject": "Mathematics",
  "budget": 500,
  "latitude": 28.7041,
  "longitude": 77.1025,
  "contact_info": "9876543210",
  "nickname": "Ravi"
}
```

#### Sample Response:
```json
{
  "id": 1,
  "title": "Math Assignment",
  "description": "Solve the integration problems",
  "subject": "Mathematics",
  "budget": 500,
  "latitude": 28.7041,
  "longitude": 77.1025,
  "contact_info": "9876543210",
  "nickname": "Ravi"
}
```

---

### 2. **GET /students/gethomework/{nickname}**

**Description**: Fetch all homework assignments posted by a student using their nickname.

#### Sample Request:
```bash
GET /students/gethomework/Ravi
```

#### Sample Response:
```json
[
  {
    "id": 1,
    "title": "Math Assignment",
    "description": "Solve the integration problems",
    "subject": "Mathematics",
    "budget": 500,
    "latitude": 28.7041,
    "longitude": 77.1025,
    "contact_info": "9876543210",
    "nickname": "Ravi"
  }
]
```

---

### 3. **DELETE /students/deletehomework/{homework_id}**

**Description**: Delete a specific homework post by its ID.

#### Sample Request:
```bash
DELETE /students/deletehomework/1
```

#### Sample Response:
```json
{
  "id": 1,
  "title": "Math Assignment",
  "description": "Solve the integration problems",
  "subject": "Mathematics",
  "budget": 500,
  "latitude": 28.7041,
  "longitude": 77.1025,
  "contact_info": "9876543210",
  "nickname": "Ravi"
}
```

---

### 4. **GET /solvers/browsehomework/nearby**

**Description**: Solvers can browse homework assignments near their location.

#### Sample Request:
```bash
GET /solvers/browsehomework/nearby?latitude=28.7041&longitude=77.1025&radius_km=5
```

#### Sample Response:
```json
[
  {
    "id": 1,
    "title": "Math Assignment",
    "description": "Solve the integration problems",
    "subject": "Mathematics",
    "budget": 500,
    "latitude": 28.7041,
    "longitude": 77.1025,
    "contact_info": "9876543210",
    "nickname": "Ravi"
  }
]
```

---

### 5. **POST /solvers/sendrequest/sendrequest**

**Description**: Solvers can send a request to complete a specific homework assignment.

#### Sample Request:
```bash
POST /solvers/sendrequest/sendrequest
Content-Type: application/json

{
  "homework_id": 1,
  "solver_nickname": "Amit",
  "message": "I can help you with integration problems.",
  "contact_info": "amit@example.com"
}
```

#### Sample Response:
```json
{
  "id": 1,
  "homework_id": 1,
  "solver_nickname": "Amit",
  "message": "I can help you with integration problems.",
  "contact_info": "amit@example.com",
  "status": "pending"
}
```

---

### 6. **GET /solvers/getrequests/myrequests/{solver_nickname}**

**Description**: Solvers can view all requests they have sent for homework assignments.

#### Sample Request:
```bash
GET /solvers/getrequests/myrequests/Amit
```

#### Sample Response:
```json
[
  {
    "id": 1,
    "homework_id": 1,
    "solver_nickname": "Amit",
    "message": "I can help you with integration problems.",
    "contact_info": "amit@example.com",
    "status": "pending"
  }
]
```

---

## Running the Application

To run the application:

1. Install the required dependencies:
   ```bash
   pip install fastapi uvicorn sqlalchemy psycopg2
   ```

2. Update `database.py` with your PostgreSQL connection details.

3. Run the application:
   ```bash
   uvicorn main:app --reload
   ```

4. Access the interactive documentation at: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

### License

This project is licensed under the MIT License - see the LICENSE file for details.