# Mock dataset for implement-specific data
dummy_data = {
    "101": {"running": 5, "stop": 2, "idle": 3, "total_machines": 10, "cultivated_area": 15000, "total_area" : 18000},
    "102": {"running": 3, "stop": 4, "idle": 1, "total_machines": 8, "cultivated_area": 13000, "total_area" : 15000},
    "103": {"running": 6, "stop": 1, "idle": 2, "total_machines": 9, "cultivated_area": 14000, "total_area" : 20000}
}
def get_counts(user):
    # Default empty counts
    counts = {}
    
    # Only process if user is authenticated and has a role
    if hasattr(user, 'role'):
        if user.role == 'admin':
            counts = {
                'machines': 200,
                'implements': 10,
                'clusters': 10,
                'plots': 100
            }
        elif user.role == 'implement':
            counts = {
                'machines': len(user.vehicles),
                'implements': 0,
                'clusters': 0,
                'plots': 0
            }
    
    return counts

def get_machine_states(user):
    if user.role == 'admin':
        return {
            'running': 50,
            'stop': 25,
            'idle': 65
        }
    elif user.role == 'implement':
        return {
            'running': len(user.vehicles),
            'stop': 1,
            'idle': 1
        }