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
$ pdm install
$ pytest

# option
$ pdm venv create
```

## Setting up running environment
```bash
$ cat ~/.zshrc | tail -n 3

# MY_ENV
export MOVIE_API_KEY="<KEY>"

## Troubleshhoot
- [ ] 영화진흥위원회 로그인 후 키 생성
```
{'faultInfo': {'message': '유효하지 않은 키값입니다.', 'errorCode': '320010'}}
