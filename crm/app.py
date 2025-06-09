from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crm.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def to_dict(self):
        return {"id": self.id, "name": self.name, "email": self.email}

with app.app_context():
    db.create_all()

@app.route('/customers', methods=['GET'])
def get_customers():
    customers = Customer.query.all()
    return jsonify([c.to_dict() for c in customers])

@app.route('/customers', methods=['POST'])
def create_customer():
    data = request.get_json() or {}
    name = data.get('name')
    email = data.get('email')
    if not name or not email:
        return jsonify({'error': 'Name and email required'}), 400
    customer = Customer(name=name, email=email)
    db.session.add(customer)
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Email must be unique'}), 400
    return jsonify(customer.to_dict()), 201

@app.route('/customers/<int:customer_id>', methods=['PUT'])
def update_customer(customer_id):
    customer = Customer.query.get_or_404(customer_id)
    data = request.get_json() or {}
    name = data.get('name')
    email = data.get('email')
    if name:
        customer.name = name
    if email:
        customer.email = email
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Email must be unique'}), 400
    return jsonify(customer.to_dict())

@app.route('/customers/<int:customer_id>', methods=['DELETE'])
def delete_customer(customer_id):
    customer = Customer.query.get_or_404(customer_id)
    db.session.delete(customer)
    db.session.commit()
    return '', 204

@app.route('/login/admin')
def login_admin():
    return render_template('login.html', role='Admin')

@app.route('/login/personnel')
def login_personnel():
    return render_template('login.html', role='Personnel')

@app.route('/login/customer')
def login_customer():
    return render_template('login.html', role='Customer')

if __name__ == '__main__':
    app.run(debug=True)
