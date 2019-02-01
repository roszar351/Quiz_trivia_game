import requests
import ast
import html
import json
import random

#####################################
#   Made by: Damian Skrzypek        #
#                                   #
#####################################

# Used to print out all elements of a list for debugging purposes
def print_all_elems(theList):
    for i in theList:
        print(i, '\n')

def how_many_questions():
        try:
                userInput = int(input("How questions should I load? (1-50): "))
                while userInput < 1 or userInput > 50:
                        userInput = int(input("Input valid number of questions (1-50): "))
                return userInput
        except ValueError:
                return 10

token = requests.get("https://opentdb.com/api_token.php?command=request")
tokenElements = json.loads(token.text)

if tokenElements["response_code"] == 0:
        print('Welcome to my trivia game!')
        numOfQuestions = how_many_questions()

        url = 'https://opentdb.com/api.php?amount=' + str(numOfQuestions) + "&" + tokenElements["token"]
        response = requests.get(url)

        #tempString = '{"response_code":0,"results":[{"category":"Entertainment: Music","type":"multiple","difficulty":"medium","question":"Which band had hits in 1972 with the songs &quot;Baby I&#039;m A Want You&quot;, &quot;Everything I Own&quot; and &quot;The Guitar Man&quot;","correct_answer":"Bread","incorrect_answers":["America","Chicago","Smokie"]},{"category":"Science & Nature","type":"multiple","difficulty":"hard","question":"Which is the chemical name of H2O?","correct_answer":"Dihydrogen Monoxide","incorrect_answers":["Ammonium chloride","Anhydrous Sodium Carbonate","Manganese dioxide"]},{"category":"Sports","type":"multiple","difficulty":"medium","question":"Which Formula One driver was nicknamed &#039;The Professor&#039;?","correct_answer":"Alain Prost","incorrect_answers":["Ayrton Senna","Niki Lauda","Emerson Fittipaldi"]},{"category":"History","type":"multiple","difficulty":"easy","question":"In which year did the Invasion of Kuwait by Iraq occur?","correct_answer":"1990","incorrect_answers":["1992","1988","1986"]},{"category":"History","type":"boolean","difficulty":"easy","question":"Adolf Hitler was a german soldier in World War I.","correct_answer":"True","incorrect_answers":["False"]},{"category":"Entertainment: Music","type":"multiple","difficulty":"medium","question":"What is the relationship between the band members of American rock band King of Leon?","correct_answer":"Brothers &amp; cousins","incorrect_answers":["Childhood friends","Former classmates","Fraternity house members"]},{"category":"Sports","type":"multiple","difficulty":"hard","question":"Which Italian footballer told Neuer where he&#039;s putting his shot and dragging it wide, during the match Italy-Germany, UEFA EURO 2016?","correct_answer":"Pelle","incorrect_answers":["Insigne","Barzagli","Giaccherini"]},{"category":"Entertainment: Music","type":"boolean","difficulty":"medium","question":"&quot;Twenty One Pilots&quot; made the song &quot;The Motion&quot; featuring Sampha.","correct_answer":"False","incorrect_answers":["True"]},{"category":"Entertainment: Japanese Anime & Manga","type":"multiple","difficulty":"medium","question":"In &quot;To Love-Ru: Darkness&quot;, which of the girls attempt making a harem for Rito Yuuki?","correct_answer":"Momo Deviluke","incorrect_answers":["Yami (Golden Darkness)","Haruna Sairenji","Mea Kurosaki"]},{"category":"Entertainment: Video Games","type":"multiple","difficulty":"hard","question":"Which of these characters wasn&#039;t a villian in Club Penguin?","correct_answer":"The Director","incorrect_answers":["Herbert P. Bear","Tusk","Ultimate Proto-Bot 10000"]}]}'
        responseElements = json.loads(response.text)

        if responseElements['response_code'] == 0:
                for i in range(0, numOfQuestions):
                        ans = []
                        option = 65
                        correctOption = 0

                        print('Question #{}'.format(i + 1))
                        print('Category => {}\nType => {}\t\tDifficulty => {}'.format(responseElements['results'][i]['category'], responseElements['results'][i]['type'], responseElements['results'][i]['difficulty']))
                        print(html.unescape(responseElements['results'][i]['question']))

                        correctAnswer = responseElements['results'][i]['correct_answer'] 
                        ans.append(correctAnswer)
                        ans.extend(responseElements['results'][i]['incorrect_answers'])
                        for j in range(1, random.randint(3, 10)):
                                random.shuffle(ans)

                        for j in ans:
                                if j == correctAnswer:
                                        correctOption = option
                                print('{}) {}'.format(chr(option), j))
                                option += 1

                        playerAns = (str(input())).lower()
                        if playerAns == correctAnswer.lower() or playerAns == str(chr(correctOption)).lower():
                                print("Correct!")
                        else:
                                print("Incorrect!\nCorrect answer is: {}".format(correctAnswer))
        else:
                print("Something went wrong with retrieving questions.")
else:
        print("Something went wrong with retrieving the session token.")
# My attempt at parsing the questions before knowing about json.loads
# print(html.unescape(responseElements['results'][0]['question']))
# print(html.unescape(responseElements['results'][0]['correct_answer']))
# print(html.unescape(responseElements['results'][0]['incorrect_answers']))

# strElems = tempString.split('{')

# def split_question_elems(fullQuestion):
#     fullQuestion = fullQuestion.replace('","', '"   "', 5)
#     fullQuestion = fullQuestion.replace('":"', '"eEEe"')
#     fullQuestion = fullQuestion.replace('":[', '"eEEe[')
#     return fullQuestion.split('   ')

# ind = len(strElems) - 1
# toRemove = 2

# # Decodes html entities
# for i in range(2, len(strElems)):
#     if i == ind:
#         toRemove = 3
#     strElems[i] = html.unescape(strElems[i])
#     strElems[i] = strElems[i][:len(strElems[i]) - toRemove]

# del ind
# del toRemove

# # strElems[0] is empty
# # strElems[1] contains response_code
# # strElems[i] i > 1, contains questions

# allQuestions = []

# for i in range(2, len(strElems)):
#     question = {}
#     qElems = split_question_elems(strElems[i])
#     for j in qElems:
#         x = j.split('eEEe')
#         question[x[0]] = x[1]
#     allQuestions.append(question)

# #print_all_elems(allQuestions)
