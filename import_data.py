import pandas as pd
from app import create_app
from models import db, CVE

def import_data(csv_file):
    app = create_app()
    with app.app_context():
        db.create_all()
        data = pd.read_csv(csv_file)
        for _, row in data.iterrows():
            cve = CVE(
                cve_id=row['cve_id'],
                description=row['description'],
                published_date=row['published_date'],
                last_modified_date=row['last_modified_date']
            )
            db.session.add(cve)
        db.session.commit()

if __name__ == '__main__':
    import_data('cves.csv')
