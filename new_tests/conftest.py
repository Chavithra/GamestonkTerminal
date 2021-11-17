# IMPORTATION STANDARD
import os

# IMPORTATION THIRDPARTY
import pytest

# IMPORTATION INTERNAL


@pytest.fixture
def default_csv_path(request):
    module = request.node.fspath
    path = os.path.join(
        module.dirname,
        "csv",
        module.purebasename,
        request.node.name,
    )
    path += ".csv"

    return path


@pytest.fixture
def default_txt_path(request):
    module = request.node.fspath
    path = os.path.join(
        module.dirname,
        "txt",
        module.purebasename,
        request.node.name,
    )
    path += ".txt"

    return path

@pytest.fixture
def default_json_path(request):
    module = request.node.fspath
    path = os.path.join(
        module.dirname,
        "json",
        module.purebasename,
        request.node.name,
    )
    path += ".json"

    return path
