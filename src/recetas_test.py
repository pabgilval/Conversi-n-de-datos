from recetas import *

def test_lee_recetas(recetas):
    print(f"Se han leído {len(recetas)} recetas.")
    print("Las tres primeras son:")
    print(recetas[:3])

def test_ingredientes_en_unidad(recetas, unidad):
    numero = ingredientes_en_unidad()

def main():
    recetas = lee_recetas('data/recetas.csv')
    #test_lee_recetas(recetas)
    test_ingredientes_en_unidad(None)
    test_ingredientes_en_unidad('gr')
    test_ingredientes_en_unidad('cl')

if __name__ == '__main__':
    main()