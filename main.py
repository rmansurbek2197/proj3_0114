ball = int(input("Imtihon balini kiriting (0–100): "))

if ball < 0 or ball > 100:
    print("Noto‘g‘ri ball")

elif ball < 50:
    print("Yiqildi")

elif ball < 65:
    print("Qoniqarsiz")

elif ball < 80:
    print("Qoniqarli")

elif ball < 90:
    print("Yaxshi")

else:
    print("A’lo")
