import struct

with open('spec-0285-51930-0184.fits', mode='rb') as f:
    a = f.read()


b1 = a[:2880]
b2 = a[2880:2880*2]
b3 = a[2880:2880*3]
b4 = a[2880:2880*4]
b5 = a[2880:2880*5]
b6 = a[2880:2880*6]



keyword_records = [b1[i*80 : i*80+80].decode('utf-8') for i in range(30)]

keyword_names = [i[:8] for i in keyword_records]
value_indicators = [i[8:10] for i in keyword_records] # if not '= ' means no value
value_comment = [i[10:] for i in keyword_records]
value = [i.split(' /')[0] for i in value_comment]
comment = [i.split(' /')[-1] for i in value_comment]
