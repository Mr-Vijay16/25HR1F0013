## Notification App Backend
# Campus Notifications Microservice

## Tech Stack
- Python
- Django
- Django REST Framework
- SQLite

---

## Features
- Create Notifications
- Update Notifications
- Delete Notifications
- List Notifications
- Filter Notifications
- Search Notifications
- Pagination
- Notification Sending Service

---

## Installation

```bash
git clone <repository-url>
cd notification-app-be
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

---

# 3. Create `Notification_System_Design.md`

```md
# Notification System Design

## Objective

Develop a backend service to manage campus notifications.

Supported notifications:

- Event
- Result
- Placement
- Academic

---

## Architecture

Client
↓
REST API
↓
Notification Service
↓
Database

---

## Database Design

Notification

- id
- type
- message
- timestamp
- status

Indexes:

- type
- timestamp

---

## APIs

GET /evaluation-service/health/

GET /evaluation-service/notifications/

POST /evaluation-service/notifications/

GET /evaluation-service/notifications/{id}/

PUT /evaluation-service/notifications/{id}/

DELETE /evaluation-service/notifications/{id}/

POST /evaluation-service/notifications/{id}/send/

---

## Performance Optimizations

- Database indexing
- Pagination
- Filtering
- Ordered queryset

---

## Notification Sending Flow

Client
↓
Send API
↓
Service Layer
↓
Update Status
↓
Logging Service

4. Final Folder Structure

notification-app-be/
│
├── manage.py
├── requirements.txt
├── README.md
├── Notification_System_Design.md
├── .gitignore
│
├── notification_app_be/
│
└── notifications/
    ├── migrations/
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── serializers.py
    ├── services.py
    ├── urls.py
    ├── views.py
    └── tests.py


5. Final Testing Checklist

Test all APIs:

GET    /evaluation-service/health/
GET    /evaluation-service/notifications/
POST   /evaluation-service/notifications/
GET    /evaluation-service/notifications/<id>/
PUT    /evaluation-service/notifications/<id>/
DELETE /evaluation-service/notifications/<id>/
POST   /evaluation-service/notifications/<id>/send/

Test:

Filtering
Search
Ordering
Pagination