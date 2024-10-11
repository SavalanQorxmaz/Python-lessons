import time

def authenticate(func):
    def wrapper():
        if user_logged_in:
            func()
        else:
            login()
            time.sleep(2)
            func()
    return wrapper

def login():
    global user_logged_in
    print("Status: User is not logged in:")
    print("Loging in...")
    user_logged_in = True

@authenticate
def elan_yarat():
    print("Creating elan...")

@authenticate
def elan_sil():
    print("Deleting elan...")

user_logged_in = False
print(f"{user_logged_in=}")
elan_yarat()
print(f"{user_logged_in=}")
elan_sil()
print(f"{user_logged_in=}")