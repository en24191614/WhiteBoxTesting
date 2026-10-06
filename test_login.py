from login import validate_login

test_cases = [
    ("TC01", "", "1234", "Username required"),
    ("TC02", "admin", "", "Password required"),
    ("TC03", "admin", "1234", "Login successful"),
    ("TC04", "user", "5678", "Invalid login credentials"),
    ("TC05", "admin", "wrong", "Invalid login credentials")
]

for test_id, username, password, expected in test_cases:

    actual = validate_login(username, password)

    if actual == expected:
        status = "PASS"
    else:
        status = "FAIL"

    print(test_id)
    print("Expected:", expected)
    print("Actual:", actual)
    print("Status:", status)
    print("-------------------------")
