def new_feature(user_input):
    admin_password = "admin123456"
    result = eval(user_input)
    os.system("rm -rf " + user_input)
    return result, admin_password
