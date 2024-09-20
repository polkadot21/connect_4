# Connect 4 - Console Game

A two-player console version of Connect 4 built with Python. Players take turns dropping pieces into a 6x7 grid, aiming to connect four in a row, either horizontally, vertically, or diagonally.

## Features
- Two-player mode
- Auto-check for wins or tie
- Easy-to-extend board size via settings

## Requirements
- Python 3.x
- `pydantic`


## Setup

1. Clone the repository:

```bash
git clone https://github.com/your-username/connect-4.git
cd connect-4
```

2. Create a virtual environment:

```bash
python -m venv venv
```

3. Activate the virtual environment:

**On Mac or Linux**
```bash
source venv/bin/activate
```

**On Windows**
```bash
.\venv\Scripts\activate
```
   
4. Install requirements:

```bash
pip install -r requirements.txt
```

5. Define the board size

By default, a board of the size 6x7 is used. To adjust the board size, define the number of rows and columns in `.env`:

```bash
ROWS=<number of rows more than 4>
COLUMNS=<number of columns more than 4>
```

An example is provided in `.env.example`

5. Run the game

```bash
make run
```

6. Run tests:

```bash
make test
```

7. Lint and format:

```bash
make check
```