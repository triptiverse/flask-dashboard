from flask import Blueprint, render_template, request, jsonify

bp = Blueprint('main', __name__)

# Mock dataset for implement-specific data
dummy_data = {
    "101": {"running": 5, "stop": 2, "idle": 3, "total_machines": 10, "cultivated_area": 15000, "total_area" : 18000},
    "102": {"running": 3, "stop": 4, "idle": 1, "total_machines": 8, "cultivated_area": 13000, "total_area" : 15000},
    "103": {"running": 6, "stop": 1, "idle": 2, "total_machines": 9, "cultivated_area": 14000, "total_area" : 20000}
}

@bp.route('/')
def dashboard():
    # Default mock data
    N_machines = 19
    N_implement = 10
    N_cluster = 7
    N_plot = 50

    counts = {
        'machines': N_machines,
        'implements': N_implement,
        'clusters': N_cluster,
        'plots': N_plot
    }

    machine_states = {
        'running': 10,
        'stop': 4,
        'idle': 5
    }

    total_area = sum([data["total_area"] for data in dummy_data.values()])
    total_cultivated = sum([data["cultivated_area"] for data in dummy_data.values()])

    return render_template('dashboard.html', 
                           counts=counts,
                           machine_states=machine_states,
                           total_area=total_area,
                           total_cultivated=total_cultivated)

# New Route for Implement-Specific Data
@bp.route('/get_chart_data', methods=['POST'])
def get_chart_data():
    implement_id = request.json.get("implement_id")

    # Get data based on implement_id or provide default
    data = dummy_data.get(implement_id, {"running": 0, "stop": 0, "idle": 0, "total_machines": 0, "cultivated_area": 0})

    return jsonify({
        "machine_states": {
            "running": data["running"],
            "stop": data["stop"],
            "idle": data["idle"],
        },
        "total_machines": data["total_machines"],
        "cultivated_area": data["cultivated_area"],
        "total_area": data["total_area"]
    })
