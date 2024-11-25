# Command Injection Example
import os

def execute_ping():
    ip = input("Enter an IP address or hostname to ping: ")
    # Vulnerable to command injection
    os.system(f"ping -c 4 {ip}")

if __name__ == "__main__":
    print("Command Injection Demo")
    execute_ping()
