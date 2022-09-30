from deep_translator import GoogleTranslator
from tqdm import tqdm
import json
import asyncio


translator = GoogleTranslator(target='ru')


async def translate(work_queue: asyncio.Queue) -> str:
    while not work_queue.empty():
        return translator.translate(await work_queue.get())


async def main():
    translator.target = input("Enter the target language translation (must consist of the first two characters of the language, example: 'ru', 'en'). If not specified, the language used is Russian (ru): ") or 'ru'
    work_queue = asyncio.Queue()
    dict_output = dict()

    with open("output.json", 'w', encoding='utf-8') as output:
        with open("input.json", encoding='utf-8') as source:
            source: dict = json.load(source)
            for string in source.values():
                await work_queue.put(string)
            with tqdm(range(len(source))) as pbar:
                for key in source:
                    dict_output[key] = (await asyncio.gather(
                        asyncio.create_task(translate(work_queue))
                    ))[0]
                    pbar.update(1)
                json.dump(dict_output, output, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    asyncio.run(main())
