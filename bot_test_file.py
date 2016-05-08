## Hello there.
## This is a test file using the Python inbuilt library unittest.

## OTHER FILE: Uses the bot_home file <3 

## Made by Madeleine Lindow, CDATE12, Project i INDAN DD1349


import unittest ## YAY!


class TestGithubCommitBotMethods(unittest.TestCase):

    ## Prio 1 - Milestone 1 (due 8/5)
    def botCanCommit(self): ## Basic functionality of the Github commit bot
        self.assertTrue(botCommit())

    def botCanCommitOnTestPass(self): ## This test and the one above starts the automatic commiting!
        self.assertTrue(botCanCommitOnTestPass())

    def botAwakens(self): ## Makes sure it checks the Test Pass every now and then.
        self.assertTrue(botWakeUp())
        
    def botCanRunTestFile(self):
        self.assertTrue(botTestTests())

    def botCanPullFromMaster(self):
        self.assertTrue(botPull())

    def botCanDetectFileChange(self):
        self.assertTrue(botDetectFileChange())

    def botCanPushToBotBranch(self):
        self.assertTrue(botPush())
            
    ## Prio 2 - Milestone 2 (due 14/5)
    def botCanReadFiles(self): ## In a certain folder, mind you.
        self.assertTrue(botRead())
        
    def botCanReadComments(self):
        self.assertTrue(botReadComment())

    def botCanNLP(self): # It can tokenize, tag the tokens and get certain chunks.
        self.assertTrue(botCanTokenize())

    def botCanWriteCommitMessages(self):
        self.assertTrue(botCanWriteMessages())

    def botCanDetectConflicts(self):
        self.assertTrue(botCanDetectIssues())

    def botCanPullRequest(self):
        self.assertTrue(botPullRequest())

    ## Prio 3 - Milestone 3 (due 19/5)
    def botCanCommitUpdatedTestFile(self):
        self.assertTrue(botCanCommitUpdatedTestFile())

    def botCanWriteComments(self):
        self.assertTrue(botWriteComment())

    def botCanCheckHumanBranch(self):
        self.assertTrue(botCheckOnHuman())
        
    def botCanCloseIssues(self):
        self.assertTrue(botCloseIssues()

    def botCanReadIssues(self): 
        self.assertTrue(botReadIssues())

    def botCanMakeIssue(self): # If it feels like being annoying!
        self.assertTrue(botMakeIssues())

    def botCanMerge(self):
        self.assertTrue(botMerge())

    def botCanUseIssueLabels(self):
        self.assertTrue(botUseIssueLabels())

    ## def setUp(self): ## Is this when the botAwakens?
    ## def tearDown(self):

    

        
