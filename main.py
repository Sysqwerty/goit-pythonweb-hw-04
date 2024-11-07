import asyncio
import aiofiles
from aiopath import AsyncPath
import logging
from argparse import ArgumentParser


async def read_folder(source_folder: AsyncPath, target_folder: AsyncPath):
    async for item in source_folder.iterdir():
        if await item.is_dir():
            await read_folder(item, target_folder)
        elif await item.is_file():
            await copy_file(item, target_folder)


async def copy_file(file_path: AsyncPath, target_folder: AsyncPath):
    ext = file_path.suffix.lstrip(".").lower()
    target_subfolder = target_folder / ext
    await target_subfolder.mkdir(parents=True, exist_ok=True)

    target_file_path = target_subfolder / file_path.name
    try:
        async with aiofiles.open(file_path, 'rb') as src_file, \
                aiofiles.open(target_file_path, 'wb') as dest_file:
            while chunk := await src_file.read(1024):
                await dest_file.write(chunk)
        logging.info(f"Copied: {file_path} -> {target_file_path}")
    except Exception as e:
        logging.error(f"Error copying {file_path} to {target_file_path}: {e}")


def setup_logging():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def get_folders_from_user():
    source = input("Enter the source folder path: ").strip()
    target = input("Enter the target folder path: ").strip()
    return source, target


async def main():
    parser = ArgumentParser(description="Async file copier by extension.")
    parser.add_argument('source', nargs='?', help="Source folder path")
    parser.add_argument('target', nargs='?', help="Target folder path")

    args = parser.parse_args()

    source_folder = args.source
    target_folder = args.target

    # If no arguments where passed -> ask user to provide them
    if not source_folder or not target_folder:
        source_folder, target_folder = get_folders_from_user()

    source_folder = AsyncPath(source_folder)
    target_folder = AsyncPath(target_folder)

    if not await source_folder.exists():
        logging.error(f"Source folder '{source_folder}' does not exist.")
        return

    await read_folder(source_folder, target_folder)


if __name__ == "__main__":
    setup_logging()
    asyncio.run(main())
