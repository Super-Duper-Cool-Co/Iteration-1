# Super Duper Cool Canadian Animal Database

### A Super Duper Cool Company Project

---

## Overview

This project includes both a front end and a back end for a simple HTML-based web app that serves as a database for various species of fauna native to Canada.

---

## How to Access and Run the Website

Follow the steps below to access and run the Super Duper Cool Canadian Animal Database from this GitHub repository:

### 1. Clone the Repository

Start by cloning the GitHub repository to your local machine:

```bash
git clone https://github.com/YourUsername/CanadianAnimalDatabase.git
cd CanadianAnimalDatabase
```

### 2. Open the Homepage

You can directly launch the website by opening the `homepage.html` file in your web browser:

- Navigate to the project directory.
- Open `homepage.html` using your preferred browser (double-click or right-click → Open With...).

The homepage features:
- A top navigation bar
- A large map of Canada
- A link to the animal database (future versions will support clickable provinces)
- An “Add Animal” form (UI only; not yet functionally connected to the backend)

---

## Project Structure

| File              | Description |
|-------------------|-------------|
| `homepage.html`   | Main entry point for the website |
| `app.js`          | JavaScript logic for the frontend |
| `backend.py`      | Command-line interface for managing the database |
| `Animal.py`       | Defines the data structure for animal entries |
| `Dockerfile`      | (Optional) For containerizing the application |
| `README.md`       | Documentation and setup instructions |
| `SDCC_Database.csv` | (Expected) CSV file used by the backend to store data |

---

## Database Management

To modify the database (e.g., add, edit, or remove animals):

1. Run the backend interface:

```bash
python backend.py
```

2. Use the CLI menu to manage entries:
   - Add a new animal
   - Edit existing entries
   - Remove animals

3. Once you exit the CLI, the program will automatically update the `list.html` file to reflect the changes.

---

## To-Do

- [ ] Make the "Add Animal" form functional
- [ ] Add clickable provinces to the map on the homepage
- [ ] Improve HTML and CSS styling
- [ ] Implement dynamic content rendering in `list.html`

---
