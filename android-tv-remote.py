import argparse
import subprocess

def handle_connection(ip):
    if check_connection(ip) is False:
        if connect(ip) is False:
            return

def check_connection(ip):
    if ip in str(subprocess.check_output(['adb', 'devices'])):
        return True
    return False

def connect(ip, err_count=0):
    if "unable" in str(subprocess.check_output(['adb', 'connect', ip])):
        err_count += 1
        if err_count >= 3:
            print("Unable to connect to", ip, "after", err_count, "retries")
            return False
        else:
            return connect(ip, err_count)
    print("Connected to", ip)
    return True

def main():
    parser = argparse.ArgumentParser(description='Control Philips Android TVs')
    parser.add_argument("--host", dest='host', help="TV's ip address")
    parser.add_argument("--input", dest='input', help="TV's input source (1-6)")
    args = parser.parse_args()

    if args is None:
        return print("Please set your TV's IP-address with a --host parameter and an input mode (1-6) with an --input parameter")

    if args.host is None:
        return print("Please set your TV's IP-address with a --host parameter")

    if args.input is None:
        return print("Please set an input mode (1-6) with an --input parameter")

    sources={
        1: "KEYCODE_F1",
        2: "KEYCODE_F2",
        3: "KEYCODE_F3",
        4: "KEYCODE_F4",
        5: "KEYCODE_F5",
        6: "KEYCODE_F6",
    }

    handle_connection(args.host)

    if int(args.input) in sources:
        try:
            subprocess.check_output(['adb', 'shell', 'input', 'keyevent', sources[int(args.input)]])
        except:
            print("Error connecting to TV")
    else:
        print("Unknown input (should be a value between 1-6):", args.input)

if __name__ == '__main__':
    main()