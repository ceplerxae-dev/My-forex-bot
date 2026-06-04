from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.clock import Clock
import random # صرف ڈیمو کے لیے

class ForexBot(App):
    def build(self):
        self.title = "Forex Auto Bot"
        self.running = False
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        # Title
        layout.add_widget(Label(text='FOREX AUTO TRADING BOT', font_size='20sp', size_hint_y=0.2))
        
        # Pair Select
        self.pair = Spinner(text='EURUSD', values=('XAUUSD', 'EURUSD', 'GBPUSD'), size_hint_y=0.15)
        layout.add_widget(self.pair)
        
        # Status
        self.status = Label(text='Status: Stopped', font_size='18sp', size_hint_y=0.2)
        layout.add_widget(self.status)
        
        # Start/Stop Button
        self.btn = Button(text='START BOT', size_hint_y=0.15, background_color=(0, 1, 0, 1))
        self.btn.bind(on_press=self.toggle_bot)
        layout.add_widget(self.btn)
        
        return layout

    def toggle_bot(self, instance):
        if not self.running:
            self.running = True
            self.status.text = 'Status: Running...'
            self.btn.text = 'STOP BOT'
            self.btn.background_color = (1, 0, 0, 1)
            # ہر 3 سیکنڈ بعد ٹریڈنگ چیک کرے گا
            Clock.schedule_interval(self.execute_trade, 3)
        else:
            self.running = False
            self.status.text = 'Status: Stopped'
            self.btn.text = 'START BOT'
            self.btn.background_color = (0, 1, 0, 1)
            Clock.unschedule(self.execute_trade)

    def execute_trade(self, dt):
        """
        یہاں آپ کی اصلی منطق (Strategy) آئے گی۔
        ابھی یہ صرف رینڈم ٹریڈ کر رہا ہے۔
        """
        if self.running:
            action = random.choice(['BUY', 'SELL'])
            self.status.text = f'Executing {action} on {self.pair.text}...'
            # یہاں آپ MT5 یا کسی بھی بروکر کی API کا کوڈ ڈالیں گے
            print(f"Trade Triggered: {action} on {self.pair.text}")

if __name__ == '__main__':
    ForexBot().run()
