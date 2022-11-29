import intake
import pytest
import xarray
import zarr


def test_load_dataset_zarr(store_filepath, dataset_keys, dataset_size):
    """Test loading the dataset using ``zarr``."""
    loader = zarr.open(store_filepath)
    zarr_keys = list(loader.keys())

    # check that all of the default keys ar present
    for key in dataset_keys:
        assert key in zarr_keys, zarr_keys

    # check that the images are the correct size
    for group in zarr_keys:
        assert loader[group].shape == dataset_size


def test_load_dataset_intake(catalog_filepath, dataset_keys, dataset_size):
    """Test loading the dataset using ``intake``."""
    catalog = intake.open_catalog(catalog_filepath)
    dataset = catalog.cell_cycle.to_dask()

    assert isinstance(dataset, xarray.core.dataset.Dataset)

    # check that all of the groups are present and the data is the correct size
    for key in dataset_keys:
        x = getattr(dataset, key)
        assert isinstance(x, xarray.core.dataarray.DataArray)
        assert x.shape == dataset_size
