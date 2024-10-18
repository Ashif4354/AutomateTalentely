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

data_C_b = {
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

data_C_ad = {
    'Recursion' : '//*[@id="main-content"]/div/div[2]/div[3]/div[1]/div/div[3]/a',
    'Advanced Bit Manipulation' : '//*[@id="main-content"]/div/div[2]/div[3]/div[2]/div/div[3]/a',
    'Advanced Arrays' : '//*[@id="main-content"]/div/div[2]/div[3]/div[3]/div/div[3]/a',
    'Multi Dimensional Array' : '//*[@id="main-content"]/div/div[2]/div[3]/div[4]/div/div[3]/a',
    'Advanced String' : '//*[@id="main-content"]/div/div[2]/div[3]/div[5]/div/div[3]/a',    
}

data_C_d = {
    'singly linked list' : '//*[@id="main-content"]/div/div[2]/div[3]/div[1]/div/div[3]/a',
    'doubly linked list' : '//*[@id="main-content"]/div/div[2]/div[3]/div[2]/div/div[3]/a',
    'circular linked list' : '//*[@id="main-content"]/div/div[2]/div[3]/div[3]/div/div[3]/a',
    'stack' : '//*[@id="main-content"]/div/div[2]/div[3]/div[4]/div/div[3]/a',
    'queue' : '//*[@id="main-content"]/div/div[2]/div[3]/div[5]/div/div[3]/a',
    'binary tree' : '//*[@id="main-content"]/div/div[2]/div[3]/div[6]/div/div[3]/a',
    'binary search tree' : '//*[@id="main-content"]/div/div[2]/div[3]/div[7]/div/div[3]/a'
}

data_C_al = {
    'Sorting' : '//*[@id="main-content"]/div/div[2]/div[3]/div[1]/div/div[3]/a',
    'Searching' : '//*[@id="main-content"]/div/div[2]/div[3]/div[2]/div/div[3]/a',
    'Hashing' : '//*[@id="main-content"]/div/div[2]/div[3]/div[3]/div/div[3]/a',
    'Brute Force Algorithm' : '//*[@id="main-content"]/div/div[2]/div[3]/div[4]/div/div[3]/a',
    'Divide and Conquer' : '//*[@id="main-content"]/div/div[2]/div[3]/div[5]/div/div[3]/a',
    'Greedy' : '//*[@id="main-content"]/div/div[2]/div[3]/div[6]/div/div[3]/a',
    'Mathematical' : '//*[@id="main-content"]/div/div[2]/div[3]/div[7]/div/div[3]/a',
    'Combinatorial' : '//*[@id="main-content"]/div/div[2]/div[3]/div[8]/div/div[3]/a',
    'Primality testing' : '//*[@id="main-content"]/div/div[2]/div[3]/div[9]/div/div[3]/a',
    'Backtracking' : '//*[@id="main-content"]/div/div[2]/div[3]/div[10]/div/div[3]/a',
    'Pattern Matching' : '//*[@id="main-content"]/div/div[2]/div[3]/div[11]/div/div[3]/a',
    'Graph' : '//*[@id="main-content"]/div/div[2]/div[3]/div[12]/div/div[3]/a',
    'Dynamic Programming' : '//*[@id="main-content"]/div/div[2]/div[3]/div[13]/div/div[3]/a',
    'Game theory' : '//*[@id="main-content"]/div/div[2]/div[3]/div[14]/div/div[3]/a',
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

all_tests = {
    "26/06/2023" : [ 
        ["a", "q", "number system", 1, "Number system_Level_2_Test 1"], 
        ["a", "q", "number system", 3, "Number system_Level_3_Test 1"], 
        ["a", "q", "hcf & lcm", 5, "HCF and LCM_Level_3_Test 1"], 
        ["a", "r", "syllogisms", 3, "Syllogism_Level_3_Test_1"], 
        ["a", "r", "puzzle", 4, "Puzzle_level_1_test_1"], 
        ["a", "r", "puzzle", 2, "number puzzle_level_2_test 1"], 
        ["a", "r", "puzzle", 3, "character puzzle_level_2_test 1"], 
        ["a", "v", "sentence completion", 2, "Sentence Completion_Level_2_Test 1"], 
        ["a", "v", "sentence completion", 4, "Sentence Completion_Level_3_Test 1"], 
        ["c", "b", "basic input output and data types", 4, "Basic_I/P_O/P_Level_3"]
    ],

    "27/06/2023" : [
        ["a", "q", "percentage", 2, "Percentage_Level_1_Test_2"], 
        ["a", "q", "percentage", 4, "Percentage_Lvel_2_Test_2"], 
        ["a", "q", "time & work", 2, "Time and Work_Level_1_Test 1"], 
        ["a", "r", "puzzle", 1, "Puzzle_Level_3_Test 1"], 
        ["a", "r", "data sufficiency", 4, "Data Sufficiency_Level_2_Test 2"], 
        ["a", "r", "data sufficiency", 5, "Data Sufficiency_level_3_test_2"], 
        ["a", "r", "team_formation", 1, "Team formation_Level_1_Test 1"], 
        ["a", "v", "spotting error", 2, "Spotting Errors_Level_1_Test 2"], 
        ["a", "v", "spotting error", 3, "Spotting Errors_Level_2_Test 1"], 
        ["c", "b", "conditional statements (if / while etc)", 3, "Conditional_Statement_Level _2"]
    ],

    "28/06/2023" : [
        ["a", "q", "time & work", 1, "Time and Work_Level_1_Test 2"], 
        ["a", "q", "time & work", 3, "Time and Work_Level_2_Test 1"], 
        ["a", "q", "time & work", 4, "Time and Work_Level_2_Test 2"], 
        ["a", "r", "assertion and reason", 1, "Assertion and Reason_Level_1_Test 1"], 
        ["a", "r", "image analysis", 1, "Image Analysis_Level_1_Test 1"], 
        ["a", "r", "dot situation", 1, "Dot situations_Level_1_Test 1"], 
        ["a", "r", "embedded image", 1, "Embedded Image_Level_1_Test 1"], 
        ["a", "v", "sentence formation", 1, "Sentence Formation_Level_1_Test 1"], 
        ["a", "v", "synonyms", 2, "Synonyms_Level_1_Test 2"], 
        ["c", "b", "looping", 3, "Looping_Level_2"]
    ],

    "29/06/2023" :  [
        ["a", "q", "pipes and cisterns", 1, "Pipes and Cistern_Level_1_Test 1"], 
        ["a", "q", "pipes and cisterns", 3, "Pipes and Cistern_Level_2_Test 1"], 
        ["a", "q", "time speed distance", 2, "Time_Speed_Distance_Level_1_Test_1"], 
        ["a", "r", "direction sense", 1, "Direction Sense_Level_1_Test 1"], 
        ["a", "r", "direction sense", 3, "Direction Sense_Level_2_Test 1"], 
        ["a", "r", "coding and decoding", 1, "Coding and Decoding_Level_1_Test 1"], 
        ["a", "r", "coding and decoding", 3, "Coding and Decoding_Level_2_Test 1"], 
        ["a", "v", "selecting words", 1, "Selecting words_Level_1_Test 1"], 
        ["a", "v", "selecting words", 2, "Selecting words_Level_2_Test 1"], 
        ["c", "b", "patterns", 4, "Pattern_Level_2"]
    ],

    "30/06/2023" : [
        ["a", "q", "time speed distance", 3, "Time_Speed_Distance_Level_2_Test_1"], 
        ["a", "q", "problems on trains", 1, "Problems on Trains_Level_1_test 1"], 
        ["a", "r", "blood relation", 1, "Blood Relation_Level_1_Test 1"], 
        ["a", "r", "blood relation", 2, "Blood Relation_Level_1_Test 2"], 
        ["a", "r", "blood relation", 3, "Blood Relation_Level_2_Test 1"], 
        ["a", "r", "blood relation", 4, "Blood Relation_Level_2_Test 2"], 
        ["a", "v", "passage and inference", 1, "Passage and Inference_Level_1_Test 1"], 
        ["c", "b", "patterns", 5, "Pattern_Level_3"]
    ],
    
    "01/07/2023" : [
        ["a", "q", "boats and stream", 2, "Boats and Streams_Level_1_test 2"], 
        ["a", "q", "boats and stream", 3, "Boats and Streams_Level_2_test 1"], 
        ["a", "q", "problems on ages", 3, "Problems on Ages_Level_2_test 1"], 
        ["a", "r", "critical reasoning", 1, "Critical Reasoning_Level_1_Test 1"], 
        ["a", "r", "critical reasoning", 2, "Critical Reasoning_Level_2_Test 1"], 
        ["a", "r", "figure matrix", 1, "Figure Matrix_Level_1_Test 1"],         
        ["a", "r", "grouping of images", 1, "Grouping Of Images_Level_1_Test 1"], 
        ["a", "v", "reading comprehension", 1, "Reading Comprehension_Level_1_Test 1"], 
        ["a", "v", "reading comprehension", 2, "Reading Comprehension_Level_3_Test 1"], 
        ["c", "b", "number crunching", 2, "Number_Crunching_Level_1"]
    ], 

    "03/03/2023" : [
        ["a", "q", "averages", 1, "Averages_Level_3_Test 1"], 
        ["a", "q", "averages", 2, "Averages_Level_1_Test 1"], 
        ["a", "q", "averages", 3, "Averages_Level_2_Test 1"], 
        ["a", "r", "pattern completion", 1, "Pattern Completion_Level_1_Test 1"], 
        ["a", "r", "pattern completion", 2, "pattern completion_level_2_test 1"], 
        ["a", "r", "shape construction", 1, "Shape Construction_Level_1_Test 1"], 
        ["a", "r", "coding and decoding", 5, "Coding and Decoding_Level_1_Test 3"], 
        ["c", "b", "number crunching", 3, "Number_Crunching_Level_2"]
    ],

    "04/07/2023" : [
        ["a", "q", "problems on trains", 2, "Problems on Trains_Level_1_test 2"], 
        ["a", "q", "problems on trains", 3, "Problems on Trains_Level_2_test 1"], 
        ["a", "q", "permutation and combination", 2, "Permutation and Combination_Level_1_test 1"], 
        ["a", "r", "logical deduction", 1, "Logical Deduction_Level_1_Test 1"], 
        ["a", "r", "logical deduction", 2, "Logical Deduction_Level_2_Test 1"], 
        ["a", "r", "logical order", 1, "Logical Order_Level_1_Test 1"], 
        ["a", "r", "venn diagram", 1, "Venn Diagram_Level_1_Test 1"], 
        ["a", "v", "jumbled sentence", 2, "Jumbled sentences_Level_1_test_1"], 
        ["c", "b", "number based problems", 1, "Number_Based_Problem_Level_0"]
    ],
    
    "05/07/2023" : [
        ["a", "q", "permutation and combination", 3, "Permutation_Combination_Level_1_Test_2"], 
        ["a", "q", "permutation and combination", 1, "Permutation and Combination_Level_2_test 1"], 
        ["a", "q", "permutation and combination", 6, "Permutation_and_Combination_Level_2_Test_2"], 
        ["a", "r", "venn diagram", 2, "Venn Diagram_Level_2_Test 1"], 
        ["a", "r", "venn diagram", 3, "Venn Diagram_Level_3_Test_1"], 
        ["a", "r", "seating arrangement", 2, "Seating Arrangement_Level_3_Test 1"], 
        ["a", "r", "seating arrangement", 4, "Seating Arrangement_Level_2_Test 1"], 
        ["a", "v", "jumbled sentence", 1, "Jumbled Sentence_Level_3_Test 1"], 
        ["a", "v", "jumbled sentence", 3, "Jumbled sentences_Level_2_test_1"], 
        ["c", "b", "number based problems", 2, "Number_Based_Problem_Level_1"]
    ],

    "06/07/2023" : [
        ["a", "q", "probability", 1, "Probability_Level_1_test 1"], 
        ["a", "q", "probability", 2, "Probability_Level_1_test 2"], 
        ["a", "q", "probability", 3, "Probability_Level_1_test 3"], 
        ["a", "q", "probability", 4, "Probability_Level_3_test 1"], 
        ["a", "q", "probability", 5, "Probability_Level_2_test 1"], 
        ["a", "r", "number sequence and series", 1, "Number series_Level_1_Test_1"], 
        ["a", "r", "number sequence and series", 2, "Number series_Level_2_Test_1"], 
        ["a", "v", "theme detection", 1, "Theme Detection_Level_1_Test 1"], 
        ["a", "v", "sentence improvement", 1, "Sentence Improvement_Level_1_Test 1"], 
        ["c", "b", "number based problems", 3, "Number_Based_Problem_Level_2"]
    ],      
     
    "07/07/2023" : [ 
        ["a", "q", "partnership", 1, "Partnership_Level_1_test 1"], 
        ["a", "q", "partnership", 2, "Partnership_Level_3_test 1"], 
        ["a", "r", "data arrangement", 1, "Data Arrangement_Level_1_Test 1"], 
        ["a", "r", "data arrangement", 2, "data arrangement_level_2_test 1"], 
        ["a", "r", "data arrangement", 3, "data arrangement_level_2_test 2"], 
        ["a", "r", "data arrangement", 4, "Data Arrangement_Level_1_Test 2"], 
        ["a", "v", "sentence improvement", 2, "Sentence Improvement_Level_1_Test 2"], 
        ["a", "v", "sentence improvement", 3, "Sentence Improvement_Level_2_Test 1"], 
        ["c", "b", "functions", 1, "Function_Level_0"]
    ],      

    "08/07/2023" : [
        ["a", "q", "algebra", 1, "Algebra_Level_1_test 1"], 
        ["a", "q", "algebra", 2, "Algebra_Level_2_test 1"], 
        ["a", "q", "simple interest & compound interest", 1, "Simple Interest and Compound Interest_Level_1_Test 1"], 
        ["a", "r", "functions", 1, "Functions_Level_1_test_1"], 
        ["a", "r", "rearranging words", 1, "Rearranging words_Level_1_test_1"], 
        ["c", "b", "functions", 2, "Function_Level_1"], 
        ["c", "b", "functions", 3, "Function_Level_2"]
    ],

    "10/07/2023" : [
        ["a", "q", "clocks", 1, "Clocks_Level_1_test 1"], 
        ["a", "q", "clocks", 2, "Clocks_level_2_test 1"], 
        ["a", "q", "calendar", 1, "Calendar_Level_1_test 1"], 
        ["a", "r", "odd man out", 1, "Odd man out_Level_1_test_1"], 
        ["a", "r", "odd man out", 2, "Odd man out_Level_2_test_1"], 
        ["a", "r", "odd man out", 3, "Odd man out_Level_1_test_2"], 
        ["a", "v", "fill in the blanks", 1, "Fill in the blanks_level_1_test_1"], 
        ["a", "v", "fill in the blanks", 2, "Fill in the blanks_level_1_test_2"], 
        ["c", "b", "arrays", 1, "Array_Level_0"]
    ],    

    "11/07/2023" : [ 
        ["a", "q", "height and distance", 1, "Heights and distance_Level_1_test 1"], 
        ["a", "q", "surds and indices", 1, "Surds and Indices_Level_1_test 1"], 
        ["a", "q", "surds and indices", 2, "Surds and Indices_Level_1_test 2"], 
        ["a", "r", "statements and conclusions", 1, "Statements and Conclusions_Level_1_test_1"], 
        ["a", "r", "statements and conclusions", 2, "Statements and Conclusions_Level_2_test_1"], 
        ["a", "r", "statements and conclusions", 3, "Statement and Conclusion_Level_3_Test_1"], 
        ["a", "r", "course of action", 1, "Course of action_level_2_test 1"], 
        ["a", "v", "passage comprehensive", 1, "Passage comprehensive_level_1_test_1"], 
        ["a", "v", "articles", 1, "Articles level_1_test_1"], 
        ["c", "b", "arrays", 2, "Array_Level_1"]
    ],    

    "12/07/2023" : [
        ["a", "q", "races and games", 1, "Races and Games_Level_1_test 1"], 
        ["a", "q", "chain rule", 1, "Chain Rule_Level_1_test 1"], 
        ["a", "q", "chain rule", 2, "Chain Rule_Level_1_test 2"], 
        ["a", "r", "statement and assumption", 1, "Statement and assumption_level_2_test 1"], 
        ["a", "r", "statement and assumption", 2, "Statement and Assumption_Level_3_Test_1"], 
        ["a", "r", "image based problems", 1, "image based problems_level_2_test_1"], 
        ["a", "r", "paper cutting", 1, "Paper cutting_level_2_test 1"], 
        ["a", "v", "sentence selection", 1, "Sentence selection_level_1_test_1"], 
        ["a", "v", "sentence selection", 2, "Sentence selection_level_2_test_1"], 
        ["c", "b", "strings", 2, "String_Level_1"]
    ],
     
    "13/07/2023" : [
        ["a", "q", "sequence and series", 1, "Sequence and Series_Level_1_test 1"], 
        ["a", "q", "mixture and alligation", 1, "Mixture and Alligation_Level_1_test 1"], 
        ["a", "q", "mixture and alligation", 2, "Mixture and Alligation_Level_1_test 2"], 
        ["a", "q", "mixture and alligation", 3, "Mixture and Alligation_Level_3_test 1"], 
        ["a", "q", "mixture and alligation", 4, "Mixture and Alligation_Level_2_test 1"], 
        ["a", "r", "dices and cubes", 1, "dices and cubes_level_2_test 1"], 
        ["a", "r", "graph chart", 1, "graph chart_level_2_test 1"], 
        ["a", "v", "grammatical error", 1, "Grammatical error_level_1_test_1"], 
        ["a", "v", "sentence correction", 1, "Sentence Correction_level_2_test 1"], 
        ["c", "b", "strings", 3, "String_Level_2"]
    ],    

    "14/07/2023" : [
        ["a", "q", "ratio and proportion", 2, "Ratio and Proportion_Level_1_Test 1"], 
        ["a", "q", "ratio and proportion", 3, "Ratio and Proportion_Level_3_Test 1"], 
        ["a", "q", "ratio and proportion", 4, "Ratio and Proportion_Level_2_Test 1"], 
        ["a", "r", "cube and cuboids", 1, "cube and cuboids_level_2_test 1"], 
        ["a", "r", "cube and cuboids", 2, "cube and cuboids_level_1_test 1"], 
        ["a", "r", "number puzzles", 1, "Number Puzzles_Level_2_test_1"], 
        ["a", "v", "idioms and phrases", 1, "Idioms and phrases_level_1_test 1"], 
        ["a", "v", "idioms and phrases", 2, "Idioms and phrases_level_2_test 1"], 
        ["c", "b", "bitwise operator", 2, "Biwise_Level_1"]
    ],

    "15/07/2023" : [

        ["a", "q", "mensuration", 1, "Mensuration_Level_1_test 1"], 
        ["a", "q", "mensuration", 4, "Mensuration_Level_2_test 2"], 
        ["a", "q", "geometry", 2, "Geometry_Level_1_test 2"], 
        ["a", "r", "paper folding", 1, "Paper Folding_Level_2_test_1"], 
        ["c", "b", "2d array", 1, "2D_Level_0"], 
        ["c", "b", "2d array", 3, "upd_2D_Level_2"]
    ],
}

student = {
    'email' : '',
    'password' : '',
    'answer-percentage' : 100,
    'time-percentage' : 100,
    'attend-c-test' : False
}

new_dict = {}
for key in data_C_al.keys():
    key2 = key.lower()
    new_dict[key2] = data_C_al[key]

if __name__ == '__main__':
    with open('C_al_tests.json', 'w') as json_file:
        json.dump(new_dict, json_file)


