# Scrapy commands & code

> This goes with the [Traversy Media Scrapy tutorial on YouTube](https://youtu.be/ALizgnSFTwQ)

[Download Kite](https://kite.com/download/?utm_medium=referral&utm_source=youtube&utm_campaign=TechGuyWeb&utm_content=scrapy-tutorial)

## Setup

```
pip install scrapy
```

```
scrapy startproject postscrape
cd postscrape
```

- Create spiders/posts_spider.py

```
scrapy crawl posts
```

## Working in the shell with selectors
```
scrapy shell https://blog.scrapinghub.com/
```

```
response.css('title')
response.css('title').get()
response.css('title::text').get()

response.css('h3::text').get()
response.css('h3::text')[1].get()
response.css('h3::text').getall()

response.css('.post-header').get()
response.css('.post-header a').get()

response.css('p::text').re(r'scraping')
response.css('p::text').re(r's\w+')
response.css('p::text').re(r'(\w+) you (\w+)')

response.xpath('//h3')
response.xpath('//h3/text()').extract()
response.xpath('//*[@id="hs_cos_wrapper_module_1523032069834331"]/div/div/div/div/div[1]/div[2]/div[2]/div/span[2]/a/text()').getall()
```

```
post = response.css('div.post-item')[0]
title = post.css('.post-header h2 a::text')[0].get()
date = post.css('.post-header a::text')[1].get() 
author = post.css('.post-header a::text')[2].get() 

for post in response.css('div.post-item'):
	title = post.css('.post-header h2 a::text')[0].get()
	date = post.css('.post-header a::text')[1].get() 
	author = post.css('.post-header a::text')[2].get() 
	print(dict(title=title, date=date, author=author))

```
## Script
```
import scrapy


class PostsSpider(scrapy.Spider):
    name = "posts"

    start_urls = [
        'https://blog.scrapinghub.com/'
    ]

    def parse(self, response):
        for post in response.css('div.post-item'):
            yield {
                'title': post.css('.post-header h2 a::text')[0].get(),
                'date': post.css('.post-header a::text')[1].get(),
                'author': post.css('.post-header a::text')[2].get()
            }
        next_page = response.css('a.next-posts-link::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
```
