#!/usr/bin/python3
from calculator_1.py import add,sub,div,mul
if __name__ == "__main__":
    a = 10
    b = 5
    print({:d} + {:d} = {:d}.formart(a, b, add(a, b)))
    print({:d} - {:d} = {:d}.formart(a, b, sub(a, b)))
    print({:d} * {:d} = {:d}.formart(a, b, mul(a, b)))
    print({:d} / {:d} = {:d}.formart(a, b, div(a, b)))
