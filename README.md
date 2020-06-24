# Random Data Generator

This is a Python script to generate random Text, Image, and PDF files.
These files can be used for cases when large amounts of randomized data in common filetypes are needed.

Use case: Let's say you're s security engineer evaluating how easily mass compression or encryption can be detected in your environment. This script allows you to generate as many megabytes or gigabytes of data you need to do your evaluation. Using common file types such as this also provides a more realistic scenario of user data.

For a more detailed explanation of use cases like this: https://medium.com/@ntipun/security-use-cases-of-generating-random-files-9f17999963ee

## Installation

The generator.py file and the **files** folder should be in the same directory **and** must exist.
Pillow and Reportlab are needed for this and can be installed by the following commands:
```python
pip3 install pillow
pip3 install reportlab
```

## Future Improvements
1. .docx files
2. .xlsw files
3. Better multiprocessing for faster generation
4. Other filetypes?

## License
[MIT](https://choosealicense.com/licenses/mit/)
