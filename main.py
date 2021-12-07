import json

from src.controller import ValidatorController

if __name__ == "__main__":
    users = [
        {"id": "1151959064", "name": "Jorge"},
        {"id": "21429829", "name": "Miguel"},
        {"id": "1438277384", "name": "Karen"},
        {"id": "14382774", "name": "Julia"},
    ]

    validator_controller = ValidatorController(users)
    print(json.dumps(validator_controller.validate_users(), indent=2))
