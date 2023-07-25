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
    'Assertion and Reason' : '//*[@id="main-content"]/div/div[2]/div[3]/div[4]/div/div[3]/a',
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
    'Seating Arrangement' : '//*[@id="main-content"]/div/div[2]/div[3]/div[20]/div/div[3]/a',
    'Data Arrangement' : '//*[@id="main-content"]/div/div[2]/div[3]/div[21]/div/div[3]/a',
    'Number Sequence and Series' : '//*[@id="main-content"]/div/div[2]/div[3]/div[22]/div/div[3]/a',
    'Functions' : '//*[@id="main-content"]/div/div[2]/div[3]/div[23]/div/div[3]/a',
    'Rearranging Words' : '//*[@id="main-content"]/div/div[2]/div[3]/div[24]/div/div[3]/a',
    'Odd man out' : '//*[@id="main-content"]/div/div[2]/div[3]/div[25]/div/div[3]/a',
    'Statements and Conclusions' : '//*[@id="main-content"]/div/div[2]/div[3]/div[26]/div/div[3]/a',
    'Course of action' : '//*[@id="main-content"]/div/div[2]/div[3]/div[27]/div/div[3]/a',
    'Statement and assumption' : '//*[@id="main-content"]/div/div[2]/div[3]/div[28]/div/div[3]/a',
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
    'Sentence Formation' : '//*[@id="main-content"]/div/div[2]/div[3]/div[4]/div/div[3]/a',
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




data2 = {
    'COMPLETED' : [],
    'INCOMPLETE' : [],
    'ERROR' : []
}

