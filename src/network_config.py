from abc import ABC, abstractmethod
import json
import os
import re
import sys
from typing import Optional


DHCP_VERSION = {"v4": "DHCPv4", "v6": "DHCPv6"}


class DHCP(ABC):
    def __init__(self, subnet: str, lease_time: Optional[int] = None) -> None:
        super().__init__()
        self._dhcp_table = self.load()
        self._subnet = subnet
        self._lease_time = lease_time

    @abstractmethod
    def gen_ip(self, mac_address: str) -> str:
        pass

    @abstractmethod
    def _dhcp_table_file(self) -> str:
        pass

    def load(self):
        if os.path.exists(self._dhcp_table_file()):
            with open(self._dhcp_table_file(), "r") as f:
                return json.loads(f.read())

        else:
            return {}

    def save(self):
        with open(self._dhcp_table_file(), "+w") as f:
            f.write(json.dumps(self.dhcp_table))

    @property
    def dhcp_table(self):
        return self._dhcp_table

    @property
    def subnet(self):
        return self._subnet

    @property
    def lease_time(self):
        return self._lease_time


class DHCPv4(DHCP):
    dhcp_table_file = "ipv4_dhcp_table.json"

    def __init__(self):
        super().__init__(subnet="192.168.1.0/24", lease_time=3600)

    def _dhcp_table_file(self) -> str:
        return "ipv4_dhcp_table.json"

    def gen_ip(self, mac_address: str) -> str:
        if self.dhcp_table.get(mac_address) is not None:
            return self.dhcp_table[mac_address]

        assigned_ipv4_list = self.dhcp_table.values()
        assigned_hosts = list(map(lambda ip: int(ip.split(".")[3]), assigned_ipv4_list))
        available_hosts = range(2, 254)

        new_host = None
        for host in available_hosts:
            if host in assigned_hosts:
                continue
            else:
                new_host = host
                break

        if new_host is None:
            print("I can't assign new IPv4 because all addresses are used.")
            exit(1)

        ip = "192.168.1." + str(new_host)
        self.dhcp_table[mac_address] = ip

        return ip


class DHCPv6(DHCP):
    def __init__(self):
        super().__init__(subnet="2001:db8::/64")

    def _dhcp_table_file(self) -> str:
        return "ipv6_dhcp_table.json"

    def gen_ip(self, mac_address: str) -> str:
        if self.dhcp_table.get(mac_address) is not None:
            return self.dhcp_table[mac_address]

        # Split mac address
        mac_address_hextets = mac_address.split(":")
        # Flip 7th bit of first byte
        mac_address_hextets[0] = (
            hex(int(mac_address_hextets[0], 16) ^ 0b00000010).replace("0x", "").upper()
        )

        eui64 = (
            ":".join(mac_address_hextets[0:3])
            + ":FF:FE:"
            + ":".join(mac_address_hextets[3:6])
        )
        eui64_hextets = eui64.split(":")
        interface_id = (
            "".join(eui64_hextets[0:2])
            + ":"
            + "".join(eui64_hextets[2:4])
            + ":"
            + "".join(eui64_hextets[4:6])
            + ":"
            + "".join(eui64_hextets[6:8])
        )

        ip = "2001:db8::" + interface_id
        self.dhcp_table[mac_address] = ip

        return ip


def validate_mad_address(mac_address: str):
    pattern = "^[a-fA-F0-9]{2}:[a-fA-F0-9]{2}:[a-fA-F0-9]{2}:[a-fA-F0-9]{2}:[a-fA-F0-9]{2}:[a-fA-F0-9]{2}$"
    if not re.match(pattern, mac_address):
        print(f'mac_address "{mac_address}" is invalid. Please input valid value.')
        exit(1)


mac_address = sys.argv[1]
dhcp_version = sys.argv[2]

validate_mad_address(mac_address)

dhcp: DHCP | None = None
if dhcp_version == DHCP_VERSION["v4"]:
    dhcp = DHCPv4()
elif dhcp_version == DHCP_VERSION["v6"]:
    dhcp = DHCPv6()

if dhcp is None:
    print('DHCP is invalid. Please select "DHCPv4" or "DHCPv6".')
    exit(1)

output = {
    "ip": dhcp.gen_ip(mac_address),
    "mac_address": mac_address,
    "lease_time": dhcp.lease_time,
    "subnet": dhcp.subnet,
}

print(json.dumps(output))

exit(0)
