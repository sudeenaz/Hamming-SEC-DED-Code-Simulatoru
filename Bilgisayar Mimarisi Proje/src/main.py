import os
import sys

# Proje kök dizinini Python path'ine ekle
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import tkinter as tk
from src.gui import HammingSimulatorGUI

if __name__ == '__main__':
    root = tk.Tk()
    app = HammingSimulatorGUI(root)
    root.mainloop() 