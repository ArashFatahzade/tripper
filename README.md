#  Tripper backend

### Instalation

```bash
v.activate
mkvirtualenv tripper
pip install -e .
```

#### Create DB
`tripper db create --drop --schema`

#### Basedata
`tripper db basedata`

#### Mockup
`tripper db mockup`

#### One liner setup
```tripper db create --drop --schema --basedata --mockup```

### Run tests and documnetion
```bash
pytest
```

Docs are avaliable on `data/markdown/` after running tests **successfuly**.

### Serve on http://localhost:8081
```bash
./gunicorn
```

