#!/usr/bin/python3
import sqlite3

# Init SQL Server
def init_db():
    connection = sqlite3.connect("main.db")
    cursor = connection.cursor()

    cursor.execute("""
                CREATE TABLE IF NOT EXISTS services (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                port INTEGER NOT NULL,
                protocol TEXT NOT NULL,
                service TEXT NOT NULL,
                cli_tool TEXT NOT NULL,
                description TEXT
    );
    """)

    cursor.execute("""
            CREATE TABLE IF NOT EXISTS credentials (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                service TEXT NOT NULL,
                username TEXT NOT NULL,
                password TEXT NOT NULL
    );
    """)

    services_data = [
        (21, "tcp", "ftp", "nmap -p 21 --script=ftp-anon {IP}", "FTP anonymous access check"),
        (22, "tcp", "ssh", "nmap -p 22 --script=ssh-auth-methods {IP}", "SSH authentication methods"),
        (25, "tcp", "smtp", "nmap -p 25 --script=smtp-enum-users {IP}", "SMTP user enumeration"),
        (80, "tcp", "http", "nmap -p 80 --script=http-enum {IP}", "HTTP service scan"),
        (445, "tcp", "smb", "crackmapexec smb {IP}", "SMB enumeration"),
        (3306, "tcp", "mysql", "nmap -p 3306 --script=mysql-info {IP}", "MySQL enumeration"),
    ]

    credentials_data = [
        ("ftp", "anonymous", "anonymous"),
        ("mysql", "root", "toor"),
        ("smb", "admin", "admin123"),
    ]

    #cursor.executemany("INSERT INTO services (port, protocol, service, cli_tool, description) VALUES (?, ?, ?, ?, ?)", services_data)
    #cursor.executemany("INSERT INTO credentials (service, username, password) VALUES (?, ?, ?)", credentials_data)

    # Commit changes and close connection
    connection.commit()
    connection.close()

    print("[+] Database successfully initialized.")