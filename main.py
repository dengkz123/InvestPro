from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class InvestPro(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", padding=10, spacing=10, **kwargs)

        self.add_widget(Label(text="INVESTPRO", font_size=28, size_hint=(1,0.1)))

        self.modal = TextInput(
            hint_text="Modal (Rp)",
            multiline=False,
            input_filter="float",
            size_hint=(1,None),
            height=50
        )
        self.add_widget(self.modal)

        self.apr = TextInput(
            hint_text="APR (%)",
            multiline=False,
            input_filter="float",
            size_hint=(1,None),
            height=50
        )
        self.add_widget(self.apr)

        self.hari = TextInput(
            hint_text="Lama Investasi (Hari)",
            multiline=False,
            input_filter="int",
            size_hint=(1,None),
            height=50
        )
        self.add_widget(self.hari)

        btn_hitung = Button(text="Hitung", size_hint=(1,None), height=50)
        btn_hitung.bind(on_press=self.hitung)
        self.add_widget(btn_hitung)

        btn_simpan = Button(text="Simpan Riwayat", size_hint=(1,None), height=50)
        btn_simpan.bind(on_press=self.simpan)
        self.add_widget(btn_simpan)

        self.hasil = Label(text="Keuntungan: Rp0\nTotal: Rp0", size_hint=(1,0.2))
        self.add_widget(self.hasil)

        self.riwayat = Label(text="Riwayat:\nBelum ada data", valign="top")
        self.add_widget(self.riwayat)

        self.data = []

    def hitung(self, instance):
        try:
            modal = float(self.modal.text)
            apr = float(self.apr.text)
            hari = int(self.hari.text)

            keuntungan = modal * (apr/100) * (hari/365)
            total = modal + keuntungan

            self.hasil.text = (
                f"Keuntungan: Rp{keuntungan:,.2f}\n"
                f"Total: Rp{total:,.2f}"
            )
        except:
            self.hasil.text = "Input tidak valid"

    def simpan(self, instance):
        try:
            modal = float(self.modal.text)
            apr = float(self.apr.text)
            hari = int(self.hari.text)

            keuntungan = modal * (apr/100) * (hari/365)
            total = modal + keuntungan

            teks = f"Modal Rp{modal:,.0f} | Untung Rp{keuntungan:,.0f} | Total Rp{total:,.0f}"
            self.data.append(teks)

            self.riwayat.text = "Riwayat:\n" + "\n".join(self.data)

        except:
            self.riwayat.text = "Gagal menyimpan"

class InvestProApp(App):
    def build(self):
        return InvestPro()

InvestProApp().run()