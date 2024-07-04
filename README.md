# CVE Management Flask Application

This is a Flask application to manage data related to Common Vulnerabilities and Exposures (CVEs). The application provides RESTful APIs to perform various operations on CVE data. Data can be imported from a CSV file into an SQLite database.

## Setup Instructions

### Dependencies

- Python 3
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- pandas
- SQLite (default) or PostgreSQL (optional)

### Installation

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd cve_app
