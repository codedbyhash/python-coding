# Python Coding Practice

My Python learning record: concept examples, programming exercises, and small experiments.

## Topic index

| Topic | Folder |
|---|---|
| Basics | [basics](content/basics/) |
| Data types, strings, tuples and dictionaries | [data_types](content/data_types/) |
| Lists and comprehensions | [lists](content/lists/) |
| Conditions, loops and exercises | [loops](content/loops/) |
| Functions | [functions](content/functions/) |
| Custom modules | [modules](content/modules/) |
| Python standard library | [standard_library](content/standard_library/) |
| Exception handling | [exception_handling](content/exception_handling/) |
| Classes and objects | [oop](content/oop/) |
| Scientific Python | [data_science](content/data_science/) |

## Learning checklist

Check a topic when I can explain it and solve fresh exercises independently.
Existing examples show practice, rather than confirmed mastery.

- [ ] Python basics and data types
- [ ] Strings, lists, tuples, sets and dictionaries
- [ ] Conditions and loops
- [ ] Functions and modules
- [ ] Standard library
- [ ] Exception handling
- [ ] Object-oriented programming
- [ ] File handling
- [ ] Data structures and algorithms
- [ ] Scientific Python and data analysis
- [ ] Mini projects

## Run an example

From the repository folder, using Python 3:

```bash
python3 content/basics/hello.py
python3 content/modules/app.py
```

Some exercises ask for input. Run each script individually.
The line case conversion exercise is unfinished and currently keeps requesting input; stop it with Ctrl+C.

For the scientific Python example, create an environment and install dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 content/data_science/scipy_interpolation.py
```

## Daily workflow

1. Save new examples in the matching topic folder.
2. Use lowercase filenames with underscores and descriptive exercise names.
3. Record progress with a meaningful commit:

```bash
git add .
git commit -m "Practise Python list comprehensions"
git push
```

Before starting work, pull updates made on GitHub into the local checkout.
