# MovieAdv - Movie Database Manager

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

A comprehensive Python application for managing your movie collection with a command-line interface.

---

## Features

### Core Functionality
- 🎬 **Add Movies** - Add new movies with validation for name, rating (1-10), and year (1896-current)
- 📜 **List Movies** - Display all movies in your collection
- ❌ **Delete Movies** - Remove movies by name
- ✏️ **Update Movies** - Modify existing movie entries
- 📊 **Statistics** - View detailed stats including average/median ratings and best/worst movies
- 🎲 **Random Movie** - Get a random movie recommendation
- 🔍 **Fuzzy Search** - Find movies using fuzzy matching (with `fuzzywuzzy`)
- ⭐ **Sorting** - Sort movies by rating or year (ascending or descending)
- 🪄 **Filtering** - Filter movies by min rate and release year.
- 📈 **Histogram** - Visualize rating distribution with Matplotlib

---

### Data Management
- 💾 **JSON Storage** - Persistent data storage in `movies.json`
- 🔄 **Automatic Loading/Saving** - Seamless data handling
- ✅ **Input Validation** - Comprehensive validation for all fields

---

## Installation

1. Clone the repository:
    ```bash
        git clone https://github.com/yourusername/movie_adv.git
        cd movie_adv
    ```
2. Create and activate a virtual environment:
    ```bash
        python -m venv .venv
        # On Windows:
        .venv\Scripts\activate
        # On macOS/Linux:
        source .venv/bin/activate
    ```
3. Install dependencies:
    ```bash
        pip install -r requirements.txt
    ```

---

## Usage

Run the application:
```bash
    python main.py
```
You'll see the interactive menu:
```text
******* My Movies Database *******
============== Menu =============
0.  Exit
1.  List movies
2.  Add movie
3.  Delete movie
4.  Update movie
5.  Stats
6.  Random movie
7.  Search movie
8.  Sort movies by rating and release year
9.  Filter movies by rating and release year
10. Create Rating Histogram
=================================
Select from the menu (1-10): 
=================================

```

---

## Code Structure

```bash

Movies/
├── core/
│   ├── __init__.py
│   ├── add_movie.py        # Add movies with validation
│   ├── delete_movie.py     # Remove movies
│   ├── update_movie.py     # Modify movies
│   ├── show_all_movies.py  # List all movies
│   ├── show_statistics.py  # Display stats
│   ├── random_movie.py     # Random recommendation
│   ├── search_movie.py     # Fuzzy search
│   ├── sort_movies.py      # Sort movies
│   ├── filter_movies.py    # Filter movies
│   └── build_histogram.py  # Rating visualization
├── data/
│   └── movies.json         # Movie database
├── data_managers/
│   └── load_json.py        # JSON read/write operations
├── utils/
│   ├── text_utils.py       # Text formatting
│   └── validators.py       # Input validation
├── main.py                 # Entry point
├── README.md               # This file
└── requirements.txt        # Dependencies

```

---

## Dependencies

- Python 3.8+
- fuzzywuzzy (for search functionality)
- matplotlib (for histogram visualization)
- python-Levenshtein (for faster fuzzy matching)

Add to requirements.txt:

```bash
  fuzzywuzzy>=0.18.0
  matplotlib>=3.5.0
  numpy>=2.2.5
  python-Levenshtein>=0.12.2
```

---

## Contributing

1. Fork the repository
2. Create a new branch (git checkout -b feature)
3. Commit your changes (git commit -am 'Add new feature')
4. Push to the branch (git push origin feature)
5. Create a new Pull Request

---

### License

MIT License - see LICENSE file for details

```text

This README includes:
1. Clear feature descriptions
2. Installation instructions
3. Usage examples
4. Code structure explanation
5. Dependency information
6. Contribution guidelines
7. License information

The document is formatted with proper Markdown syntax and includes badges for Python version and license. You can customize the repository URL, license file, and other details as needed.

Would you like me to add any additional sections or modify any existing ones?
```