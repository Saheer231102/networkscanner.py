import argparse
import nmap

def argument_parser():
    parser = argparse.ArgumentParser(description = "TCP port scanner. accept a hostname/IP address and list of ports to scan. Attempts to identify the service running as a port.")
    parser.add_argument("-o", "--host", required=True, help = "Host Ip address")
    parser.add_argument("-p", "--port", default="21,22,23,25,53,80,110,111,135,143,443,445,993,1723,3306,3389,5900,8080", help = "comma-seperation port list, such as '80,227,143'")
    args = vars(parser.parse_args())
    return args

def nmap_scan(host_id, port_num):
    nm_scan = nmap.PortScanner()
    nm_scan.scan(host_id, port_num)
    try:
        state = nm_scan[host_id]['tcp'][int(port_num)]['state']
    except KeyError:
        state = "closed"
    result=("{port} [&] {host} tcp/port {state}".format(host=host_id, port=port_num, state=state))
    return result

if __name__ == '__main__':
    try:
        user_args = argument_parser()
        host = user_args["host"]
        ports = user_args["port"]
        for port in ports.split(","):
            print(nmap_scan(host,port))
    except AttributeError as e:
        if e.args[0] == "'port'":
            print("Error, please provide the list of ports to scan before running.")
        else:
            raise e
