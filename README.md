# MoroccanHousing-ETL
<img src="https://i.ibb.co/svCq2Jm/af4fb37b0a14d0a9dd9a7fd72451aaef-collage-450.jpg" alt="af4fb37b0a14d0a9dd9a7fd72451aaef-collage-450" border="0">
This project is a data pipeline built with scrapy spiders that crawl the famous housing moroccan website avito.ma , the pipeline extract data from the website and it's deployed on  Zyte (Scrapy cloud) and the data collected will be loaded to MongoDB on Digital ocean cloud

## Requirements
* Python >= 3.8
* Installing other requirements with the following command:
    ```sh
      pip install -r requirements.txt
    ```
## Usage

First you need to change the value of the variable **MONGO_URI** with your connection string of your MongoDB, Then you can simply run the spider :
```sh
      scrapy crawl avitoSpider
```
