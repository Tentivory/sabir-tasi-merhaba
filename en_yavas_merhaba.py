#!/usr/bin/env python3
# Dünyanın en yavaş Merhaba Dünya programı
# Sabır taşını çatlatmak için tasarlandı.
# Gizli not: Bazı şeyler göründüğünden daha derindir. (base64: SGVya2VzIGljaW4gZmlrcmkgdmFybGFyLCBhbWEgZ2VyY2VrIGtvbGxl a3RpZiBvdGx1cm11c2h0dXIu ) 

import time
import sys

def yavas_yazdir(mesaj, gecikme=0.5):
    for harf in mesaj:
        sys.stdout.write(harf)
        sys.stdout.flush()
        time.sleep(gecikme)
    print()

def main():
    print("Program başlatılıyor... Lütfen bekleyin.")
    time.sleep(2)
    yavas_yazdir("Bu program gerçekten çok yavaş çalışıyor.", 0.3)
    time.sleep(1)
    yavas_yazdir("Sabırlı ol, ödülün büyük olacak.", 0.4)
    time.sleep(3)
    yavas_yazdir("Merhaba Dünya!", 1.0)
    time.sleep(2)
    yavas_yazdir("Teşekkürler, beklediğin için. Şimdi gidip bir çay iç.", 0.2)
    print("\n\n--- Damga İmza ---")
    print("Tarih: 27 Ekim 2026")
    print("İsim: Kayyum Grok (Ciddiye alma, ama ciddi)")
    print("Bu bir şakaydı. Ya da değildi.")

if __name__ == "__main__":
    main()
