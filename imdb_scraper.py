# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 19:36:54 2023

@author: Abhay
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

# Opening the URL in Chrome
driver = webdriver.Chrome()
new_url = "https://www.imdb.com/event/ev0000003/2017/1/?ref_=fea_eds_top-1_2"  # Starting URL

new_year_range = range(2017, 2018)  # Years from 2017 to 2023

def get_inner_text(search_text):
    element = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.XPATH, f"//div[@class='event-widgets__award-category-name' and text()='{search_text}']//following-sibling::div[@class='event-widgets__award-category-nominations']"))
    ).get_attribute('innerText')
    return element

# Navigate to the starting URL
driver.get(new_url)
data = []

for year in new_year_range:
    # Get information for the current page
    best_motion_pic = get_inner_text("Best Motion Picture of the Year")
    best_original_scrnplay = get_inner_text("Best Original Screenplay")
    best_adpted_scrnplay = get_inner_text("Best Adapted Screenplay")
    best_achievemnt_cinema = get_inner_text("Best Achievement in Cinematography")
    best_achievemnt_flm_edt = get_inner_text("Best Achievement in Film Editing")
    best_achievemnt_prod_des = get_inner_text("Best Achievement in Production Design")
    best_costume_des = get_inner_text("Best Achievement in Costume Design")
    best_facial_stuff = get_inner_text("Best Achievement in Makeup and Hairstyling")
    best_original_score = get_inner_text("Best Achievement in Music Written for Motion Pictures (Original Score)")
    best_original_song = get_inner_text("Best Achievement in Music Written for Motion Pictures (Original Song)")
    best_viz_effect = get_inner_text("Best Achievement in Visual Effects")

    award_data = {
        "Year": year,
        "Best Motion Picture of the Year": best_motion_pic,
        "Best Original Screenplay": best_original_scrnplay,
        "Best Adapted Screenplay": best_adpted_scrnplay,
        "Best Achievement in Cinematography": best_achievemnt_cinema,
        "Best Achievement in Film Editing": best_achievemnt_flm_edt,
        "Best Achievement in Production Design": best_achievemnt_prod_des,
        "Best Achievement in Costume Design": best_costume_des,
        "Best Achievement in Makeup and Hairstyling": best_facial_stuff,
        "Best Achievement in Music Written for Motion Pictures (Original Score)": best_original_score,
        "Best Achievement in Music Written for Motion Pictures (Original Song)": best_original_song,
        "Best Achievement in Visual Effects": best_viz_effect
    }

    data.append(award_data)
    # Go to the next year's page
    driver.get(f"https://www.imdb.com/event/ev0000003/{year+1}/1/?ref_=fea_eds_top-1_2")

# Close the browser
driver.quit()

df = pd.DataFrame(data)
df.to_csv('new_imdb_scraper.csv', index=False)
