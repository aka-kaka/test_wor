import asyncio
from sys import stdin
from hashlib import sha256
from random import randrange


async def prtn(string):
    """ожидание от 1 до 5 сек перед выводом"""
    await asyncio.sleep(randrange(1,5))
    return string


async def corut(c):
    """ запуск корутин """
    result=[]
    if type(c) in (tuple, list, set):
        tasks=[prtn(i) for i in c]
    elif type(c) in (str, int):
        tasks=prtn(c)
    elif type(c) == dict:
        tasks=[prtn(i) for i in c.values()]
    else:
        return None

    for task in asyncio.as_completed(tasks):
        result.append(await task)
    return(result)


def get_hash(string):
    """ получение хэша """
    if type(string) in (str, int):    
        string=str(string).strip("\n")
        string=string.encode()
        return sha256(string).hexdigest()
    else:
        return None


def main (cor):
    """
    подготовка петли 
    возвращает список
    """
    loop=asyncio.get_event_loop()
    rsp=loop.run_until_complete(corut(cor))
    return rsp
    

if __name__=="__main__":

    rsp=main([input(i) for i in ('Имя: ', 'Должность: ', 'Зарплата: ')])
    print('получено от асинхронной функции', rsp)

    for i in rsp:
        print(f'{i} hash({get_hash(i)})')
    
    print(get_hash(stdin.readline()))
