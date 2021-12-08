# Valid user that exists in our DB, this one could be a prospect
VALID_USER = {"id": "1151959064", "name": "Jorge"}

# Invalid user that doens't exists in our DB
INVALID_USER = {"id": "14382774", "name": "Julia"}

# Users that exists in our DB, Users doesn't exist, and not valid users
MIXED_USERS = [
    VALID_USER,
    {"id": "21429829", "name": "Miguel"},
    {"id": "1438277384", "name": "Karen"},
    INVALID_USER,
    {"ids": "14382774", "names": "Julia"},
]

# Users that exists in our DB and Users doesn't exist
VALIDATED_USERS = [
    VALID_USER,
    {"id": "21429829", "name": "Miguel"},
    {"id": "1438277384", "name": "Karen"},
    INVALID_USER,
]
