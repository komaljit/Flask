# Flask

templates- contains all the html files for the project

static- contains css, pictures for the website

Initially the questions are stored in text file (question.json.txt). Using json module the file is taken as json input and uing randm integer, a random question is selected and its answer is stored in redis database for later comparison of correct answer. the options for answers are selected from option.json file.
