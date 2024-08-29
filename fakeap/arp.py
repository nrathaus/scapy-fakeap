# arp.py
import threading

from rpyutils import Level, printd


class ARPHandler:
    def __init__(self):
        self.mutex = threading.Lock()
        self.arp_table = {}

    def add_entry(self, client_ip, client_mac):
        """add_entry"""
        self.mutex.acquire()
        if client_ip not in self.arp_table:
            self.arp_table[client_ip] = client_mac
        self.mutex.release()

    def get_entry(self, client_ip):
        """get_entry"""
        self.mutex.acquire()
        try:
            temp = self.arp_table[client_ip]
        except KeyError:
            temp = None
            # printd(f"Could not find IP {client_ip} in ARP table.", Level.WARNING)
        self.mutex.release()

        return temp
