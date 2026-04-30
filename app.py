from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage
employees = []

# Home route
@app.route('/')
def home():
    return "Employee API Running"

# GET all employees
@app.route('/employees', methods=['GET'])
def get_employees():
    return jsonify(employees)

# POST - Add new employee
@app.route('/employees', methods=['POST'])
def add_employee():
    data = request.get_json()

    if not data or not data.get('name') or not data.get('role'):
        return jsonify({"error": "Name and role are required"}), 400

    employee = {
        "name": data['name'],
        "role": data['role'],
        "salary": data.get('salary', 0)
    }

    employees.append(employee)
    return jsonify({"message": "Employee added", "employee": employee}), 201

# PUT - Update employee
@app.route('/employees/<int:index>', methods=['PUT'])
def update_employee(index):
    if index >= len(employees):
        return jsonify({"error": "Employee not found"}), 404

    data = request.get_json()
    employees[index].update(data)

    return jsonify({"message": "Employee updated", "employee": employees[index]})

# DELETE - Remove employee
@app.route('/employees/<int:index>', methods=['DELETE'])
def delete_employee(index):
    if index >= len(employees):
        return jsonify({"error": "Employee not found"}), 404

    removed = employees.pop(index)
    return jsonify({"message": "Employee deleted", "employee": removed})

# Run the app
if __name__ == '__main__':
    app.run(debug=True)