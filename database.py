# ═══════════════════════════════════════════════════════════════
#  db/queries.py  —  Saari Database Queries Yahan Hain
#  Agar koi query change karni ho toh sirf yeh file kholein.
#  UI (manage_stock.py) ko chhhuna bilkul zaroori nahi.
# ═══════════════════════════════════════════════════════════════

import mysql.connector
from config import DB_CONFIG


# ───────────────────────────────────────────────
#  Connection
# ───────────────────────────────────────────────

def get_connection():
    """MySQL se connection banao aur return karo."""
    conn = mysql.connector.connect(
        host     = DB_CONFIG["host"],
        port     = DB_CONFIG.get("port", 3306),
        user     = DB_CONFIG["user"],
        password = DB_CONFIG["password"],
        database = DB_CONFIG["database"],
    )
    return conn


# ───────────────────────────────────────────────
#  Setup
# ───────────────────────────────────────────────

def create_database_and_table(conn):
    """
    Agar database ya table exist nahi karta toh bana do.
    Yeh function sirf pehli baar (ya safe check ke liye) chalao.
    """
    cur = conn.cursor()
    cur.execute(f"CREATE DATABASE IF NOT EXISTS `{DB_CONFIG['database']}`")
    cur.execute(f"USE `{DB_CONFIG['database']}`")
    cur.execute("""
        CREATE TABLE IF NOT EXISTS stock (
            id          INT AUTO_INCREMENT PRIMARY KEY,
            description VARCHAR(255) NOT NULL DEFAULT '',
            stock       INT           DEFAULT 0,
            rate        DECIMAL(10,2) DEFAULT 0.00,
            updated_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                        ON UPDATE CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    cur.close()


# ───────────────────────────────────────────────
#  SELECT Queries
# ───────────────────────────────────────────────

def fetch_all_stock(conn):
    """
    Stock table se saara data lao, id ke order mein.
    Return: list of dicts  [{id, description, stock, rate}, ...]
    """
    cur = conn.cursor(dictionary=True)
    cur.execute("""
        SELECT id, description, stock, rate
        FROM   stock
        ORDER  BY id
    """)
    rows = cur.fetchall()
    cur.close()
    return rows


def fetch_stock_by_id(conn, stock_id):
    """
    Ek specific medicine ID se lao.
    Return: dict ya None
    """
    cur = conn.cursor(dictionary=True)
    cur.execute("""
        SELECT id, description, stock, rate
        FROM   stock
        WHERE  id = %s
    """, (stock_id,))
    row = cur.fetchone()
    cur.close()
    return row


def search_stock(conn, keyword):
    """
    Description mein keyword search karo (LIKE query).
    Return: list of dicts
    """
    cur = conn.cursor(dictionary=True)
    cur.execute("""
        SELECT id, description, stock, rate
        FROM   stock
        WHERE  description LIKE %s
        ORDER  BY id
    """, (f"%{keyword}%",))
    rows = cur.fetchall()
    cur.close()
    return rows


def fetch_low_stock(conn, threshold=5):
    """
    Woh medicines jo stock mein threshold se kam ya barabar hain.
    Default threshold = 5 units.
    Return: list of dicts
    """
    cur = conn.cursor(dictionary=True)
    cur.execute("""
        SELECT id, description, stock, rate
        FROM   stock
        WHERE  stock <= %s
        ORDER  BY stock ASC
    """, (threshold,))
    rows = cur.fetchall()
    cur.close()
    return rows


def fetch_stock_summary(conn):
    """
    Poori inventory ka summary: total medicines, total units, total value.
    Return: dict  {total_medicines, total_units, total_value}
    """
    cur = conn.cursor(dictionary=True)
    cur.execute("""
        SELECT
            COUNT(*)                        AS total_medicines,
            COALESCE(SUM(stock), 0)         AS total_units,
            COALESCE(SUM(stock * rate), 0)  AS total_value
        FROM stock
    """)
    row = cur.fetchone()
    cur.close()
    return row


# ───────────────────────────────────────────────
#  INSERT Queries
# ───────────────────────────────────────────────

def insert_empty_row(conn):
    """
    Ek khali row insert karo (Add Row button ke liye).
    Return: naya row ka id (int)
    """
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO stock (description, stock, rate)
        VALUES ('', 0, 0.00)
    """)
    conn.commit()
    new_id = cur.lastrowid
    cur.close()
    return new_id


def insert_stock(conn, description, stock, rate):
    """
    Ek nayi medicine directly insert karo.
    Return: naya row ka id (int)
    """
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO stock (description, stock, rate)
        VALUES (%s, %s, %s)
    """, (description, int(stock), float(rate)))
    conn.commit()
    new_id = cur.lastrowid
    cur.close()
    return new_id


# ───────────────────────────────────────────────
#  UPDATE Queries
# ───────────────────────────────────────────────

def update_stock_row(conn, stock_id, description, stock, rate):
    """
    Ek row update karo uske id se.
    Return: True agar successful
    """
    cur = conn.cursor()
    cur.execute("""
        UPDATE stock
        SET    description = %s,
               stock       = %s,
               rate        = %s
        WHERE  id = %s
    """, (description, int(stock), float(rate), stock_id))
    conn.commit()
    cur.close()
    return True


def update_stock_quantity(conn, stock_id, new_quantity):
    """
    Sirf stock quantity update karo (rate aur description change nahi hoga).
    """
    cur = conn.cursor()
    cur.execute("""
        UPDATE stock
        SET    stock = %s
        WHERE  id   = %s
    """, (int(new_quantity), stock_id))
    conn.commit()
    cur.close()


# ───────────────────────────────────────────────
#  DELETE Queries
# ───────────────────────────────────────────────

def delete_stock_by_id(conn, stock_id):
    """
    Ek medicine delete karo uske id se.
    Return: True agar successful
    """
    cur = conn.cursor()
    cur.execute("""
        DELETE FROM stock
        WHERE  id = %s
    """, (stock_id,))
    conn.commit()
    cur.close()
    return True


def delete_all_empty_rows(conn):
    """
    Woh saari rows delete karo jinki description khali hai.
    """
    cur = conn.cursor()
    cur.execute("""
        DELETE FROM stock
        WHERE  TRIM(description) = ''
    """)
    conn.commit()
    affected = cur.rowcount
    cur.close()
    return affected