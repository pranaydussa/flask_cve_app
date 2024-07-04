from flask import Blueprint, request, jsonify
from models import db, CVE

cve_bp = Blueprint('cve', __name__)

@cve_bp.route('/cves', methods=['GET'])
def get_cves():
    cves = CVE.query.all()
    return jsonify([cve.as_dict() for cve in cves])

@cve_bp.route('/cves/<int:id>', methods=['GET'])
def get_cve(id):
    cve = CVE.query.get_or_404(id)
    return jsonify(cve.as_dict())

@cve_bp.route('/cves', methods=['POST'])
def add_cve():
    data = request.get_json()
    cve = CVE(
        cve_id=data['cve_id'],
        description=data['description'],
        published_date=data['published_date'],
        last_modified_date=data['last_modified_date']
    )
    db.session.add(cve)
    db.session.commit()
    return jsonify(cve.as_dict()), 201

@cve_bp.route('/cves/<int:id>', methods=['PUT'])
def update_cve(id):
    data = request.get_json()
    cve = CVE.query.get_or_404(id)
    cve.cve_id = data['cve_id']
    cve.description = data['description']
    cve.published_date = data['published_date']
    cve.last_modified_date = data['last_modified_date']
    db.session.commit()
    return jsonify(cve.as_dict())

@cve_bp.route('/cves/<int:id>', methods=['DELETE'])
def delete_cve(id):
    cve = CVE.query.get_or_404(id)
    db.session.delete(cve)
    db.session.commit()
    return '', 204

def cve_as_dict(self):
    return {
        'id': self.id,
        'cve_id': self.cve_id,
        'description': self.description,
        'published_date': self.published_date,
        'last_modified_date': self.last_modified_date
    }

CVE.as_dict = cve_as_dict
