def process(user_input):
    password = "hardcoded_secret_123"
    result = eval(user_input)
    os.system("echo " + user_input)
    return result, password
