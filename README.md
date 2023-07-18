scanner.py - TCP Port Scanner

This Python script, named scanner.py, is a TCP port scanner that allows you to scan a specified hostname/IP address for open ports. It utilizes the argparse and nmap modules to provide a user-friendly command-line interface and perform the scanning operation.

Usage

To run the script, execute the scanner.py file from the command line with the necessary arguments. The available command-line options are as follows:

-o or --host: Specifies the hostname or IP address of the target to scan. This argument is required.
-p or --port: Specifies the list of ports to scan. It accepts a comma-separated list of port numbers. If not provided, a default set of ports will be scanned.
Example Usage:

*'''"python scanner.py -o 192.168.0.1 -p 80,443,8080"

This command will scan the host with the IP address 192.168.0.1 for open ports 80, 443, and 8080.

Scanning Process

The script uses the argparse module to parse the command-line arguments and retrieve the specified host and port values. It then utilizes the nmap module to perform the actual port scanning.

The nmap_scan function is responsible for conducting the scan on a given host and port. It creates a nmap.PortScanner object and uses its scan method to scan the specified host and port. The result is then obtained from the scan object and stored in the state variable. If the port is not found in the scan results, it is assumed to be "closed."

Finally, the script iterates through each port provided by the user, invoking the nmap_scan function for each port. The scan results, including the host, port, and state, are printed to the console.