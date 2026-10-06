def validate_login(username, password):

    if username == "":
        return "Username required"

    if password == "":
        return "Password required"

    if username == "admin" and password == "1234":
        return "Login successful"

    return "Invalid login credentials"
