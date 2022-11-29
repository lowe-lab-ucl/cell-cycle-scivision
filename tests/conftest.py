import pytest

from pathlib import Path


DATASET_KEYS = (
    "Interphase",
    "Prometaphase",
    "Metaphase",
    "Anaphase",
    "Apoptosis",
)

DATASET_SIZE = (2000, 80, 80, 1)


@pytest.fixture
def store_filepath() -> Path:
    return Path(__file__).parent.parent / "cell_cycle.zarr"


@pytest.fixture
def catalog_filepath() -> Path:
    return Path(__file__).parent.parent / ".scivision" / "data.yaml"


@pytest.fixture
def dataset_keys() -> tuple[str]:
    return DATASET_KEYS


@pytest.fixture
def dataset_size() -> tuple[int]:
    return DATASET_SIZE
