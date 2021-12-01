import scrapy

# class ShopcluesSpider(scrapy.Spider):
#    #name of spider
#    name = 'shopclues'

#    #list of allowed domains
#    allowed_domains = ['https://www.flipkart.com/']
#    #starting url
#    start_urls = ['https://www.flipkart.com/search?q=cameras&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off']
#    #location of csv file
#    custom_settings = {
#        'FEED_URI' : '/Users/sanjitkumar/Documents/VIT_DOC/vit_semester_7/C2 - Web Mining/Lab/Code/DigitalAssignment2/s2.csv'
#    }


#    def parse(self, response):
#        #Extract product information
#        titles = response.css('.ss1Q9rs::attr(title)').extract()
#        images = response.css('img::attr(data-img)').extract()
#        prices = response.css('._30jeq3::text').extract()
#        discounts = response.css('._3Ay6Sb::text').extract()


#        for item in zip(titles,prices,images,discounts):
#            scraped_info = {
#                'title' : item[0],
#                'price' : item[1],
#                'image_urls' : item[2], #Set's the url for scrapy to download images
#                'discount' : item[3]
#            }

#            yield scraped_info
           
class ShopcluesSpider(scrapy.Spider):
   #name of spider
   name = 'shopclues'

   #list of allowed domains
   allowed_domains = ['https://www.flipkart.com/search?q=cameras&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off']
   #starting url
   start_urls = ['https://www.flipkart.com/search?q=cameras&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off']
   #location of csv file
   custom_settings = {
       'FEED_URI' : '/Users/sanjitkumar/Documents/VIT_DOC/vit_semester_7/C2 - Web Mining/Lab/Code/DigitalAssignment2/s3.csv'
   }


   def parse(self, response):
       #Extract product information
       titles = response.css('a.ss1Q9rs::text').extract()
       images = response.css('img::attr(data-img)').extract()
       prices = response.css('div._30jeq3::text').extract()
       discounts = response.css('div._3Ay6Sb span::text').extract()


       for item in zip(titles,prices,images,discounts):
           scraped_info = {
               'title' : item[0],
               'price' : item[1],
               'image_urls' : item[2], #Set's the url for scrapy to download images
               'discount' : item[3]
           }

           yield scraped_info