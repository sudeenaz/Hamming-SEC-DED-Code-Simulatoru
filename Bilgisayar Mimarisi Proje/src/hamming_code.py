class HammingCode:
    def __init__(self):
        pass

    def calculate_hamming_code(self, data):
        # Veriyi binary string'e çevir
        binary_data = bin(data)[2:].zfill(8)  # 8 bit için
        
        # Hamming kod pozisyonları (1'den başlayarak)
        # p1, p2, d1, p3, d2, d3, d4, p4, d5, d6, d7, d8
        hamming = ['0'] * 12
        
        # Veri bitlerini yerleştir
        data_index = 0
        for i in range(12):
            if i not in [0, 1, 3, 7]:  # Kontrol bit pozisyonları
                hamming[i] = binary_data[data_index]
                data_index += 1
        
        # Kontrol bitlerini hesapla
        # p1: 1,3,5,7,9,11
        hamming[0] = str(self._calculate_parity([hamming[i] for i in [2,4,6,8,10]]))
        # p2: 2,3,6,7,10,11
        hamming[1] = str(self._calculate_parity([hamming[i] for i in [2,5,6,9,10]]))
        # p3: 4,5,6,7
        hamming[3] = str(self._calculate_parity([hamming[i] for i in [4,5,6,7]]))
        # p4: 8,9,10,11
        hamming[7] = str(self._calculate_parity([hamming[i] for i in [8,9,10,11]]))
        
        return ''.join(hamming)

    def _calculate_parity(self, bits):
        # XOR işlemi ile parite hesapla
        return sum(int(bit) for bit in bits) % 2

    def detect_error(self, hamming_code):
        # Sendrom hesapla
        # p1: 1,3,5,7,9,11
        s1 = self._calculate_parity([hamming_code[i] for i in [0,2,4,6,8,10]])
        # p2: 2,3,6,7,10,11
        s2 = self._calculate_parity([hamming_code[i] for i in [1,2,5,6,9,10]])
        # p3: 4,5,6,7
        s3 = self._calculate_parity([hamming_code[i] for i in [3,4,5,6]])
        # p4: 8,9,10,11
        s4 = self._calculate_parity([hamming_code[i] for i in [7,8,9,10]])
        
        # Hata pozisyonunu hesapla
        error_pos = s1 + 2*s2 + 4*s3 + 8*s4
        
        return error_pos if 0 < error_pos <= 12 else 0

    def correct_error(self, hamming_code):
        if not hamming_code or len(hamming_code) != 12:
            return hamming_code

        # Hatalı koddan veri bitlerini çıkar
        data_bits = []
        for i in range(12):
            if i not in [0, 1, 3, 7]:  # Kontrol bit pozisyonları
                data_bits.append(hamming_code[i])
        
        # Veri bitlerini decimal sayıya çevir
        data = int(''.join(data_bits), 2)
        
        # Orijinal Hamming kodunu hesapla
        return self.calculate_hamming_code(data) 