sale_for_arena = int(input())

figurine = sale_for_arena - (sale_for_arena * 0.30)
kittering = figurine - (figurine * 0.15)
sound_system = 1 / 2 * kittering
price_all = sale_for_arena + figurine + kittering + sound_system

print(f'{price_all:.2f}')