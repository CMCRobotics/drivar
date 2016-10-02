# Build with Apache maven 3.0.5+

```
mvn package
```

# Deploy with pip

```
cd target/py
python setup.py register -r pypi
python setup.py sdist upload -r pypi
```
