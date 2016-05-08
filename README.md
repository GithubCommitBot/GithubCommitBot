# GithubCommitBot
For the Github Commit Bot for the KTH course: Projektuppgift i introduktion till datalogi (DD1349). 
The Github Commit bot will automatically check if commits can be made, and then commit these with a commit message. 

The Github commit bot reads two files: 
  1. It's own file, where it checks and tracks changes and reads function names and comments. 
  2. The test file, which is can run to check whether or not a function is good enough to push to github. 
  
It uses 3 libaries: 
  1. nltk for the Natural Language processing part of analyzing its ow file, and most notably function names and comments. http://www.nltk.org/ 
  2. unittest, which is a Standard Python libary for testing. https://docs.python.org/3/library/unittest.html
  3. PyGithub for easily accessing the Github API. https://github.com/PyGithub/PyGithub 

Python version: 3.4.2

Process: 
  The project will be developed using TDD (Test-Driven Development). This is in part so that the bot can then automatically run and check the tests. The natural language components will be added to help it analyze text and write its own commit messages.
  
Installation: 
  Download the masters branch. Check the BotBranch. Make a test case in bot_test_file.py (for example def botCanHelloWorld: self.assertEqual(botHello(), "Hello World!"). Write the corresponding code in bot_home (def botHello(): print("Hello World!") return "Hello World!"). Run bot_home. Check the BotBranch. Check pull requests for master. Voila. 

Testing Strategy: 
  As said above, TDD. 
  
Branch Explaination:
  There are a total of three branches. Masters, BotBranch and HumanBranch. The Human is only ever allowed to work on the HumanBranch and push to masters (unless in emergencies). The Bot is only allowed to commit to the BotBranch but may make pull requests to master (which Human will then need to approve). 
  
Possible expansions (further Milestones, if time is to be had): 
  Bot can open and close issues, comment on Milestones and write little agressive messages of blame/reminders/random. 
    

