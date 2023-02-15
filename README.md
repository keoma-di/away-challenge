# Finish list: (total cost: 170 minutes)
[x] The requirement needs a program to crawl data of a page then collect data and generate an image of a graph plot

[x] Using a package to crawl data and library to generate an image of a graph plot

[x] After research in 30 minute then I found two strong packages [Python Scrapy](https://docs.scrapy.org/en/latest/) and library [matplotlib](https://matplotlib.org/stable/index.html) this support to many thing and easy to implement and support so much feature if we need to extend

[x] Code and debug - 120 minutes

[x] Write documentation - 20 minutes

# Todo list
## Code
- Support attribute columns when run command. These columns will using to generate vertical and horizontal axis
- Validate input argument(url, column)
- Write Unit Test

## Testing
### Test Pass checklist
- Give a correct URL with 1 table inside the page
  - Get a response from spider
  - Make sure data from the table is included in raw WikiTableItem
  - Generate an image of a graph plot
- Give a correct URL with 2 tables inside page
  - Get a response from spider
  - Make sure data from the table is included in raw WikiTableItem
  - Generate two images of the graph plot

### Test Failed checklist
- Give incorrect URL
  - Give error message validate URL and stop
  - No response from
  - No image to generate


# Setup project
## Prerequisite: Python 3.9

## Install package
You could use virtual environment for setup [ref](https://docs.python.org/3/library/venv.html)
```
pip install -r req.txt
```

## Run project 
You need to run this comment in the root folder then you could see the image with name is ```wiki-table.png```
```
scrapy crawl wiki-table -a url=https://en.wikipedia.org/wiki/Women%27s_high_jump_world_record_progression
```
