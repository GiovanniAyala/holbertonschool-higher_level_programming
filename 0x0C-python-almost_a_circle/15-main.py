#!/usr/bin/python3
""" 15-main """
from models.rectangle import Rectangle
from models.square import Square


if __name__ == "__main__":

    r1 = Square(10)
    r2 = Square(15)
    Square.save_to_file([r1, r2])

    with open("Square.json", "r") as file:
        print(file.read())

