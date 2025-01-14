from ldap3 import Server, Connection, ALL

userID = 'Admin'
#userID = 'gladyart' # not sure what is wrong now, worked before with just a string
OUPath = 'OU=Users,OU=MyDomain,dc=mydomain,dc=com'


server = Server("192.168.0.17", use_ssl=False, get_info=ALL)

conn = Connection(server, f'cn={userID},{OUPath}', 'Secret123', auto_bind=True)


searchParameters = '(&(objectclass=organizationalUnit)(OU=Users))'

conn.search('OU=MyDomain,dc=mydomain,dc=com', searchParameters, attributes=['distinguishedName', 'objectclass'])

print(conn.entries[0])

DN = str(conn.entries[0].distinguishedName)

splitDN = DN.split(',')

print(splitDN)