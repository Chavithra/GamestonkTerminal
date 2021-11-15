import yaml
import gzip
from io import StringIO, BytesIO


def read_yaml(path: str):
    with open(path) as file:
        content = yaml.load(file, Loader=yaml.CLoader)

    return content


def decompress(content: str) -> str:
    stio = BytesIO(content)
    gzip_file = gzip.GzipFile(fileobj=stio)
    return gzip_file.read()


def read_interaction(path: str, index: int):
    content = read_yaml(path=path)
    response = content["interactions"][0]["response"]
    body = response["body"]["string"]
    # headers = response["headers"]
    # status = response["status"]
    return decompress(body)


path = "tests/cassettes/test_fa/test_fa_market/test_income.yaml"
body = read_interaction(path=path, index=0)

print(body)
