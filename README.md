# Music Library
This app allows you to search for albums and artists in a database of vinyl, CD and cassette powered by Discogs and save them in 
your local library. The app uses the Discogs API to fetch data from the database.

## Requirements
- Python 3.13
``` bash
pip install -r requirements.txt
```

## Configuration
Before running the application, you need to set up your environment variables:

1. Get your Discogs API token:
   - Go to [Discogs Settings](https://www.discogs.com/settings/developers)
   - Generate a personal access token

2. Set up your environment variables:
``` bash
DISCOGS_TOKEN=your_token_here
FLASK_ENV=development
```

## Docker
``` bash
docker compose up -d
```
## Usage
``` bash
python src/main.py
```

## Building
To build the package as a wheel distribution:

1. Install build dependencies:
``` bash
pip install build
```

2. Build the wheel:
``` bash
make all
```

The wheel file will be created in the `dist/` directory and can be distributed or installed with:
``` bash
pip install dist/music_library-X.X.X-py3-none-any.whl
```

## Credits
This app uses the [Discogs API](https://www.discogs.com/developers/) to fetch album and artist information.
All data retrieved is licensed under [CC0 1.0 Universal (Public Domain Dedication)](https://creativecommons.org/public-domain/cc0/).
Data provided by Discogs.
