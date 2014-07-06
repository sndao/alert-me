import praw
import environment


class reddit:
    def __init__(self):
        self.links = []
        self.links_str = ''

    def publish_reddit(self, links):
        for link in links:
            self.links_str += link + '\n\n'

        env = environment.environment()
        r = praw.Reddit(user_agent='Sndao self-messaging bot 1.0')
        r.login(env.reddit_username, env.reddit_password)
        r.send_message('sndao', 'Links to Eventbrite', self.links_str)

