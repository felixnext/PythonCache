from datetime import datetime
from glob import glob
import os
import shutil
import time
import unittest

import pandas as pd

import pycache


class TestPandasCache(unittest.TestCase):
    def setUp(self) -> None:
        '''Setup the folder'''
        self.cache_folder = "./cache"

    def test_cache_init(self):
        # create the cache and check if folder exists
        cache = pycache.PandasFileCache(self.cache_folder)
        self.assertTrue(os.path.isdir(self.cache_folder), "Expecting cache folder to exist")

    def test_cache_write(self):
        # create the cache
        cache = pycache.PandasFileCache(self.cache_folder)

        # insert data
        df = pd.DataFrame([[1, 2, 3], [3, 4, 5]], columns=["A", "B", "C"])
        cache["test"] = df

        # make sure data exists
        files = glob(os.path.join(self.cache_folder, "**", "*.csv"))
        self.assertEqual(len(files), 1, f"Expected to find one folder, but got: {files}")

    def test_cache_write_read(self):
        # create the cache
        cache = pycache.PandasFileCache(self.cache_folder)

        # insert data
        df = pd.DataFrame([[1, 2, 3], [3, 4, 5]], columns=["A", "B", "C"])
        cache["test"] = df
        df_load = cache["test"]

        pd.testing.assert_frame_equal(df, df_load)

    def test_cache_write_read_write(self):
        # create the cache
        cache = pycache.PandasFileCache(self.cache_folder)

        # insert data
        df1 = pd.DataFrame([[1, 2, 3], [3, 4, 5]], columns=["A", "B", "C"])
        cache["test"] = df1
        df_load1 = cache["test"]
        df2 = pd.DataFrame([[4, 6, 7], [10, 9, 8]], columns=["A", "B", "C"])
        cache["test"] = df2
        df_load2 = cache["test"]

        # make sure data is equal
        pd.testing.assert_frame_equal(df1, df_load1)
        pd.testing.assert_frame_equal(df2, df_load2)

    def test_cache_history(self):
        # create the cache
        cache = pycache.PandasFileCache(self.cache_folder, keep_history=True, outdated_interval=5)

        # insert first data
        time1 = datetime.now()
        df1 = pd.DataFrame([[1, 2, 3], [3, 4, 5]], columns=["A", "B", "C"])
        cache["test"] = df1

        # wait
        time.sleep(10)

        # insert second data
        time2 = datetime.now()
        df2 = pd.DataFrame([[4, 6, 7], [10, 9, 8]], columns=["A", "B", "C"])
        cache["test"] = df2

        # load both datasets
        df_load1, _ = cache.get("test", time1)
        df_load2, _ = cache.get("test", time2)

        # make sure data is equal
        pd.testing.assert_frame_equal(df1, df_load1)
        pd.testing.assert_frame_equal(df2, df_load2)

    def tearDown(self) -> None:
        '''Make sure cache is deleted'''
        shutil.rmtree(self.cache_folder, ignore_errors=True)


if __name__ == '__main__':
    unittest.main()
