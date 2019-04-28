# to guess the Coding Form of bytes

import chardet
chardet.detect(bytes_of_html)
-> return {'encoding': 'ascii', 'confidence': 1.0, 'language': ''}
-> os it's encoding maybe ascii in confidence 1.0