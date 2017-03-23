

try:
    print('To jest blok try')
    raise ValueError

#except Exception:
 #   print('Złapałem wyjątek')

except ValueError as blad:
    print('test', blad.with_traceback())
finally:
    print('To jest blok finally')