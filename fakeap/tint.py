# tint.py
import fcntl
import os
import struct
import threading

from constants import DOT11_MTU, IFF_NO_PI, IFF_TUN, IFNAMSIZ, TUNSETIFF
from rpyutils import set_ip_address
from scapy.layers.inet import IP


class TunInterface(threading.Thread):
    def __init__(self, ap, name="fakeap"):
        threading.Thread.__init__(self)

        if len(name) > IFNAMSIZ:
            raise Exception(f"Tun interface name cannot be larger than {IFNAMSIZ}")

        self.name = name
        self.daemon = True
        self.ap = ap

        # Virtual interface
        # https://stackoverflow.com/questions/69801765/opening-tun-interface-throws-either-io-unsupportedoperation-or-filenotfounderror (why not to use open)
        self.fd = os.open("/dev/net/tun", os.O_RDWR)
        ifr_flags = IFF_TUN | IFF_NO_PI  # Tun device without packet information
        ifreq = struct.pack("16sH", name.encode(), ifr_flags)
        fcntl.ioctl(self.fd, TUNSETIFF, ifreq)  # Syscall to create interface

        # Assign IP and bring interface up
        set_ip_address(name, self.ap.ip)

        print(
            f"Created TUN interface {name} at {self.ap.ip}. Bind it to your services if needed."
        )

    def write(self, pkt):
        """write"""
        os.write(self.fd, str(pkt[IP]))  # Strip layer 2

    def read(self):
        """read"""
        raw_packet = os.read(self.fd, DOT11_MTU)
        return raw_packet

    def close(self):
        """close"""
        os.close(self.fd)

    def run(self):
        """run"""
        while True:
            raw_packet = self.read()
            self.ap.callbacks.cb_tint_read(raw_packet)
