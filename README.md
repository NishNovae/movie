# Movie

## Installation
```bash
# main
$ pip install git+https://github.com/NishNovae/movie.git

# branch
$ pip install git+https://github.com/NishNovae/movie.git@<BRANCH>
```

## Setting up dev environment
```bash
$ git clone <url>
$ cd <DIR>
$ source .venv/bin/activate
$ pytest

# option
$ pdm venv create
```

## Setting up running environment
```bash
$ cat ~/.zshrc | tail -n 3
export MOVIE_API_KEY="<KEY>"
