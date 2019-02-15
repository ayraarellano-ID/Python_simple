import gzip
import shutil
with open('test_txt.txt', 'rb') as f_in, gzip.open('test_txt.txt.gz', 'wb') as f_out:
    shutil.copyfileobj(f_in, f_out)