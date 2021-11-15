# IMPORTATION STANDARD
import os

# IMPORTATION THIRDPARTY
import pytest

# IMPORTATION INTERNAL


@pytest.fixture
def default_csv_path(request, default_cassette_name):
    module = request.node.fspath
    path = os.path.join(
        module.dirname, "csv", module.purebasename, default_cassette_name
    )
    path_csv = path + ".csv"

    return path_csv
