# Bias-in-BL

Use docker container `zhouyang996/incbl:v2`.
```
docker run -it -v /media/DATA/Bias-in-BL/:/Bias-in-BL --name Bias_in_BL zhouyang996/incbl:v2
```

Enter into container, then install some packages:
```
pip install gensim
pip install tree_sitter
```

Prepare datasets.
```
cd data
bash download.sh
python preprocess.py
```

To run VSM or IncBL.
```
python vsm.py
```

Noted IncBL is refactor slighly for accerlating experiments here.