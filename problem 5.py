import Scuba from Scuba

def transfer_air(source, target, amount):
    old_pressure = source.get_bar()

    source.release(amount)

    if source.get_bar() == old_pressure - amount:
        target.fill(amount)

src = ScubaTank(" A ", 150)
dst = ScubaTank(" B ", 20)

transfer_air(src, dst, 50)
print(src)
print(dst)

transfer_air(src, dst, 120)
print(src.get_bar())
print(dst.get_bar())