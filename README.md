# goit-pythonweb-hw-04

Develop the script that takes all files from the source folder and copies them to the destination folder to a subfolder
files extension name.

## Variant 1:

Run the script with parameters (source_folder and destination_folder)

example:

```shell
python main.py ./source ./dest
```

## Varuant 2:

Run the script with no parameters

Then the script asks for the parameters:

- `Enter the source folder path:`
- `Enter the target folder path:`

Example:

```shell
python main.py
```

- `source`
- `dest`

After you run the script destination folder will have all the sorted files.

The script uses async operations IO that make process mach faster prior to sync ones.