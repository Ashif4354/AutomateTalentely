import json

data_Q = {
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

data_R = {
    'Puzzle' : '//*[@id="main-content"]/div/div[2]/div[3]/div[1]/div/div[3]/a',
    'Data Sufficiency' : '//*[@id="main-content"]/div/div[2]/div[3]/div[2]/div/div[3]/a',
    'Syllogisms' : '//*[@id="main-content"]/div/div[2]/div[3]/div[3]/div/div[3]/a',
    'Assertion and Reason' : '//*[@id="main-content"]/div/div[2]/div[4]/div[2]/div/div[3]/a',
    'Image Analysis' : '//*[@id="main-content"]/div/div[2]/div[3]/div[5]/div/div[3]/a',
    'Dot situation' : '//*[@id="main-content"]/div/div[2]/div[3]/div[6]/div/div[3]/a',
    'Embedded Image' : '//*[@id="main-content"]/div/div[2]/div[3]/div[7]/div/div[3]/a',
    'team_formation' : '//*[@id="main-content"]/div/div[2]/div[3]/div[8]/div/div[3]/a',
    'Critical Reasoning' : '//*[@id="main-content"]/div/div[2]/div[3]/div[9]/div/div[3]/a',
    'Figure Matrix' : '//*[@id="main-content"]/div/div[2]/div[3]/div[10]/div/div[3]/a',
    'Grouping of Images' : '//*[@id="main-content"]/div/div[2]/div[3]/div[11]/div/div[3]/a',
    'Pattern Completion' : '//*[@id="main-content"]/div/div[2]/div[3]/div[12]/div/div[3]/a',
    'Shape Construction' : '//*[@id="main-content"]/div/div[2]/div[3]/div[13]/div/div[3]/a',
    'Direction Sense' : '//*[@id="main-content"]/div/div[2]/div[3]/div[14]/div/div[3]/a',
    'Blood Relation' : '//*[@id="main-content"]/div/div[2]/div[3]/div[15]/div/div[3]/a',
    'Coding and Decoding' : '//*[@id="main-content"]/div/div[2]/div[3]/div[16]/div/div[3]/a',
    'Logical Deduction' : '//*[@id="main-content"]/div/div[2]/div[3]/div[17]/div/div[3]/a',
    'Logical Order' : '//*[@id="main-content"]/div/div[2]/div[3]/div[18]/div/div[3]/a',
    'Venn Diagram' : '//*[@id="main-content"]/div/div[2]/div[3]/div[19]/div/div[3]/a',
    'Seating Arrangement' : '//*[@id="main-content"]/div/div[2]/div[20]/div[2]/div/div[3]/a',
    'Data Arrangement' : '//*[@id="main-content"]/div/div[2]/div[3]/div[21]/div/div[3]/a',
    'Number Sequence and Series' : '//*[@id="main-content"]/div/div[2]/div[3]/div[22]/div/div[3]/a',
    'Functions' : '//*[@id="main-content"]/div/div[2]/div[3]/div[23]/div/div[3]/a',
    'Rearranging Words' : '//*[@id="main-content"]/div/div[2]/div[3]/div[24]/div/div[3]/a',
    'Odd man out' : '//*[@id="main-content"]/div/div[2]/div[3]/div[25]/div/div[3]/a',
    'Statements and Conclusions' : '//*[@id="main-content"]/div/div[26]/div[3]/div[2]/div/div[3]/a',
    'Course of action' : '//*[@id="main-content"]/div/div[2]/div[3]/div[27]/div/div[3]/a',
    'Statement and assumption' : '//*[@id="main-content"]/div/div[28]/div[3]/div[2]/div/div[3]/a',
    'Paper cutting' : '//*[@id="main-content"]/div/div[2]/div[3]/div[29]/div/div[3]/a',
    'image based problems' : '//*[@id="main-content"]/div/div[2]/div[3]/div[30]/div/div[3]/a',
    'dices and cubes' : '//*[@id="main-content"]/div/div[2]/div[3]/div[31]/div/div[3]/a',
    'graph chart' : '//*[@id="main-content"]/div/div[2]/div[3]/div[32]/div/div[3]/a',
    'cube and cuboids' : '//*[@id="main-content"]/div/div[2]/div[3]/div[33]/div/div[3]/a',
    'Cryptarithmetic' : '//*[@id="main-content"]/div/div[2]/div[3]/div[34]/div/div[3]/a',
    'Number puzzles' : '//*[@id="main-content"]/div/div[2]/div[3]/div[35]/div/div[3]/a',
    'Paper folding' : '//*[@id="main-content"]/div/div[2]/div[3]/div[36]/div/div[3]/a'

}

data_V = {
    'Antonyms' : '//*[@id="main-content"]/div/div[2]/div[3]/div[1]/div/div[3]/a',
    'Sentence Completion' : '//*[@id="main-content"]/div/div[2]/div[3]/div[2]/div/div[3]/a',
    'Spotting Error' : '//*[@id="main-content"]/div/div[2]/div[3]/div[3]/div/div[3]/a',
    'Synonyms' : '//*[@id="main-content"]/div/div[2]/div[3]/div[4]/div/div[3]/a',
    'Sentence Formation' : '//*[@id="main-content"]/div/div[2]/div[5]/div[1]/div/div[3]/a',
    'Selecting Words' : '//*[@id="main-content"]/div/div[2]/div[3]/div[6]/div/div[3]/a',
    'Passage and Inference' : '//*[@id="main-content"]/div/div[2]/div[3]/div[7]/div/div[3]/a',
    'Reading Comprehension' : '//*[@id="main-content"]/div/div[2]/div[3]/div[8]/div/div[3]/a',
    'Jumbled Sentence' : '//*[@id="main-content"]/div/div[2]/div[3]/div[9]/div/div[3]/a',
    'Theme Detection' : '//*[@id="main-content"]/div/div[2]/div[3]/div[10]/div/div[3]/a',
    'Sentence Improvement' : '//*[@id="main-content"]/div/div[2]/div[3]/div[11]/div/div[3]/a',
    'Fill in the blanks' : '//*[@id="main-content"]/div/div[2]/div[3]/div[12]/div/div[3]/a',
    'Passage comprehensive' : '//*[@id="main-content"]/div/div[2]/div[3]/div[13]/div/div[3]/a',
    'Sentence selection' : '//*[@id="main-content"]/div/div[2]/div[3]/div[14]/div/div[3]/a',
    'Articles' : '//*[@id="main-content"]/div/div[2]/div[3]/div[15]/div/div[3]/a',
    'Grammatical error' : '//*[@id="main-content"]/div/div[2]/div[3]/div[16]/div/div[3]/a',
    'Sentence Correction' : '//*[@id="main-content"]/div/div[2]/div[3]/div[17]/div/div[3]/a',
    'Logical word sequence' : '//*[@id="main-content"]/div/div[2]/div[3]/div[18]/div/div[3]/a',
    'Idioms and phrases' : '//*[@id="main-content"]/div/div[2]/div[3]/div[19]/div/div[3]/a',
    'Spelling' : '//*[@id="main-content"]/div/div[2]/div[3]/div[20]/div/div[3]/a',
    'Subject verb agreement' : '//*[@id="main-content"]/div/div[2]/div[3]/div[21]/div/div[3]/a',
    'Paragraph formation' : '//*[@id="main-content"]/div/div[2]/div[3]/div[22]/div/div[3]/a'
}

data_C = {
    'Basic Input Output and Data Types' : '//*[@id="main-content"]/div/div[2]/div[3]/div[1]/div/div[3]/a',
    'Conditional Statements (IF / While etc)' : '//*[@id="main-content"]/div/div[2]/div[3]/div[2]/div/div[3]/a',
    'Looping' : '//*[@id="main-content"]/div/div[2]/div[3]/div[3]/div/div[3]/a',
    'Patterns' : '//*[@id="main-content"]/div/div[2]/div[3]/div[4]/div/div[3]/a',
    'Number Crunching' : '//*[@id="main-content"]/div/div[2]/div[3]/div[5]/div/div[3]/a',
    'Number Based Problems' : '//*[@id="main-content"]/div/div[2]/div[3]/div[6]/div/div[3]/a',
    'Functions' : '//*[@id="main-content"]/div/div[2]/div[3]/div[7]/div/div[3]/a',
    'Arrays' : '//*[@id="main-content"]/div/div[2]/div[3]/div[8]/div/div[3]/a',
    'Strings' : '//*[@id="main-content"]/div/div[2]/div[3]/div[9]/div/div[3]/a',
    'Bitwise Operator' : '//*[@id="main-content"]/div/div[2]/div[3]/div[10]/div/div[3]/a',
    '2D Array' : '//*[@id="main-content"]/div/div[2]/div[3]/div[11]/div/div[3]/a',
    'Structure' : '//*[@id="main-content"]/div/div[2]/div[3]/div[12]/div/div[3]/a',
    'Pointers' : '//*[@id="main-content"]/div/div[2]/div[3]/div[13]/div/div[3]/a',
    'Time Complexity' : '//*[@id="main-content"]/div/div[2]/div[3]/div[14]/div/div[3]/a',
}


new_dict = {}
for key in data_C.keys():
    key2 = key.lower()
    new_dict[key2] = data_C[key]


data2 = {
    'COMPLETED' : [],
    "INCOMPLETE" : []
}

tests = {
    'TESTS' : [
        #15/07
        ['c', 'b', 'bitwise operator', 2],
        ['a', 'q', 'mensuration', 1],
        ['a', 'q', 'mensuration', 4],
        ['a', 'q', 'geometry', 2],
        ['a', 'r', 'paper folding', 1],
        

        #14/07
        ['a', 'q', 'ratio and proportion', 2],
        ['a', 'q', 'ratio and proportion', 3],
        ['a', 'q', 'ratio and proportion', 4], 
        ['a', 'r', 'cube and cuboids', 1],
        ['a', 'r', 'cube and cuboids', 2],
        ['a', 'r', 'number puzzles', 1],
        ['a', 'v', 'idioms and phrases', 1],
        ['a', 'v', 'idioms and phrases', 2],
        ['c', 'b', '2d array', 1],
        ['c', 'b', '2d array', 3]

        
        #
        


    ]
}

with open('tests.json', 'w') as json_file:
  json.dump(tests, json_file)