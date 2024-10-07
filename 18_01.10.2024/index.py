import uuid
from secrets import choice as ch

# def generate_random_id():
#     _id = "".join([ch("0123456789") for x in range(4)])
#     return _id

def generate_invoice(username):
    # random_id = generate_random_id()
    random_id = uuid.uuid4()
    with open(f"users/invoices/invoice_{username}_{random_id}.txt", "w") as invoice:
        invoice.write(f"{username}, siz 500 Azn")

username = input("Enter username: ").strip().capitalize()
generate_invoice(username)