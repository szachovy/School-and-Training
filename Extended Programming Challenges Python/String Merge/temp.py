"""
async def stringyield(string1):
    for it in string1:
        yield it

loop = asyncio.get_event_loop()

loop.run_until_complete(stringyield(string1))
loop.run_until_complete(stringyield(string2))

print(next(iterere(string)))

print(finalstr)
print(getRes(finalstr, long))
"""
