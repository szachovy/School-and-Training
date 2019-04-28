import sys
import tempfile as tmp
import Wrongs
import Count

if __name__ == '__main__':
    if sys.argv[1]:
        print('Argument setted')
        if Wrongs.wrongType(sys.argv[1]) and Wrongs.wrongRange(sys.argv[1]):
            arg = int(sys.argv[1])
            getArg = Count.LookForNumbers()
            repr(getArg)

            calc = getArg.number(arg)
            getRes = Count.CalculateThis(calc)
            print(getRes.calculations())
            getRes.separate()

            with tmp.NamedTemporaryFile(delete=False) as t:
                t.write(b'getRes.separate()')
                path = t.name
                print(path)

            with open(path) as t:
                t.read()

            sys.exit(0)
        else:
            sys.exit(1)
    else:
        sys.exit(1)
