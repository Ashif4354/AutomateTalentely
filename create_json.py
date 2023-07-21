import json

data = {
    'Number System' : '//*[@id="main-content"]/div/div[2]/div[3]/div[1]/div/div[3]/a',
    'HCF & LCM' : '//*[@id="main-content"]/div/div[2]/div[3]/div[2]/div/div[3]/a',
    'Percentage' : '//*[@id="main-content"]/div/div[2]/div[3]/div[3]/div/div[3]/a',
    'profit & Loss' : '//*[@id="main-content"]/div/div[2]/div[3]/div[4]/div/div[3]/a',
    'Simple Interest & Compound Interest' : '//*[@id="main-content"]/div/div[2]/div[3]/div[5]/div/div[3]/a',
    'Time & Work' : '//*[@id="main-content"]/div/div[2]/div[3]/div[6]/div/div[3]/a',
    'Pipes and Cisterns' : '//*[@id="main-content"]/div/div[2]/div[3]/div[7]/div/div[3]/a',
    'Time Speed Distance' : '//*[@id="main-content"]/div/div[2]/div[3]/div[8]/div/div[3]/a',
    'Problems On Trains' : '//*[@id="main-content"]/div/div[2]/div[3]/div[9]/div/div[3]/a',
    'Boats and Stream' : '//*[@id="main-content"]/div/div[2]/div[3]/div[10]/div/div[3]/a',
    'Averages' : '//*[@id="main-content"]/div/div[2]/div[3]/div[11]/div/div[3]/a',
    'Permutation and Combination' : '//*[@id="main-content"]/div/div[2]/div[3]/div[12]/div/div[3]/a',
    'Probability' : '//*[@id="main-content"]/div/div[2]/div[3]/div[13]/div/div[3]/a',
    'Logarithm' : '//*[@id="main-content"]/div/div[2]/div[3]/div[14]/div/div[3]/a',
    'Problems On Ages' : '//*[@id="main-content"]/div/div[2]/div[3]/div[15]/div/div[3]/a',
    'Partnership' : '//*[@id="main-content"]/div/div[2]/div[3]/div[16]/div/div[3]/a',
    'Algebra' : '//*[@id="main-content"]/div/div[2]/div[3]/div[17]/div/div[3]/a',
    'Clocks' : '//*[@id="main-content"]/div/div[2]/div[3]/div[18]/div/div[3]/a',
    'Calendar' : '//*[@id="main-content"]/div/div[2]/div[3]/div[19]/div/div[3]/a',
    'Height and Distance' : '//*[@id="main-content"]/div/div[2]/div[3]/div[20]/div/div[3]/a',
    'Surds and Indices' : '//*[@id="main-content"]/div/div[2]/div[3]/div[21]/div/div[3]/a',
    'Races and Games' : '//*[@id="main-content"]/div/div[2]/div[3]/div[22]/div/div[3]/a',
    'Chain Rule' : '//*[@id="main-content"]/div/div[2]/div[3]/div[23]/div/div[3]/a',
    'Sequence and Series' : '//*[@id="main-content"]/div/div[2]/div[3]/div[24]/div/div[3]/a',
    'Trigonometry' : '//*[@id="main-content"]/div/div[2]/div[3]/div[25]/div/div[3]/a',
    'Mixture and Alligation' : '//*[@id="main-content"]/div/div[2]/div[3]/div[26]/div/div[3]/a',
    'Mensuration' : '//*[@id="main-content"]/div/div[2]/div[3]/div[27]/div/div[3]/a',
    'Geometry' : '//*[@id="main-content"]/div/div[2]/div[3]/div[28]/div/div[3]/a',
    'Ratio and Proportion' : '//*[@id="main-content"]/div/div[2]/div[3]/div[29]/div/div[3]/a',
    'Equations' : '//*[@id="main-content"]/div/div[2]/div[3]/div[30]/div/div[3]/a',
    'Statistics' : '//*[@id="main-content"]/div/div[2]/div[3]/div[31]/div/div[3]/a',
    'True Discount' : '//*[@id="main-content"]/div/div[2]/div[3]/div[32]/div/div[3]/a',
    'Data Interpretation' : '//*[@id="main-content"]/div/div[2]/div[3]/div[33]/div/div[3]/a',
        
}

new_dict = {}
for key in data.keys():
    key2 = key.lower()
    new_dict[key2] = data[key]

#//*[@id="main-content"]/div/div[2]/div[3]/div[33]/div/div[3]/a

with open('Qtests.json', 'w') as json_file:
  json.dump(new_dict, json_file)