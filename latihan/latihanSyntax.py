import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['dbbarang']
mycol = mydb['barang']


class Barang:
    __pesan = 'barang anda'
    nama = ''
    harga = ''
    jenis = ''

    def __init__(self, nama):
        print('ini kontruktor')
        # self.id = ''
        self.nama = nama
        self.harga = '0'
        self.jenis = 'null'
        self.get = ''
        self.update = ''

    def get_pesan(self):
        print(self.__pesan)
        for x in mycol.find():
            print(x)

    def set_barang(self, nama, harga, jenis):
        self.nama = nama
        self.harga = harga
        self.jenis = jenis
        x = mycol.insert_one(
            {'nama': self.nama, 'harga': self.harga, 'jenis': self.jenis})
        # x.inserted_id untuk menampikan id
        print(x.inserted_id)

    def update_barang(self, get, update):
        self.get = get
        self.update = update
        findone = mycol.find_one({}, {'nama': self.nama})
        # print(findone)

        # x = {'nama': 'mie gorang'}
        # # print(x)
        newvalue = {'$set': {'nama': self.update}}
        mycol.update_one(findone, newvalue)
        x = mycol.find_one()
        print(x)
        # for a in mycol.find():
        #     print(a)


p = Barang('mie gorang')
p.set_barang('ayam', 15000, 'makanan')
# p.get_pesan()
# p.update_barang('mei goreng', 'lalapan')
# print(p., p.harga, p.jenis)
