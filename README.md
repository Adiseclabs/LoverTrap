# LoveTrap - ❤️ Social Engineering Simulation & Behavioral Analysis Platform

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-Framework-000000?style=flat-square&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=flat-square&logo=sqlite&logoColor=white)](https://sqlite.org)
[![Render](https://img.shields.io/badge/Deployed%20on-Render-46E3B7?style=flat-square&logo=render&logoColor=white)](https://render.com)
[![Purpose](https://img.shields.io/badge/Purpose-Educational%20Only-FF6B6B?style=flat-square)](https://github.com)

> A cybersecurity research platform that simulates a fake dating website to study how users respond to social engineering attacks in a fully safe and controlled environment.

---

## Overview

**LoveTrap** mimics a realistic dating platform to expose users to simulated scam scenarios and observe their behavioral responses. Every scenario is purely visual — no malicious code runs, no real harm occurs. The project exists to educate, demonstrate, and raise awareness about how social engineering attacks operate in the wild.

**Live Demo →** [https://lovertrap.onrender.com](https://lovertrap.onrender.com/)

---

## How It Works

When a user clicks **"Get Contact"** on the fake dating interface, the system randomly triggers one of three simulated attack scenarios:

| Scenario | Description |
|---|---|
| ⚠️ Fake Warning Message | A simulated police fine or legal alert notification |
| 📲 Fake App Download | A prompt mimicking a suspicious app installation screen |
| 💻 System Command Trick | A social engineering prompt replicating Win+R / Win+C style attacks |

All scenarios are designed to replicate techniques used in real-world attacks — presented safely for analysis and learning.

---

## Data Collection

The system logs minimal, non-sensitive interaction data for research use only:

- Button click events
- IP address (for frequency and geographic tracking)
- Scenario type that was triggered

### Admin Dashboard

A built-in admin panel allows researchers to review:

- Full interaction logs
- IP activity summaries
- Total click and interaction statistics

---

## Objectives

- Analyze how users respond to deceptive online situations
- Demonstrate real-world social engineering attack vectors in a safe setting
- Raise awareness about online scams and psychological manipulation
- Contribute to cybersecurity education and behavioral research

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Flask |
| Database | SQLite |
| Frontend | HTML, CSS, JavaScript |
| Deployment | Render |

---

## Getting Started

**Prerequisites:** Python 3.x, pip

```bash
# Clone the repository
git clone https://github.com/your-username/lovetrap.git
cd lovetrap

# Install dependencies
pip install -r requirements.txt

# Start the server
python app.py
```

Visit `http://localhost:5000` in your browser.

---

## Project Structure

```
lovetrap/
├── app.py                  # Flask application and routing
├── templates/
│   ├── index.html          # Fake dating platform frontend
│   └── admin.html          # Admin analytics dashboard
├── static/
│   ├── css/
│   └── js/
├── database.db             # SQLite interaction logs
├── requirements.txt
└── README.md
```

---

## Ethical Usage

This project is open for educational and cybersecurity research use.

**Allowed:**
- Personal learning, academic research, and security demonstrations
- Modifying and extending for classroom or lab environments

**Not Allowed:**
- Deploying with intent to deceive real users without informed consent
- Any use that violates applicable laws or ethical guidelines

---

## Disclaimer

This project is built **strictly for cybersecurity research and educational purposes**.

- All scenarios are fully simulated — no real actions are executed
- No sensitive personal data is collected or stored
- Intent is awareness and analysis, not exploitation

The author bears no responsibility for misuse of this project.

---

## Author

**Aditya Bhosale**
Cybersecurity Analyst · Security Researcher

---

*If you found this project useful, consider giving it a ⭐ on GitHub — it helps the project reach more security learners.*
