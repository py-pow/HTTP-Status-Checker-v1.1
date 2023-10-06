
![Logo](https://user-images.githubusercontent.com/120333416/273262997-641e322f-16f5-4857-874c-abd81812394b.png)

    


HTTP Status Checker v1.1  Code checking tool open to development written in Python programming language.



## Innovations:

- Some bugs have been fixed.
- Added extra error trap except.
- It is enabled to continue scanning in case of any error.
- Added the -s/--status argument to scan and save only the desired HTTP Status Code.

  
## Installation 

To installation the used libraries.

```python 
$  pip install -r requirements.txt

```
    
## Usage

```python
$ python3 main.py --list sites.txt 
$ python3 main.py --list sites.txt  --output websites.txt
$ python3 main.py --list sites.txt --status 200,404,503 --output websites.txt (default : output.txt)
```

  
## Screenshots

![Tool Screenshot](https://user-images.githubusercontent.com/120333416/273262981-2569bf73-8e1a-4c84-9f9e-b23c5ef022ff.png)

![Tool Screenshot](https://user-images.githubusercontent.com/120333416/273263001-dfec3a81-7b1f-4d65-bcee-1d071490dce1.png)
  
## Demo Video

[![asciicast](https://asciinema.org/a/9hoFh4gdq1xbhswiNRbvDl62U.svg)](https://asciinema.org/a/9hoFh4gdq1xbhswiNRbvDl62U)

  
