class Barang:
    __pesan = 'init barang'
    nama = ''
    harga = ''
    stok = ''

    def __init__(self):
        self.nama = ''
        self.harga = '0'
        self.stok = '0'

    def get_barang(self):
        print('nama barang : ', self.nama, 'harga : ',
              self.harga, 'stok : ', self.stok)

    def set_barang(self, nama, harga, stok):
        self.nama = nama
        self.harga = harga
        self.stok = stok


# p = barang()
# p.set_barang('lifeboy', 2000, 100)
# p.get_barang()
