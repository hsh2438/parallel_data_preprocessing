# multiprocess based parallel data processing example
multiprocess based parallel data processing example

## text_preprocessing_parallel

    python text_preprocessing_parallel.py
    
After once data loading, multi process starts for preprocessing text data. <br>
If data file is big, loading data takes long time. <br>
Each process creates temp file to save preprocessed text data. <br>
If all process finish to preprocess, temp files are merged with subprocess (shell command). <br>
