import json
import sys
from collections import OrderedDict
from pyasn1.codec.der.decoder import decode  # $ pip install pyasn1
from pyasn1_modules import rfc2459  # $ pip install pyasn1_modules

OID = rfc2459.AttributeType
oid2name = {  # rfc 5280 (successor of rfc 2459)
    OID('2.5.4.3'): 'commonName',
    OID('2.5.4.5'): 'serialNumber',
    OID('2.5.4.6'): 'countryName',
    OID('2.5.4.7'): 'localityName',
    OID('2.5.4.8'): 'stateOrProvinceName',
    OID('2.5.4.9'): 'streetAddress',
    OID('2.5.4.10'): 'organizationName',
    OID('2.5.4.11'): 'organizationalUnitName',
    OID('2.5.4.17'): 'postalCode',
}
with open(sys.argv[1], 'rb') as der_file:
    cert, rest = decode(der_file.read(), asn1Spec=rfc2459.Certificate())
    assert not rest  # file contains only the certificate
    rdnsequence, = cert['tbsCertificate']['subject']
    d = OrderedDict()
    for rdn, in rdnsequence:  # NOTE: rdn.prettyPrintType() is your friend
        comp, rest = decode(rdn['value'], asn1Spec=rfc2459.X520name())
        assert not rest
        assert comp.getName() == 'utf8String'
        d[oid2name[rdn['type']]] = bytes(comp['utf8String']).decode('utf-8')
    json.dump(d, sys.stdout, indent=2, ensure_ascii=False)