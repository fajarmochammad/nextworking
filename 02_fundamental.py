kamus = {}
kamus['ayah'] = 'father'
kamus['ibu'] = 'mother'

print(kamus.values())

data_driver = {
    'driver' : [
        {'nama':'joko', 'jarak' : 1000},
        {'nama' : 'paijo', 'jarak' : 200}, 
        {'nama' :'lisno', 'jarak': 300 }
    ],
    'tanggal' : '2021-07-08'
}

print (f"Data driver disekitar: {data_driver['driver'][0]['nama']} dengan jarak {data_driver['driver'][0]['jarak']}")
print (f"pada tanggal: {data_driver['tanggal']}")

for i in data_driver['driver']:
    print (f"nama {i['nama']} berjarak {i['jarak']}")