require 'open-uri'
require 'nokogiri'


puts "Enter the search content"

word = gets
  link = "https://www.google.com/search?start=0&end=11&q='#{word}"
  page = Nokogiri::HTML(open(link))
page.xpath('//div/a/div[text()]').each do |search|

   puts search.content
    
end    
