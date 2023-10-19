## ini

class Node:
    def __init__(self, data):
        self._data = data
        self._next = self
class Penumpang:
    _nama = ''
    _berat = 0
    def setNama(self, nama):
        self._nama = nama
    def setBerat(self, berat):
        self._berat = berat
    def getNamaBerat(self):
        return ({'nama' : self._nama, 'berat' : self._berat})
class STACK:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
    def __len__(self):
        return self._size
    def push(self, nama, berat):
        data_baru = Penumpang()
        data_baru.setNama(nama)
        data_baru.setBerat(berat)
        if self.__len__() == 0:
            self._head = data_baru
            self._tail = data_baru
            self._tail._next = self._head
        else:
            data_baru._next = self._head
            self._head = data_baru
        self._size += 1
        print(f'Data {nama} ({berat} kg) tersimpan')
    def pop(self):
        if self.__len__() == 0:
            print('belum ada penumpang')
        else:
            d = None
            if self._head._next == self._head:
                d = self._head._data
                self._head = None
            else:
                hapus = self._head
                d = hapus._data
                self._head = self._head._next
                hapus._next = None
            del hapus
            self._size -= 1
    def printAll(self):
        if self.__len__() == 0:
            print('Penumpang Kosong')
        else:
            pembantu = self._head
            while pembantu != none:
                print(pembantu._data, end=" ")
                pembantu = pembantu._next
                print()
                

if __name__ == '__main__':
    total_terisi = 0
    daftar_isi = []
    orang = STACK()
    while True:
        print('Pilih Menu')
        print('1. Tambah Penumpang')
        print('2. Lihat Penumpangg')
        print('3. Keluar')
        pilihan = int(input('Pilihan Anda: '))
        if pilihan == 3:
            break
        elif pilihan == 1:
            nama = input('Masukkan nama :')
            berat = int(input('Masukkan berat :'))
            if total_terisi < 1000:
                total_terisi += berat
                if total_terisi < 1000:
                    orang.push(nama, berat)
                    data = {'nama' : nama, 'berat' : berat}
                    daftar_isi.append(data)
                else:
                    berat_total_sekarang = total_terisi + berat
                    while berat_total_sekarang > 1000:
                        pass
        elif pilihan == 2:
            orang = STACK()
            orang.printAll()
