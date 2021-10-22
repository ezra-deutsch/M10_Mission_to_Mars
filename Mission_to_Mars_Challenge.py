
#10.3.3 - Scrape Mars Data: The News
# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd



#10.3.3 - Set up executable path
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)




#10.3.3 - Set up URL and instruct the browser to visit the site
# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)



#10.3.3 - Set up HTML parser
html = browser.html
news_soup = soup(html, 'html.parser')
#Create variable "slide_elem" to narrow our search for article titles
slide_elem = news_soup.select_one('div.list_text')
slide_elem



#10.3.3
#use ".find" on the variable to parse out the individual class we need for the article title
slide_elem.find('div', class_='content_title')
# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title



#10.3.3
# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ###Featured Images

#10.3.4 - Scrape Mars Data: Featured Image - new website
# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)



#10.3.4 - Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()



#10.3.4 - Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')



#10.3.4 - Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel



#10.3.4 - Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


#10.3.5 - Scrape Mars Data: Mars Facts - new website
df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df



#10.3.5 - Transform the pandas df back into HTML
df.to_html()


# D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles
# Hemispheres

# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)



# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.

# Find the elements on each loop to avoid a stale element exception
for i in range(4):
    # Create empty dictionary
    hemispheres = {}
    browser.find_by_css("a.product-item h3")[i].click()
    element = browser.find_link_by_text('Sample').first
    img_url = element['href']
    title = browser.find_by_css('h2.title').text
    hemispheres['img_url'] = img_url
    hemispheres['title'] = title
    # Append hemisphere object to list
    hemisphere_image_urls.append(hemispheres)
    # Finally, we navigate backwards
    browser.back()
    


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls



# 5. Quit the browser
#10.3.5 - Quit browser
browser.quit()

