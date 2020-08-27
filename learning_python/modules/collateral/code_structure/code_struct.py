# IMPORTS
import re  # noqa

# CONSTANTS
DNS1 = "8.8.8.8"
DNS2 = "8.8.4.4"


# FUNCTIONS/CLASSES
def dns_ip(dns="8.8.8.8"):
    print(f"DNS Server: {dns}")


# MAIN FUNCTION
def main():
    dns_ip()
    dns_ip(dns="1.1.1.1")

    print(DNS1)
    print(DNS2)


if __name__ == "__main__":
    main()
