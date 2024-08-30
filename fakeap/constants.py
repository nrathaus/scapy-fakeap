"""constants"""
DEFAULT_DNS_SERVER = "8.8.8.8"
RSN = "\x01\x00\x00\x0f\xac\x04\x01\x00\x00\x0f\xac\x04\x01\x00\x00\x0f\xac\x01\x28\x00"

AP_WLAN_TYPE_OPEN = 0
AP_WLAN_TYPE_WPA = 1
AP_WLAN_TYPE_WPA2 = 2
AP_WLAN_TYPE_WPA_WPA2 = 3
AP_AUTH_TYPE_OPEN = 0
AP_AUTH_TYPE_SHARED = 1
# Tag: Supported Rates 6, 9, 12, 18, 24, 36, 48, 54, [Mbit/sec]
AP_RATES = b"\x0c\x12\x18\x24\x30\x48\x60\x6c"

# Tag: Supported Rates 1(B), 2(B), 5.5(B), 11(B), [Mbit/sec]
# AP_RATES = b"\x82\x84\x8b\x96"

# Tag: Supported Rates 1(B), 2(B), 5.5(B), 11(B), 6, 9, 12, 18, [Mbit/sec]
# AP_RATES = b"\x82\x84\x8b\x96\x0c\x12\x18\x24"

COUNTRY = (
    b"\x55\x53"  # US Code
    b"\x20"  # Environment Any
    b"\x08"  # First channel
    b"\x08"  # Last channel
    b"\x1e"
)  # Maximum transmit

# CAP = 'short-slot+res12+ESS+privacy+short-preamble'
# 0x2104 - PRIVACY_NONE
CAP = "short-slot+ESS+short-preamble"

# PRIVACY_WEP
# CAP = 'ESS+privacy+short-preamble+short-slot'

# PRIVACY_WPA
# CAP = "ESS+privacy+short-preamble+short-slot"

# https://github.com/blkph0x/CVE_2024_30078_POC_WIFI/blob/main/AP_Test.py#L15
CUSTOM_VSA = b"\xdd\x07\x00\x50\xf2\x02\x01\x01"

DOT11_MTU = 4096

DOT11_TYPE_MANAGEMENT = 0
DOT11_TYPE_CONTROL = 1
DOT11_TYPE_DATA = 2

DOT11_SUBTYPE_DATA = 0x00
DOT11_SUBTYPE_PROBE_REQ = 0x04
DOT11_SUBTYPE_AUTH_REQ = 0x0B
DOT11_SUBTYPE_ASSOC_REQ = 0x00
DOT11_SUBTYPE_REASSOC_REQ = 0x02
DOT11_SUBTYPE_QOS_DATA = 0x28


IFNAMSIZ = 16
IFF_TUN = 0x0001
IFF_TAP = 0x0002  # Should we want to tunnel layer 2...
IFF_NO_PI = 0x1000
TUNSETIFF = 0x400454CA
