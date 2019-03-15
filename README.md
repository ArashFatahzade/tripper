#  Tripper backend

### Instalation

```bash
v.activate
mkvirtualenv tripper
pip install -e .
```

### Run tests and documnetion
```bash
pytest
```

Docs are avaliable on `data/markdown/` after running test **successfuly**.

### Serve on http://localhost:8081
```bash
./gunicorn
```

