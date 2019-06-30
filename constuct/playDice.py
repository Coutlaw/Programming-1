from gamePieces import Die
def main():
    mitchDie = Die(6)
    tiffDie = Die(10)

    print("Mitch:", mitchDie.getFaceValue())
    print("Tiff:", tiffDie.getFaceValue())

    mitchDie.roll()
    tiffDie.roll()
    print()
    print("Mitch:", mitchDie.getFaceValue())
    print("Tiff:", tiffDie.getFaceValue())
    print()
    print("Mitch die:\n", mitchDie)
    print("Tiff die:\n", tiffDie)
    print("done")

main()
