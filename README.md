#  Online Feedback Collector with Admin Dashboard
The Online Feedback Collector is a web-based application developed using Flask (Python) and SQLite that allows users to submit feedback and enables an admin to view, analyze, and export feedback data.

## This project demonstrates concepts of:

Web development using Flask

Database integration using SQLite

Admin authentication

Data visualization using Chart.js

CSV export functionality

MVC-like folder structure

## 🎯 Features
### 👤 User Features
Submit feedback with:

Name

Email

Rating (1–5)

Comments

Simple and responsive UI

Data stored securely in SQLite database

## 🔐 Admin Features

Admin login authentication

View all submitted feedback
### Dashboard with:

Total feedback count

Average rating

Rating distribution bar chart

Export feedback data as CSV

Secure logout functionality

##🛠️ Technologies Used

| Technology   | Purpose            |
| ------------ | ------------------ |
| Python       | Backend logic      |
| Flask        | Web framework      |
| SQLite       | Database           |
| HTML5        | Frontend structure |
| CSS3         | Styling            |
| Bootstrap 5  | Responsive UI      |
| Chart.js     | Data visualization |
| Git & GitHub | Version control    |

## 📁 Project Folder Structure

OnlineFeedbackCollector/
│

├── app.py

├── database.db

├── README.md

├── static/

│   └── css/

│       └── style.css


└── templates/
    
    ├── layout.html  

    ├── index.html
    
    ├── admin.html
    
    └── admin_login.html

## ⚙️ Installation & Setup Instructions
 ### Install Required Packages

Make sure Python is installed, then run:

  pip install flask

### Run the Application
   python app.py

### Open in Browser
    http://127.0.0.1:5000/
## 🔐 Admin Login Credentials

Default Admin Credentials

Username: admin

Password: admin123

## 📊 Admin Dashboard

### Displays:

Total number of feedbacks

Average rating

Rating distribution graph

Feedback displayed in tabular form

CSV export option available

## 📤 Export Feedback

Admin can export all feedback data

CSV file downloaded automatically

Useful for reports and analysis

## 🧪 Database Details

Database: SQLite

File: database.db

Table: feedback

## Feedback Table Schema
| Column         | Type                  |
| -------------- | --------------------- |
| id             | INTEGER (Primary Key) |
| name           | TEXT                  |
| email          | TEXT                  |
| rating         | INTEGER               |
| comments       | TEXT                  |
| date_submitted | TEXT                  |
