import os
import subprocess


def read_mac_addresses(file_path):
    """
    Reads in a text file containing MAC addresses, one per line, and
    returns a list of them
    """
    mac_addresses = []
    with open(file_path, 'r') as f:
        for line in f:
            mac_addresses.append(line.strip())
    return mac_addresses


def run_tshark(mac_addresses, input_file):
    """
    Runs the TShark command for each MAC address in the list, with the
    -r flag set to the input file, the -Y flag set to filter for the
    MAC address, and the -w flag set to write to a unique file in the
    output folder
    """
    output_folder = "pycap_output"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    for mac in mac_addresses:
        output_file = os.path.join(output_folder, mac.remove(':') + '.pcap')
        command = f"C:\\\"Program Files\"\\Wireshark\\tshark.exe -r " \
                  f"{input_file} -Y \"wlan.addr == {mac}\" -w " \
                  f"{output_file}"
        subprocess.run(command, shell=True)


def merge_pcap(input_files, output_file):
    """
    Merges the input pcap files into a single output file using the
    mergecap command
    """
    input_files_str = ' '.join(input_files)
    command = f"C:\\\"Program Files\"\\Wireshark\\mergecap.exe -w {output_file} {input_files_str}"
    subprocess.run(command, shell=True)


def main_menu():
    """
    Displays a menu to the user with options to read in mac
    addresses, run TShark, and merge pcap files
    """
    while True:
        print("1. Read in MAC addresses from file")
        print("2. Run TShark on input file for each MAC address")
        print("3. Merge pcap files")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            file_path = input("Enter the file path: ")
            mac_addresses = read_mac_addresses(file_path)
            print(f"Read in {len(mac_addresses)} MAC addresses from {file_path}")
        elif choice == '2':
            input_file = input("Enter the input file path: ")
            run_tshark(mac_addresses, input_file)
            print("Completed running TShark on input file for each MAC address")
        elif choice == '3':
            input_files = input("Enter the input file paths, separated by commas: ").split(',')
            output_file = input("Enter the output file path: ")
            merge_pcap(input_files, output_file)
            print("Completed merging pcap files")
        elif choice == '4':
            break
        else:
            print("Invalid choice, please try again")


# Run the main menu
main_menu()
