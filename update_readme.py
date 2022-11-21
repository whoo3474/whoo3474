import feedparser

minhan_blog_rss_url = "https://minhan2.tistory.com/rss"
rss_feed = feedparser.parse(minhan_blog_rss_url)

MAX_POST_NUM = 10

latest_blog_post_list = ""

MAX_POST_NUM = 10

for idx, feed in enumerate(rss_feed['entries']):
    if idx > MAX_POST_NUM:
        break
    feed_date = feed['published_parsed']
    latest_blog_post_list += f"[{feed_date.tm_year}/{feed_date.tm_mon}/{feed_date.tm_mday} - {feed['title']}]({feed['link']}) <br>\n"
    
markdown_text = """### Hi there 👋
📬  Contact Email : minhan_a@naver.com

👨🏻‍💻  Tech & Daily Blog : https://minhan2.tistory.com

[![github stats](https://github-readme-stats.vercel.app/api?username=whoo3474&show_icons=true&hide_border=False)](https://minhan2.tistory.com)


✨ My Certificate

![image](https://tistory1.daumcdn.net/tistory/2920456/skin/images/hashicorp-certified-terraform-associate.png)![image](https://tistory1.daumcdn.net/tistory/2920456/skin/images/aws-certified-solutions-architect-associate.png)![image](https://tistory1.daumcdn.net/tistory/2920456/skin/images/cka-certified-kubernetes-administrator.png)


🤩 Latest Blog Post

"""

readme_text = f"{markdown_text}{latest_blog_post_list}"

with open("README.md", 'w', encoding='utf-8') as f:
    f.write(readme_text)
