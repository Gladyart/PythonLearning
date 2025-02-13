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
userAttributes = ['accountExpires', 'badPwdCount', 'cn','description', 'displayName', 'distinguishedName', 'GivenName', 'HomeDirectory', 'HomeDrive', 'lastLogon', 'lockoutTime', 'mail', 'manager', 'pwdLastSet', 'sAMAccountName', 'sn', 'userAccountControl']

conn.search(OUPath, searchParameters, attributes=userAttributes)
# other attr: Enabled, PasswordExpired, MemberOf, 
   
entry = conn.entries[0]
print(entry)
 
print(entry.lockoutTime.value)
if entry.lockoutTime != None:
    print('Lck=none')
    conn.modify(f'{entry.distinguishedName}', {'lockoutTime': [(MODIFY_REPLACE, [0])]})
print(entry.lockoutTime)
print(entry.lockoutTime.raw_values[0].decode('utf-8'))
print(type(entry.lockoutTime.raw_values[0].decode('utf-8')))

# locked: # 2025-01-03 07:53:36.012011+00:00 | [b'133803644160120109']
# notlocked: 1601-01-01 00:00:00+00:00 | [b'0']

print(f"current =  {entry.userAccountControl}")
if entry.userAccountControl == 514:
    conn.modify(f'{entry.distinguishedName}',
                {'userAccountControl': [(MODIFY_REPLACE, [512])]})
elif entry.userAccountControl == 66050:
    conn.modify(f'{entry.distinguishedName}',
                {'userAccountControl': [(MODIFY_REPLACE, [66048])]})
    
conn.search(OUPath, searchParameters, attributes=userAttributes) 
entry = conn.entries[0]    
print(f"En - {entry.userAccountControl}")
if entry.userAccountControl == 512:
    conn.modify(f'{entry.distinguishedName}',
                {'userAccountControl': [(MODIFY_REPLACE, [514])]})
elif entry.userAccountControl == 66048:
    conn.modify(f'{entry.distinguishedName}',
                {'userAccountControl': [(MODIFY_REPLACE, [66050])]})
    
conn.search(OUPath, searchParameters, attributes=userAttributes) 
entry = conn.entries[0]    
print(f"Dis - {entry.userAccountControl}")    

'''
# Create a container for new entries
conn.add('ou=ldap3-tutorial,dc=demo1,dc=freeipa,dc=org', 'organizationalUnit')

# Add a new user
conn.add('cn=b.young,ou=ldap3-tutorial,dc=demo1,dc=freeipa,dc=org', 'inetOrgPerson', {'givenName': 'Beatrix', 'sn': 'Young', 'departmentNumber': 'DEV', 'telephoneNumber': 1111})

# Rename DN
conn.modify_dn(f'cn={userID},ou=ldap3-tutorial,dc=demo1,dc=freeipa,dc=org', f'cn={userID}')

# Move
conn.modify_dn(f'cn={userID},ou=ldap3-tutorial,dc=demo1,dc=freeipa,dc=org', f'cn={userID}', new_superior='ou=moved, ou=ldap3-tutorial,dc=demo1,dc=freeipa,dc=org')

from ldap3.utils.dn import safe_rdn
safe_rdn('cn=b.smith,ou=moved,ou=ldap3-tutorial,dc=demo1,dc=freeipa,dc=org')
# out [cn=b.smith]

# Modify
from ldap3 import MODIFY_ADD, MODIFY_REPLACE, MODIFY_DELETE

OUPath = 'OU=users,OU=MyDomain,dc=mydomain,dc=com'
searchParameters = f'(&(objectclass=person)(cn={userID}))'

class ModifyUser():

    conn.search(OUPath, searchParameters, attributes=['distinguishedName']) # distinguishedName only
    
    DN = str(conn.entries[0].distinguishedName) # out= CN=userID,OU=users,OU=MyDomain,dc=mydomain,dc=com

    # For later. Don't for loop, maybe conn.search per object OU?
    splitDN = DN.split(',') # out list= ['CN=userID', 'OU=users', 'OU=MyDomain', 'dc=mydomain', 'dc=com']
    


    def addAttributes(DN):
        conn.modify(DN, {'sn': [(MODIFY_ADD, ['Smyth'])]})

    def deleteAttributes(DN):
        conn.modify(DN, {'sn': [(MODIFY_DELETE, ['Young'])]})

    def replaceAttributes(DN):
        conn.modify(DN, {'sn': [(MODIFY_REPLACE, ['Smith'])]})

'''