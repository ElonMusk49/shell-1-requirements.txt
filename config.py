import os

w = open('config.json', 'w+')
w.write('{')
w.write('\n')
w.write('    "authToken": "'+os.getenv('5588686540:AAFE6WuOHr7Q0hlIirshsOIYXhfbyKzliDg')+'",')
w.write('\n')
w.write('    "owner": '+os.getenv('5455166957'))
w.write('\n')
w.write('}')
