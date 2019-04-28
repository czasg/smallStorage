# when you storage the password, fi you use the source, it will be dangerous when database revealed
# so you can storage the hash password, each login account it will calculate again to match the
# enciphered data

from hashlib import md5
m5 = md5()
m5.update(bytes)
m5.update(another_bytes)
result = m5.hexdigest()

from hashlib import sha1
sh1 = sha1()
sh1.update(bytes)
sh1.update(another_bytes)
result = sh1.hexdigest()

import hmac
hc = hmac.new(salt, enciphered_data, 'MD5')
hc.update(other_enciphered_data_if_need)
result = hc.hexdigest()