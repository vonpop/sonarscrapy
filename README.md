# sonarscrapy
Use scrapy to get metrics from sonarqube.
Scrapy docs: scrapy.org

# Setup

## Create Python3 Environment (Optional) 

` $> python3 -m venv venv

## Activate environment (Optional) 
` $> source venv/bin/activate

## Install dependencies
pip install -r requirements.txt

## Configure 

Change sonar/spiders/projects.py to

* config URL/IP of your sonarqube instance
* set your access token

# Run

` $> scrapy crawl projects -O projects.json

Creates projects.json.




