# CycleWorks

**Tagline**: Your go-to marketplace for buying and selling bicycles.

CycleWorks is a web application designed to connect bike enthusiasts by allowing users to browse, add, and explore bicycle listings with auto-calculated scores based on price and condition. This Minimum Viable Product (MVP) was built entirely solo by Prince Peter Ojezua (GitHub: PBrown0007) as part of my ALX portfolio project. As a beginner software engineering student with no prior experience, I created this from scratch between February and March 2025, hitting an 8/10 progress milestone by Week 2.

---

## Table of Contents
1. [Features](#features)
2. [Team](#team)
3. [Tech Stack](#tech-stack)
4. [Prerequisites](#prerequisites)
5. [Setup Instructions](#setup-instructions)
6. [Usage](#usage)
7. [Project Journey](#project-journey)
8. [Development Process](#development-process)
9. [Directory Structure](#directory-structure)
10. [Screenshots](#screenshots)
11. [Challenges](#challenges)
12. [Current Status](#current-status)
13. [Future Enhancements](#future-enhancements)
14. [Troubleshooting](#troubleshooting)
15. [How to Contribute](#how-to-contribute)
16. [Notes](#notes)
17. [License](#license)
18. [Acknowledgments](#acknowledgments)

---

## Features
CycleWorks delivers a functional MVP with these core capabilities:
- **Browse Listings**: View a table of bikes with name, price, condition, and score.
- **Detailed View**: Click a bike to see its full details on a dedicated page.
- **Add Listings**: Submit a form to add new bikes to the database.
- **Score Calculation**: Automatically assigns scores:
  - 90: New bikes under $100.
  - 70: Bikes under $200.
  - 50: All others.

These align with the user stories defined in Part 2, ensuring a complete end-to-end user experience.

---

## Team
- **Prince Peter Ojezua**: Full-stack developer (solo)
  - **Roles**: Designed and implemented the frontend (HTML, JavaScript), backend (Python, Flask), and database (MongoDB).
  - **Context**: Assigned teammates PrinceBrown Ojezua and [Third Member] did not contribute, leaving me to build this entirely on my own as a first-time coder.

---

## Tech Stack
- **Backend**:
  - Python 3.12: Core programming language.
  - Flask: Lightweight web framework for APIs.
  - PyMongo: Python library to interact with MongoDB.
  - MongoDB: NoSQL database for storing bike data.
- **Frontend**:
  - HTML: Structures the webpages.
  - JavaScript: Handles dynamic fetching and form submission.
- **Tools**:
  - Git & GitHub: Version control and hosting (repo: PBrown0007/CycleWorks).
  - Trello: Task management with 9 engineering and 5 mandatory tasks.
  - Visual Studio Code: Code editor.

---

## Prerequisites
To run CycleWorks locally, install these tools:
- **Python 3.12**: [Download](https://www.python.org/downloads/)
- **MongoDB Community Server**: [Download](https://www.mongodb.com/try/download/community)
- **Git**: [Download](https://git-scm.com)
- **Visual Studio Code**: [Download](https://code.visualstudio.com) (optional, but my choice for development)
- **Operating System**: Tested on Windows/Mac—should work on Linux too.

---

## Setup Instructions
Follow these detailed steps to get CycleWorks running on your machine:

1. **Clone the Repository**:
   - Open a terminal (Command Prompt on Windows, Terminal on Mac).
   - Run:
     ```bash
     git clone https://github.com/PBrown0007/CycleWorks.git
     cd CycleWorks
