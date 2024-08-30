
# Serverless Photo Gallery Application

![Photo Gallery Banner](https://user-images.githubusercontent.com/yourprofile/photo-gallery-banner.png)

## 🌟 Overview

The Serverless Photo Gallery Application is a cloud-based solution designed to manage photos seamlessly with capabilities such as uploading, viewing, and searching for photos. The application is built with Python, leveraging AWS services including Lambda, DynamoDB, S3, and Cognito for a scalable, secure, and highly available infrastructure. The solution integrates with a React frontend, providing an intuitive user experience for managing photo collections.

## 📋 Table of Contents

- [Introduction](#introduction)
- [Technologies Used](#technologies-used)
- [Architecture](#architecture)
- [Project Structure](#project-structure)
- [Setup and Installation](#setup-and-installation)
- [Key Features](#key-features)
  - [User Management](#user-management)
  - [Photo Management](#photo-management)
  - [Search and Update Photos](#search-and-update-photos)
- [Screenshots](#screenshots)
- [Contributors](#contributors)
- [License](#license)

## 🚀 Introduction

This project is focusing on creating serverless applications using AWS services. The application allows users to manage their photo collections, providing features such as user authentication, photo upload, search, and metadata management. The backend is entirely serverless, ensuring scalability and ease of maintenance.

## 🛠️ Technologies Used

- **Python**: Core programming language for Lambda functions.
- **AWS Lambda**: Serverless compute service to run backend logic.
- **DynamoDB**: NoSQL database service for storing photo metadata.
- **Amazon S3**: Scalable storage service for photo files.
- **Amazon Cognito**: Service for user authentication and authorization.
- **API Gateway**: Manages API requests and routes them to Lambda functions.
- **Boto3**: AWS SDK for Python to interact with AWS services.
- **Bootstrap & jQuery**: Frontend technologies for responsive design and dynamic content.

## 🏗️ Architecture

The Serverless Photo Gallery Application architecture is built using a combination of AWS services to provide a fully managed, highly available, and scalable solution:

1. **Frontend**: Static website hosted on Amazon S3, using HTML, CSS, and JS for the user interface.
2. **Backend**: AWS Lambda functions handle CRUD operations, search, and user management.
3. **Storage**: Photos are stored in S3, with metadata stored in DynamoDB.
4. **Authentication**: AWS Cognito manages user pools, handling signup, login, and email verification.
5. **API Gateway**: Serves as the entry point for all API requests, routing them to the appropriate Lambda functions.

![Architecture Diagram](https://user-images.githubusercontent.com/yourprofile/architecture-diagram.png)

## 🗂️ Project Structure

```plaintext
├── app.py                     # Main Flask application for local testing
├── lambda_functions/          # Lambda functions for backend operations
│   ├── addphoto.py            # Add a new photo to the gallery
│   ├── delete.py              # Delete a photo from the gallery
│   ├── getphoto.py            # Retrieve a specific photo's details
│   ├── getphotos.py           # Retrieve all photos in the gallery
│   ├── login.py               # Handle user login via Cognito
│   ├── signup.py              # Handle user signup via Cognito
│   ├── confirmemail.py        # Confirm user email via Cognito
│   ├── search.py              # Search photos by title, description, or tags
│   ├── update.py              # Update photo details
├── frontend/                  # HTML templates and static files
│   ├── index.html             # Homepage displaying albums
│   ├── login.html             # Login page for users
│   ├── signup.html            # Signup page for new users
│   ├── addphoto.html          # Form for adding photos
│   ├── search.html            # Search results page
│   ├── viewphoto.html         # Detailed view of a single photo
├── cloudformation/            # CloudFormation templates for infrastructure setup
└── README.md                  # Project documentation
🛠️ Setup and Installation
Prerequisites
AWS Account: Required for deploying serverless resources.
AWS CLI: For managing AWS services from the command line.
Python 3.x: Required for running Lambda functions and local tests.
Node.js: Required for building and deploying the frontend.
Installation Steps
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/photo-gallery.git
cd photo-gallery
Set up environment variables:

Update env.py with your AWS credentials and service configurations.
Deploy AWS Resources:

Use the CloudFormation template to deploy all AWS resources.
bash
Copy code
aws cloudformation deploy --template-file cloudformation/template.yaml --stack-name PhotoGalleryStack --capabilities CAPABILITY_NAMED_IAM
Deploy Lambda Functions:

Deploy the Lambda functions via AWS CLI.
bash
Copy code
./deploy_lambda.sh
Deploy Frontend:

Navigate to the frontend/ directory and deploy the static site.
bash
Copy code
npm install
npm run build
aws s3 sync build/ s3://your-s3-bucket/
Access the Application:

Once deployed, access the application via the API Gateway URL or CloudFront distribution.
✨ Key Features
🔐 User Management
Signup: Users can create an account with a username, email, and password.

Lambda Function: signup.py
Cognito: Handles user pools, signup, and email verification.
Login: Authenticate users using Cognito.

Lambda Function: login.py
Email Confirmation: Users confirm their email after signup.

Lambda Function: confirmemail.py
Password Reset: Users can reset their password through an email confirmation code.

HTML Template: forgotpassword.html
Lambda Integration: Cognito handles password reset.
📸 Photo Management
Add Photo: Users can upload photos, which are stored in S3, and metadata is stored in DynamoDB.

Lambda Function: addphoto.py
S3 Storage: Stores the photo file.
DynamoDB: Stores metadata like title, description, tags, and URL.
View Photo Details: Retrieve and display specific photo metadata.

Lambda Function: getphoto.py
HTML Template: viewphoto.html
View All Photos: Display all photos in the user's gallery.

Lambda Function: getphotos.py
🔍 Search and Update Photos
Search Photos: Users can search for photos by title, description, or tags.

Lambda Function: search.py
DynamoDB: Uses filter expressions to query the database.
Update Photo Details: Edit the metadata of an existing photo.

Lambda Function: update.py
DynamoDB: Update title, description, tags.
Delete Photo: Remove a photo and its metadata from the gallery.

Lambda Function: delete.py
📸 Screenshots
The homepage of the Photo Gallery application.

Uploading a new photo to the gallery.

Searching for photos by title, description, or tags.

👥 Contributors
[Your Name] - Cloud Developer & Solution Architect
Proficient in developing serverless applications on AWS, including hands-on experience with Lambda, DynamoDB, S3, and Cognito.
Developed this project as part of coursework at Georgia Tech, showcasing skills in cloud architecture and serverless computing.
