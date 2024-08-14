with open('data.tsv', 'r') as data:
    rows = [ line.strip().split('\t') for line in data ]
for row in rows:
    mmsid = row[0]
    umr = row[1]
    barcode = row[2]
    #print (mmsid, umr, barcode)

    # This does
    # addSubField "TMZ.a.UMR1" if ( exists "TMZ.b.99188039715706381" )
    #print(f'addSubField "TMZ.a.{umr}" if ( exists "TMZ.b.{mmsid}" )')

    # This does
    # addSubField "TMY.v.UMR1" if ( exists "TMY.b.99188039715706381" )
    #print (f'addSubField "TMY.v.{umr}" if ( exists "TMY.b.{mmsid}" )')

    # This does
    # addSubField "TMU.p.123" if ( exists "TMU.b.99188039715706381" )
    print (f'addSubField "TMU.p.{barcode}" if ( exists "TMU.b.{mmsid}" )')


# for i in range(5):
#     new_i = i + 1
#     extracted_digits = f"{new_i:04d}"
#     print(f'addSubField "TMZ.v.UMR{new_i}" if ( exists "TMZ.b.{new_i}" )')