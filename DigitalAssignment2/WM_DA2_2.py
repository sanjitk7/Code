import scrapy

class ScrapeCamera(scrapy.Spider):
   #name of spider
   name = 'scrape_camera'

   #list of allowed domains
   allowed_domains = ['https://www.flipkart.com/search?q=cameras&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off']
   #starting url
   start_urls = ['https://www.flipkart.com/search?q=cameras&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off']
   #location of csv file
   custom_settings = {
       'FEED_URI' : '/Users/sanjitkumar/Documents/VIT_DOC/vit_semester_7/C2 - Web Mining/Lab/Lab2/FlipKartCameras.csv'
   }


   def parse(self, response):
       #Extract product information
       titles = response.css('.s1Q9rs)').extract()
       images = response.css('img::._396cs4._3exPp9').extract()
       prices = response.css('._30jeq3').extract()
       discounts = response.css('div::._3Ay6Sb').extract()


       for item in zip(titles,prices,images,discounts):
           scraped_info = {
               'title' : item[0],
               'price' : item[1],
               'image_urls' : [item[2]], #Set's the url for scrapy to download images
               'discount' : item[3]
           }

           yield scraped_info