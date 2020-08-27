def dns_ip(dns="8.8.8.8"):
    print(f"DNS Server: {dns}")


def main():
    dns_ip()
    dns_ip(dns="1.1.1.1")


if __name__ == "__main__":
    main()
