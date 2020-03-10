# HImageCombiner
Horizontal Image Combiner written in python 3.7

# Dependencies
- pil

# How to use

1. Set input/output folder
- Both absolute/relative path allowed.
- When using relative path, don't forget the root is <path-to-HImageCombiner>

2. Set filename regex
- Regex string should contain two groups, and each should be named as <filenum> and <imagenum>.  
- For example, you can use  ```(?P<filenum>\d+)-(?P<imagenum>\d+)``` which indicates filenames like : <001-001>, <001-002>, <001-003> ...
- filenum and imagenum MUST BE number
  
# Control flow

1. Get all files in input folder.
2. Extract filenames that matches filename regex.
3. Sort filenum and imagenum by ascending order.
4. Combine images horizontally order by filenum.
