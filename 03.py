import struct

BEG_PRM = 'SIMPLE  '
BEG_EXT = 'XTENSION'
END = 'END' + ' '*77

def read_blk(b):
    kw_recs = [b[i*80 : i*80+80].decode('utf-8') for i in range(36)]

    # Type
    dc_type = {'prm':None, 'ext':None, 'fin':None}
    
    if BEG_PRM in kw_recs[0]:
        dc_type['prm'] = True
        dc_type['ext'] = False
    elif BEG_EXT in kw_recs[0]:
        dc_type['prm'] = False
        dc_type['ext'] = True

    if END in kw_recs:
        kw_recs = kw_recs[: kw_recs.index(END)+1]
        dc_type['fin'] = True
    else:
        dc_type['fin'] = False
        
    kw_names = [i[:8] for i in kw_recs]
    # value indicators : if not '= ' means no value
    val_ind = [i[8:10] for i in kw_recs]
    value_comment = [i[10:] for i in kw_recs]
    val = [i.split(' /')[0] for i in value_comment]
    comment = [i.split(' /')[-1] for i in value_comment]
    return kw_recs, kw_names, val_ind, val, comment, dc_type


with open('spec-0285-51930-0184.fits', mode='rb') as f:
    a = f.read()

# create blocks
# =============
c = [*range(0, len(a), 2880)]

blocks = []
for i in range(len(c)):
    if i < len(c)-1:
        blocks.append(a[ c[i] : c[i+1] ])
        print(c[i] , ':',  c[i+1])
    else:
        blocks.append(a[ c[i] : ])
        print(c[i] , ':')


data = []
i = 0
for b in blocks:
    i += 1
    kw_recs, kw_names, val_ind, val, comment, dc_type = read_blk(b)
    data.append([kw_recs, kw_names, val_ind, val, comment, dc_type])
