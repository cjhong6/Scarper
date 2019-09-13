from scrapy.http import FormRequest
from scrapy.spiders import Spider

class FormSpider(Spider):
  name = 'horseForm'
  start_urls = ['https://treehouse-projects.github.io/horse-land/form.html']

  def parse(self, response):
    formdata = { 'firstname': 'CJ', 'lastname': 'Hong', 'jobtitle': 'GT Technician'}
    return FormRequest.from_response(response,formnumber=0,formdata=formdata,callback=self.after_post)

  def after_post(self,response):
    print('\n\n*************Form Processed.\n')
    print(response)