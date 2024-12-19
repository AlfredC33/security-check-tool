import os
import subprocess

def check_firewall():
    """Check if the firewall is active."""
    print("Checking firewall status...")
    try:
        if os.name == "nt":  # Windows
            result = subprocess.run(["netsh", "advfirewall", "show", "allprofiles"], capture_output=True, text=True)
            if "State ON" in result.stdout:
                print("Firewall is enabled.")
            else:
                print("Firewall is disabled.")
        else:  # Linux/Mac
            result = subprocess.run(["sudo", "ufw", "status"], capture_output=True, text=True)
            if "Status: active" in result.stdout:
                print("Firewall is enabled.")
            else:
                print("Firewall is disabled.")
    except Exception as e:
        print(f"Error checking firewall: {e}")


def check_open_ports():
    """Check for open ports."""
    print("\nChecking open ports...")
    try:
        if os.name == "nt":  # Windows
            result = subprocess.run(["netstat", "-an"], capture_output=True, text=True)
            print("Open ports:")
            print(result.stdout)
        else:  # Linux/Mac
            result = subprocess.run(["sudo", "netstat", "-tuln"], capture_output=True, text=True)
            print("Open ports:")
            print(result.stdout)
    except Exception as e:
        print(f"Error checking open ports: {e}")


def check_ssh_config():
    """Check if SSH is configured securely."""
    print("\nChecking SSH configuration...")
    try:
        if os.name != "nt":  # Linux/Mac
            ssh_config_path = "/etc/ssh/sshd_config"
            if os.path.exists(ssh_config_path):
                with open(ssh_config_path, "r") as file:
                    config = file.read()
                    if "PermitRootLogin no" in config:
                        print("Root login via SSH is disabled (good).")
                    else:
                        print("Warning: Root login via SSH is enabled.")
                    if "PasswordAuthentication no" in config:
                        print("Password authentication is disabled (good).")
                    else:
                        print("Warning: Password authentication is enabled.")
            else:
                print("SSH configuration file not found.")
        else:
            print("SSH configuration checks are not applicable on Windows.")
    except Exception as e:
        print(f"Error checking SSH configuration: {e}")


if __name__ == "__main__":
    print("System Security Check Tool\n")
    check_firewall()
    check_open_ports()
    check_ssh_config()
    print("\nSecurity check completed.")
