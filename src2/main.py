import post
import punish

if __name__ == "__main__":
    # post.tweetBot(1)
    # punish.dumpSSH()
    currOS = post.detectOS()
    print(post.chromeProfile(currOS))