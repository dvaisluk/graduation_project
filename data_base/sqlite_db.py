from create_bot import bot
import sqlite3


def sql_start():
    global conn, cur
    conn = sqlite3.connect('users.db')
    cur = conn.cursor()
    if conn:
        print('Data base connected OK!')

    cur.execute("""CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, telegram_id INTEGER, username TEXT, RUB_balance INTEGER, referrer_id INTEGER)""")

    conn.commit()


def registration_check(telegram_id):
    return cur.execute("SELECT telegram_id FROM users WHERE telegram_id = ?", (telegram_id,)).fetchone()


def register_user(telegram_id, username, referrer_id):
    cur.execute("INSERT OR REPLACE INTO users (telegram_id, username, RUB_balance, referrer_id) VALUES (?, ?, ?, ?)",
                (telegram_id, username, 0.0, referrer_id))
    conn.commit()


def count_referrals(telegram_id):
    cur.execute("SELECT COUNT(*) FROM users WHERE referrer_id = ?",
                (telegram_id,))
    referral_count = cur.fetchone()[0]
    return referral_count

