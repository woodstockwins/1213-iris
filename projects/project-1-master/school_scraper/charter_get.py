import pandas as pd
from selenium import webdriver

# data scraped from: https://www.cde.ca.gov/ds/si/cs/ap1/imagemap.aspx
url = "https://www.cde.ca.gov/ds/si/cs/ap1/countyresults.aspx?id="

url_ids = [str(x) for x in range(1, 60)]
url_ids[0:9] = ["0" + x for x in url_ids[0:9]]

output = pd.DataFrame()

driver_path = "/Users/genebob/Dropbox/LoL Python v1.0/v2/LoL_Scrape_Bot_v2/chromedriver/chromedriver"
driver = webdriver.Chrome(driver_path)

for u in url_ids:
    try_url = url + u

    try:
        print(try_url)

        driver.get(try_url)

        # Code adapted from user: "SIM" on StackOverflow (source: https://stackoverflow.com/a/52448691)
        scrape_table = driver.find_element_by_xpath('//*[@id="ctl00_CPH_gvCharSch"]')
        for table in driver.find_elements_by_xpath('/html/body/div/div[3]/div/form/div[3]/div[2]/div/table/tbody'):
            data = [item.text for item in table.find_elements_by_xpath(".//*[self::td or self::th]")]
        # end adaptation

        # Get County Name:
        county_name = driver.find_element_by_xpath('//*[@id="ctl00_CPH_lblCountyName"]').text

        county_name = " ".join(county_name.split()[:-3])

        school_name = []
        charter_number = []
        site_type = []
        more_details = []
        statistical_info = []

        for i in range(0, len(data), 5):
            school_name.append(data[i])
            charter_number.append(data[(i+1)])
            site_type.append(data[(i+2)])
            more_details.append(data[(i+3)])
            statistical_info.append(data[(i+4)])

        df_charter = pd.DataFrame(
            {school_name[0].lower(): school_name[1:], charter_number[0].lower(): charter_number[1:],
             site_type[0].lower(): site_type[1:], more_details[0].lower(): more_details[1:],
             statistical_info[0].lower(): statistical_info[1:], "county": county_name}
        )

        output = pd.concat([output, df_charter], ignore_index=True, axis=0)

    except Exception as e:
        print(f"{try_url} does not exist. Trying next url id")

driver.quit()

output.to_csv("charter.csv")

