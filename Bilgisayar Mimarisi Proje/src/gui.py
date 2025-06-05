import tkinter as tk
from tkinter import ttk, messagebox
from src.hamming_code import HammingCode

class HammingSimulatorGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Hamming SEC-DED Code Simülatörü")
        self.hamming = HammingCode()
        self.original_hamming = ""  # Orijinal Hamming kodunu saklamak için
        self.setup_gui()

    def setup_gui(self):
        # Ana frame
        main_frame = ttk.Frame(self.master, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Veri girişi
        ttk.Label(main_frame, text="Veri (8 bit):").grid(row=0, column=0, sticky=tk.W)
        self.data_entry = ttk.Entry(main_frame, width=20)
        self.data_entry.grid(row=0, column=1, padx=5, pady=5)

        # Hamming kodu hesaplama butonu
        ttk.Button(main_frame, text="Hamming Kodu Hesapla", 
                  command=self.calculate_hamming).grid(row=1, column=0, columnspan=2, pady=5)

        # Hamming kodu sonucu
        ttk.Label(main_frame, text="Hamming Kodu:").grid(row=2, column=0, sticky=tk.W)
        self.hamming_result = ttk.Label(main_frame, text="")
        self.hamming_result.grid(row=2, column=1, sticky=tk.W)

        # Hata oluşturma
        ttk.Label(main_frame, text="Hata Pozisyonu (1-12):").grid(row=3, column=0, sticky=tk.W)
        self.error_pos = ttk.Entry(main_frame, width=20)
        self.error_pos.grid(row=3, column=1, padx=5, pady=5)

        ttk.Button(main_frame, text="Hata Oluştur", 
                  command=self.create_error).grid(row=4, column=0, columnspan=2, pady=5)

        # Hatalı kod sonucu
        ttk.Label(main_frame, text="Hatalı Kod:").grid(row=5, column=0, sticky=tk.W)
        self.error_result = ttk.Label(main_frame, text="")
        self.error_result.grid(row=5, column=1, sticky=tk.W)

        # Hata düzeltme butonu
        ttk.Button(main_frame, text="Hata Düzelt", 
                  command=self.detect_and_correct_error).grid(row=6, column=0, columnspan=2, pady=5)

        # Düzeltilmiş kod sonucu
        ttk.Label(main_frame, text="Düzeltilmiş Kod:").grid(row=7, column=0, sticky=tk.W)
        self.corrected_result = ttk.Label(main_frame, text="")
        self.corrected_result.grid(row=7, column=1, sticky=tk.W)

    def calculate_hamming(self):
        try:
            data = int(self.data_entry.get())
            if data < 0 or data > 255:  # 8 bit kontrol
                messagebox.showerror("Hata", "Lütfen 0-255 arası bir sayı girin!")
                return
            hamming_code = self.hamming.calculate_hamming_code(data)
            self.hamming_result.config(text=hamming_code)
            self.original_hamming = hamming_code  # Orijinal Hamming kodunu sakla
        except ValueError:
            messagebox.showerror("Hata", "Geçerli bir sayı girin!")

    def create_error(self):
        try:
            pos = int(self.error_pos.get())
            if pos < 1 or pos > 12:
                messagebox.showerror("Hata", "Pozisyon 1-12 arası olmalıdır!")
                return
            hamming_code = self.hamming_result.cget("text")
            if not hamming_code:
                messagebox.showerror("Hata", "Önce Hamming kodu hesaplayın!")
                return
            # Hata oluştur
            hamming_list = list(hamming_code)
            hamming_list[pos-1] = str(1 - int(hamming_list[pos-1]))
            self.error_result.config(text=''.join(hamming_list))
            # Orijinal Hamming kodunu sakla
            self.original_hamming = hamming_code
        except ValueError:
            messagebox.showerror("Hata", "Geçerli bir pozisyon girin!")

    def detect_and_correct_error(self):
        error_code = self.error_result.cget("text")
        if not error_code:
            messagebox.showerror("Hata", "Önce hata oluşturun!")
            return
        if len(error_code) != 12:
            messagebox.showerror("Hata", "Geçersiz Hamming kodu uzunluğu!")
            return
        # Orijinal Hamming kodunu göster
        self.corrected_result.config(text=self.original_hamming) 