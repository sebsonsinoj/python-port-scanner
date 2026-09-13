import socket


def scan(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)

    result = s.connect_ex((ip, port))

    s.close()

    return result == 0


target = input("Enter IP address or hostname: ")

try:
    ip = socket.gethostbyname(target)

    print("Scanning", ip)
    print("--------------------")

    start = int(input("Starting port: "))
    end = int(input("Ending port: "))

    if start < 1 or end > 65535 or start > end:
        print("Invalid port range")

    else:
        found = 0

        for port in range(start, end + 1):

            if scan(ip, port):
                print("Port", port, "is open")
                found += 1

        print("--------------------")
        print("Open ports:", found)

except:
    print("Something went wrong. Check your input.")
