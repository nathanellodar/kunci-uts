class Node:
    def __init__(self, data):
        self._data = data
        self._next = None
class LL:
    def __init__(self):
        self._head = None
    def insert(self, _data):
        new_node = Node(_data)
        if not self._head:
            self._head = new_node
        else:
            current = self._head
            while current._next:
                current = current._next
            current._next = new_node
    def tampilkata(self, n):
        current = self._head
        for i in range(n - 1):
            if current is None:
                return None
            current = current._next
        return current._data
def main():
    my_list = LL()
    kata_kata = input("Masukkan kata-kata: ").split()
    for kata in kata_kata:
        my_list.insert(kata)
    urutan_angka = input("Masukkan urutan angka: ").split()
    hasil = [my_list.tampilkata(int(angka)) for angka in urutan_angka if my_list.tampilkata(int(angka)) is not None]
    if hasil:
        print("Hasil:", ' '.join(hasil))
    else:
        print("Tidak ada hasil.")
if __name__ == "__main__":
    main()
