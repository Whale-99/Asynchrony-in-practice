import asyncio


async def start_strongman(name, power):
    # Силач начинает соревнования
    print(f"Силач {name} начал соревнования.")

    # Для каждого шара (всего 5 шаров)
    for i in range(1, 6):
        # Поднимаем шар с задержкой пропорциональной мощности
        await asyncio.sleep(1 / power)
        print(f"Силач {name} поднял {i} шар")

    # Силач завершает соревнования
    print(f"Силач {name} закончил соревнования.")


async def start_tournament():
    # Создаем задачи для 3 силачей с разными мощностями
    strongman1 = asyncio.create_task(start_strongman('Pasha', 3))
    strongman2 = asyncio.create_task(start_strongman('Denis', 4))
    strongman3 = asyncio.create_task(start_strongman('Apollon', 5))

    # Ожидаем завершения всех задач
    await strongman1
    await strongman2
    await strongman3


# Запуск турнира
if __name__ == "__main__":
    asyncio.run(start_tournament())
