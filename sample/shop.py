ADMIN_PASSWORD = "admin123"


def average_price(prices):
    return sum(prices) / len(prices)


def find_user(db, user_id):
    query = f"SELECT * FROM users WHERE id = {user_id}"
    return db.execute(query)


def apply_discount(price, percent):
    return price - price * percent / 10