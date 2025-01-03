from ldap3 import Server, Connection, ALL
from ldap3 import MODIFY_ADD, MODIFY_DELETE, MODIFY_REPLACE


userID = 'Admin'
#userID = 'gladyart' # not sure what is wrong now, worked before with just a string
OUPath = 'OU=users,OU=MyDomain,dc=mydomain,dc=com'


server = Server("192.168.0.17", use_ssl=False, get_info=ALL)

conn = Connection(server, f'cn={userID},{OUPath}', 'Secret123', auto_bind=True)

# connection test user
# no TLS config applied yet

def connectADServer(server, userID, OUPath):
    conn = Connection(server, f'cn={userID},{OUPath}', 'Secret123', auto_bind=True)

    return conn

#conn.search('cn=users,dc=mydomain,dc=com', '(objectclass=person)')
# output: [CN=gladyart,CN=Users,DC=mydomain,DC=com]
user = 'gladyart'

searchParameters = f'(&(objectclass=person)(cn={user}))'
# specify attr, will use on user page
# output is sorted alfabetically by key
## for later:
# searchParameters = f'(&(objectclass=person)(cn=*{searched}*))'
# searchParameters = f'(&(givenName={firstName}*)(mail=*@example.org))'

conn.search(OUPath, searchParameters, attributes=['accountExpires', 'description', 'displayName','lastLogon', 'lockoutTime', 'mail', 'manager', 'pwdLastSet', 'sAMAccountName'])
# other attr: Enabled, PasswordExpired, MemberOf, 
    
entry = conn.entries[0]
print(entry)

print(entry.lockoutTime.value)
print(entry.lockoutTime.raw_values[0].decode('utf-8'))

# locked: # 2025-01-03 07:53:36.012011+00:00 | [b'133803644160120109']
# notlocked: 1601-01-01 00:00:00+00:00 | [b'0']