hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)
if h<40:
    print(h*rate)
elif h>40:
    overtimeHours = h - 40
    print((overtimeHours * r *1.5)+40*r)
