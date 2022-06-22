#!/usr/bin/python3
def safe_print_division(a, b):
    ir = 0
    try:
        ir = (a / b)
    except Exception:
        ir = None
    finally:
        print("Inside result: {}".format(ir))
    return (ir)
