# HImageCombiner
Horizontal Image Combiner written in python 3.7

# How to use

1. Set input/output folder
- Both absolute/relative path allowed.
- When using relative path, don't forget the root is <path-to-HImageCombiner>

2. Set filename regex
- regex should contain two groups, and each should be named as <filenum> and <imagenum>,
  
  for example,
  ```(?P<filenum>\d+)-(?P<imagenum>\d+)```
  indicates filenames like : <001-001>, <001-002>, <001-003> ...
  
# Control flow

1. Get all files in input folder.
2. Extract filenames that matches filename regex.
3. Sort filenum and imagenum by ascending order.
4. Combine images horizontally order by filenum.
