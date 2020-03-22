class Produk:
    __vendor_massage = 'ini rahasia'
    nama = ''
    harga = ''
    unit = ''

    def __init__(self, nama):
        # ini adalah contruktor
        self.nama = nama
        self.harga = '2500'
        self.unit = 'ml'

    def get_vendor_massage(self):
        print(self.__vendor_massage)

    def set_harga(self, harga):
        self.harga = harga


p = Produk('mie goreng')
p.set_harga(3500)

print(p.nama, p.harga, p.unit)