tests = {
    'TESTS' : [
        #15/07
        ['a', 'q', 'mensuration', 1],
        ['a', 'q', 'mensuration', 4],
        ['a', 'q', 'geometry', 2],
        ['a', 'r', 'paper folding', 1],
        ['c', 'b', '2d array', 1],
        ['c', 'b', '2d array', 3],               

        #14/07
        ['a', 'q', 'ratio and proportion', 2],
        ['a', 'q', 'ratio and proportion', 3],
        ['a', 'q', 'ratio and proportion', 4], 
        ['a', 'r', 'cube and cuboids', 1],
        ['a', 'r', 'cube and cuboids', 2],
        ['a', 'r', 'number puzzles', 1],
        ['a', 'v', 'idioms and phrases', 1],
        ['a', 'v', 'idioms and phrases', 2],
        ['c', 'b', 'bitwise operator', 2],       
        
        #13/07
        ['a', 'q', 'sequence and series', 1],#####
        ['a', 'q', 'mixture and alligation', 1],
        ['a', 'q', 'mixture and alligation', 2],
        ['a', 'q', 'mixture and alligation', 3],
        ['a', 'q', 'mixture and alligation', 4],
        ['a', 'r', 'dices and cubes', 1],
        ['a', 'r', 'graph chart', 1],
        ['a', 'v', 'grammatical error', 1],
        ['a', 'v', 'sentence correction', 1],
        ['c', 'b', 'strings', 3],

        #12/07
        ['a', 'q', 'races and games', 1],
        ['a', 'q', 'chain rule', 1],
        ['a', 'q', 'chain rule', 2],
        ['a', 'r', 'statement and assumption', 1],    
        ['a', 'r', 'statement and assumption', 2],
        ['a', 'r', 'image based problems', 1],
        ['a', 'r', 'paper cutting', 1],
        ['a', 'v', 'sentence selection', 1], 
        ['a', 'v', 'sentence selection', 2],
        ['c', 'b', 'strings', 2],

        #11/07
        ['a', 'q', 'height and distance', 1],
        ['a', 'q', 'surds and indices', 1],
        ['a', 'q', 'surds and indices', 2],
        ['a', 'r', 'statements and conclusions', 1],
        ['a', 'r', 'statements and conclusions', 2],
        ['a', 'r', 'statements and conclusions', 3],
        ['a', 'r', 'course of action', 1],
        ['a', 'v', 'passage comprehensive', 1],
        ['a', 'v', 'articles', 1],
        ['c', 'b', 'arrays', 2],

        #10/07
        ['a', 'q', 'clocks', 1],
        ['a', 'q', 'clocks', 2],
        ['a', 'q', 'calendar', 1],
        ['a', 'r', 'odd man out', 1],
        ['a', 'r', 'odd man out', 2],
        ['a', 'r', 'odd man out', 3],
        ['a', 'v', 'fill in the blanks', 1],
        ['a', 'v', 'fill in the blanks', 2],
        ['c', 'b', 'arrays', 1],

        #08/07
        ['a', 'q', 'algebra', 1],
        ['a', 'q', 'algebra', 2],
        ['a', 'q', 'simple interest & compound interest', 1],
        ['a', 'r', 'functions', 1],
        ['a', 'r', 'rearranging words', 1],
        ['c', 'b', 'functions', 2],
        ['c', 'b', 'functions', 3],

        #07/07
        ['a', 'q', 'partnership', 1],
        ['a', 'q', 'partnership', 2],
        ['a', 'q', 'sequence and series', 1], 
        ['a', 'r', 'data arrangement', 1],
        ['a', 'r', 'data arrangement', 2], 
        ['a', 'r', 'data arrangement', 3],
        ['a', 'r', 'data arrangement', 4],
        ['a', 'v', 'sentence improvement', 2],
        ['a', 'v', 'sentence improvement', 3],
        ['c', 'b', 'functions', 1],

        #06/07
        ['a', 'q', 'probability', 1],
        ['a', 'q', 'probability', 2],
        ['a', 'q', 'probability', 3],
        ['a', 'q', 'probability', 4],
        ['a', 'q', 'probability', 5],
        ['a', 'r', 'number sequence and series', 1],
        ['a', 'r', 'number sequence and series', 2],
        ['a', 'v', 'theme detection', 1],
        ['a', 'v', 'sentence improvement', 1], 
        ['c', 'b', 'number based problems', 3],

        #05/07
        ['a', 'q', 'permutation and combination', 3],
        ['a', 'q', 'permutation and combination', 1],
        ['a', 'q', 'permutation and combination', 6],
        ['a', 'r', 'venn diagram', 2],
        ['a', 'r', 'venn diagram', 3],
        ['a', 'r', 'seating arrangement', 2], 
        ['a', 'r', 'seating arrangement', 4],
        ['a', 'v', 'jumbled sentence', 1], 
        ['a', 'v', 'jumbled sentence', 3],
        ['c', 'b', 'number based problems', 2],


        #04/07
        ['a', 'q', 'problems on trains', 2],
        ['a', 'q', 'problems on trains', 3],
        ['a', 'q', 'permutation and combination', 2],
        ['a', 'r', 'logical deduction', 1],
        ['a', 'r', 'logical deduction', 2],
        ['a', 'r', 'logical order', 1], 
        ['a', 'r', 'venn diagram', 1],
        ['a', 'v', 'theme detection', 1],
        ['a', 'v', 'jumbled sentence', 2], 
        ['c', 'b', 'number based problems', 1],

        #03/07
        ['a', 'q', 'averages', 1],
        ['a', 'q', 'averages', 2],
        ['a', 'q', 'averages', 3],
        ['a', 'r', 'pattern completion', 1], 
        ['a', 'r', 'pattern completion', 2],
        ['a', 'r', 'shape construction', 1],
        ['a', 'r', 'coding and decoding', 5],
        ['a', 'v', 'jumbled sentence', 2],
        ['a', 'v', 'jumbled sentence', 3],
        ['c', 'b', 'number crunching', 3],

        #01/07
        ['a', 'q', 'boats and stream', 2], 
        ['a', 'q', 'boats and stream', 3], 
        ['a', 'q', 'problems on ages', 3], 
        ['a', 'r', 'critical reasoning', 1],
        ['a', 'r', 'critical reasoning', 2],
        ['a', 'r', 'figure matrix', 1],
        ['a', 'r', 'grouping of images', 1],
        ['a', 'v', 'reading comprehension', 1],
        ['a', 'v', 'reading comprehension', 2],
        ['c', 'b', 'number crunching', 2], 

        #30/06
        ['a', 'q', 'time speed distance', 3],
        ['a', 'q', 'problems on trains', 1], 
        ['a', 'q', 'problems on trains', 3],
        ['a', 'r', 'blood relation', 1],
        ['a', 'r', 'blood relation', 2],
        ['a', 'r', 'blood relation', 3],
        ['a', 'r', 'blood relation', 4],
        ['a', 'v', 'passage and inference', 1],
        ['c', 'b', 'patterns', 5],


        #29/06
        ['a', 'q', 'pipes and cisterns', 1],
        ['a', 'q', 'pipes and cisterns', 3],
        ['a', 'q', 'time speed distance', 2],
        ['a', 'r', 'direction sense', 1],
        ['a', 'r', 'direction sense', 3],
        ['a', 'r', 'coding and decoding', 1],
        ['a', 'r', 'coding and decoding', 3],
        ['a', 'v', 'selecting words', 1], 
        ['a', 'v', 'selecting words', 2], 
        ['c', 'b', 'patterns', 4],


        #28/06
        ['a', 'q', 'time & work', 1],
        ['a', 'q', 'time & work', 3],
        ['a', 'q', 'time & work', 4],
        ['a', 'r', 'assertion and reason', 1], 
        ['a', 'r', 'image analysis', 1], 
        ['a', 'r', 'dot situation', 1], 
        ['a', 'r', 'embedded image', 1], 
        ['a', 'v', 'sentence formation', 1], 
        ['a', 'v', 'synonyms', 2], 
        ['c', 'b', 'looping', 3], 


        #27/06
        ['a', 'q', 'percentage', 2], 
        ['a', 'q', 'percentage', 4], 
        ['a', 'q', 'time & work', 2], 
        ['a', 'r', 'puzzle', 1], 
        ['a', 'r', 'data sufficiency', 4], 
        ['a', 'r', 'data sufficiency', 5], 
        ['a', 'r', 'team_formation', 1], 
        ['a', 'v', 'spotting error', 2], 
        ['a', 'v', 'spotting error', 3], 
        ['c', 'b', 'conditional statements (if / while etc)', 3],

        #26/06
        ['a', 'q', 'number system', 1], 
        ['a', 'q', 'number system', 3], 
        ['a', 'q', 'hcf & lcm', 5], 
        ['a', 'r', 'syllogisms', 3], 
        ['a', 'r', 'puzzle', 4], 
        ['a', 'r', 'puzzle', 2], 
        ['a', 'r', 'puzzle', 3], 
        ['a', 'v', 'sentence completion', 2], 
        ['a', 'v', 'sentence completion', 4], 
        ['c', 'b', 'basic input output and data types', 4],
    ]
}

student = {
    'email' : '',
    'password' : '',
    'answer-percentage' : 100,
    'time-percentage' : 100,
    'attend-c-test' : False
}

new_dict = {}
for key in data_R.keys():
    key2 = key.lower()
    new_dict[key2] = data_R[key]

with open('Student.json', 'w') as json_file:
  json.dump(student, json_file)


