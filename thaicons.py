Python 3.12.4 (v3.12.4:8e8a4baf65, Jun  6 2024, 17:33:18) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import tkinter as tk
... import random
... 
... # List of Thai consonants with their names
... thai_consonants = [
...     ("ก", "กอ ไก่"), ("ข", "ขอ ไข่"), ("ค", "คอ ควาย"), ("ง", "งอ งู"),
...     ("จ", "จอ จาน"), ("ฉ", "ฉอ ฉิ่ง"), ("ช", "ชอ ช้าง"), ("ซ", "ซอ โซ่"),
...     ("ญ", "ญอ หญิง"), ("ฎ", "ฎอ ชฎา"), ("ฐ", "ฐอ ฐาน"), ("ฑ", "ฑอ มณโฑ"),
...     ("ท", "ทอ ทหาร"), ("น", "นอ หนู"), ("บ", "บอ ใบไม้"), ("ป", "ปอ ปลา"),
...     ("พ", "พอ พาน"), ("ฟ", "ฟอ ฟัน"), ("ม", "มอ ม้า"), ("ร", "รอ เรือ"),
...     ("ล", "ลอ ลิง"), ("ว", "วอ แหวน"), ("ส", "สอ เสือ"), ("ห", "หอ หีบ")
... ]
... 
... # Shuffle the consonants
... random.shuffle(thai_consonants)
... 
... class FlashcardApp:
...     def __init__(self, root):
...         self.root = root
...         self.root.title("Thai Consonant Flashcards")
...         
...         self.current_index = 0
...         self.flipped = False
...         
...         self.card_frame = tk.Frame(root, width=300, height=200, bg="white", bd=2, relief="ridge")
...         self.card_frame.pack(pady=20)
...         
...         self.label = tk.Label(self.card_frame, text="", font=("Arial", 50), bg="white")
...         self.label.pack(expand=True)
...         
...         self.flip_button = tk.Button(root, text="Flip", command=self.flip_card)
...         self.flip_button.pack(side="left", padx=10, pady=10)
...         
...         self.next_button = tk.Button(root, text="Next", command=self.next_card)
...         self.next_button.pack(side="right", padx=10, pady=10)
        
        self.show_card()
    
    def show_card(self):
        self.flipped = False
        consonant, _ = thai_consonants[self.current_index]
        self.label.config(text=consonant)
    
    def flip_card(self):
        if not self.flipped:
            _, name = thai_consonants[self.current_index]
            self.label.config(text=name)
            self.flipped = True
        else:
            self.show_card()
    
    def next_card(self):
        self.current_index = (self.current_index + 1) % len(thai_consonants)
        self.show_card()

if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardApp(root)
    root.mainloop()
