# import asyncio
# import time
#
# async def async_func(num):
#     print(f'...start {num}')
#     await asyncio.sleep(3)
#     print(f'..end {num}')
#
# async def main():
#     taskA = asyncio.create_task(async_func('A'))
#     taskB = asyncio.create_task(async_func('B'))
#     taskC = asyncio.create_task(async_func('C'))
#
#     await asyncio.wait([taskA, taskB, taskC])
#
# if __name__ == '__main__':
#     asyncio.run(main())


# import asyncio
#
# async def count(counter):
#     print(f'Количество записей в списке {len(counter)}')
#     while True:
#         await asyncio.sleep(1/1000)
#         counter.append(1)
#         # print(len(counter))
#
# async def print_every_sec(counter):
#     while True:
#         await asyncio.sleep(1)
#         print(f'Прошла 1 секунда. Элементов в списке {len(counter)}')
#
# async def print_every_5sec():
#     while True:
#         await asyncio.sleep(5)
#         print(f'Прошло 5 секунд')
#
# async def print_every_10sec():
#     while True:
#         await asyncio.sleep(10)
#         print(f'Прошло 10 секунд')
#
# async def main():
#     counter = []
#     task1 = asyncio.create_task(count(counter))
#     task2 = asyncio.create_task(print_every_sec(counter))
#     task3 = asyncio.create_task(print_every_5sec())
#     task4 = asyncio.create_task(print_every_10sec())
#
#     task_list1 = [task1, task2, task3, task4]
#
#     await asyncio.wait([task1, task2, task3, task4])
#
#     # task_list = [count(counter), print_every_sec(counter), print_every_5sec(), print_every_10sec()]
#     # await asyncio.gather(*task_list)
#
# asyncio.run(main())

# import asyncio
# import time
#
# async def makeCoffee():
#     print('start makeCoffee')
#     await asyncio.sleep(3)
#     print('end makeCoffee')
#     return 'Coffee is ready'
#
# async def toastBrew():
#     print('start toastBrew')
#     await asyncio.sleep(2)
#     print('end toastBrew')
#     return 'Toast is ready'
#
# async def main():
#     start = time.time()
#     # work = asyncio.gather(makeCoffee(), toastBrew())
#     # res_coffee, res_toast = await work
#
#     task1 = asyncio.create_task(makeCoffee())
#     task2 = asyncio.create_task(toastBrew())
#
#     res_coffee = await task1
#     res_toast = await task2
#
#     end = time.time()
#     print(res_coffee)
#     print(res_toast)
#     print(f'Времени прошло {end-start:.2f} минут')
#
# if __name__ == '__main__':
#     asyncio.run(main())


# import asyncio
#
# async def my_sleep():
#     print('sleep start')
#     await asyncio.sleep(3)
#     print('sleep end')
#
# async def main():
#     print('rest start')
#     await my_sleep()
#     print('rest end')
#     await my_work()

# asyncio.run(main())


# import asyncio
# import httpx
#
# async def download(current):
#     url = f'https://www.thecocktaildb.com/api/json/v1/1/filter.php?c=Cocktail'
#
#     async with httpx.AsyncClient() as client:
#         result = await client.get(url)
#         if result.status_code == 200:
#             my_res = result.json()
#             print_info(my_res["drinks"],current)
#         else:
#             print(result.status_code)
#         print(f'Результат №{current}')
#
# def print_info(info,current):
#     # print(f"Имя: {info['first_name']}, Фамилия:{info['last_name']},E-mail:{info['email']}")
#     print(info[current]['strDrink'])
# async def main():
#     users_count = int(input('Сколько человек?  '))
#
#     current = 0
#     while current < users_count:
#         current += 1
#         task = asyncio.create_task(download(current))
#         await task
#     print('Done')
#
# asyncio.run(main())


# import asyncio
# import time
#
# async def summ(a,b):
#     await asyncio.sleep(1)
#     print(a+b)
# async def slow(a,b):
#     await asyncio.sleep(5)
#     print(a*b)
# async def main():
#     start = time.time()
#     task1 = asyncio.create_task(summ(12,2))
#     task2 = asyncio.create_task(slow(5,5))
#     await task1
#     await task2
#     end = time.time()
#     print(f'Времени прошло:{end - start:.2f} секунд')
#
#
# asyncio.run(main())


import asyncio
import time


async def call():
    print('Начался звонок....')
    await asyncio.sleep(5)
    print('Звонок закончился.')

async def prin_pos():
    print('Пришёл посетитель')
    await asyncio.sleep(2)
    print('Посетитель ушёл.')

async def grafiks():
    print('Начало работы с графиками')
    await asyncio.sleep(2)
    print('Работа с графиками завершена.')
async def aeroticket():
    print('Выбор авиабилетов')
    await asyncio.sleep(5)
    print('Авиабилет куплен.')
async def documents():
    print('Начало заполнения')
    await asyncio.sleep(3)
    print('Документы заполнены.')

async def main():
    print('9:00')
    await prin_pos()
    print('10:00')
    await asyncio.gather(aeroticket(),documents())
    print('11:00')
    await call()
    print('12:00')
    await grafiks()
    print('13:00')
    await asyncio.gather(aeroticket(),documents())

asyncio.run(main())
