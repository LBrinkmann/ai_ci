import torch as th
import pandas as pd
import numpy as np
import os
from aci.utils.store import load
from aci.utils.io import get_subfiles


def compare_folder(folder, ref_folder):
    paths = get_subfiles(folder)
    ref_paths = get_subfiles(ref_folder)
    if set(paths) != set(ref_paths):
        raise ValueError(f"File names do not match: {paths} and {ref_paths}")
    for p in paths:
        path = os.path.join(folder, p)
        ref_path = os.path.join(ref_folder, p)
        if os.path.isdir(path):
            assert os.path.isdir(ref_path), f'{path} is folder, but {ref_path} not.'
            compare_folder(path, ref_path)
        else:
            assert not os.path.isdir(ref_path), f'{path} is file, but {ref_path} not.'
            compare_files(path, ref_path)


def compare_files(path, ref_path):
    obj = load(path)
    ref = load(ref_path)
    try:
        compare(obj, ref)
    except Exception as e:
        print(e)
        raise ValueError(f'Mismatch in file {path}.')


def compare(obj, ref):
    # check if both are of same type
    if type(obj) != type(ref):
        raise ValueError(f"Types mismatch: {type(obj)} {type(ref)}")
    if isinstance(obj, list):
        compare_list(obj, ref)
    elif isinstance(obj, dict):
        compare_dict(obj, ref)
    elif isinstance(obj, pd.DataFrame):
        compare_df(obj, ref)
    elif isinstance(obj, th.Tensor):
        compare_torch(obj, ref)
    elif isinstance(obj, np.ndarray):
        compare_np(obj, ref)
    else:
        compare_other(obj, ref)


def compare_other(obj, ref):
    try:
        assert (obj == ref), f'Mismatch between {obj} and {ref}'
    except Exception as e:
        print(e)
        raise ValueError(f'Error comparing {obj} and {ref}')


def compare_list(obj, ref):
    assert len(obj) == len(ref), 'Length of list mismatch'
    for i, (o, r) in enumerate(zip(obj, ref)):
        try:
            compare(o, r)
        except Exception as e:
            print(e)
            raise ValueError(f'Mismatch in list element {i}.')


def compare_dict(obj, ref):
    all_keys = set(obj.keys()).union(set(ref.keys()))
    for k in all_keys:
        assert k in obj, f'{k} missing in object, keys: {obj.keys()}'
        assert k in ref, f'{k} missing in reference, keys: {ref.keys()}'
        try:
            compare(obj[k], ref[k])
        except Exception as e:
            print(e)
            raise ValueError(f'Mismatch in dict values of key {k}.')


def compare_torch(obj, ref):
    assert (obj == ref).all(), 'torch tensors mismatch'


def compare_df(obj, ref):
    try:
        assert obj.equals(ref), 'pandas dataframe mismatch'
    except Exception as e:
        try:
            col_mismatch = (obj != ref).any()
            row_mismatch = (obj.loc[:, col_mismatch] != ref.loc[:, col_mismatch]).any(1)
            print(obj[row_mismatch].loc[:, col_mismatch])
            print(ref[row_mismatch].loc[:, col_mismatch])
        except:
            print(obj)
            print(ref)
        raise e


def compare_np(obj, ref):
    try:
        assert (obj == ref).all().all(), 'numpy array mismatch'
    except Exception as e:
        print(f'Similarity: {sim:.1%}')
        col_mismatch = (obj != ref).any()
        row_mismatch = (obj[:, col_mismatch] != ref[:, col_mismatch]).any(1)
        print(obj[row_mismatch][:, col_mismatch])
        print(ref[row_mismatch][:, col_mismatch])
        raise e
