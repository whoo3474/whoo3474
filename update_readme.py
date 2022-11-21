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
📧  ***Contact Email*** : minhan_a@naver.com

👨🏻‍💻  ***Tech & Daily Blog*** : https://minhan2.tistory.com

[![github stats](https://github-readme-stats.vercel.app/api?username=whoo3474&show_icons=true&hide_border=False)](https://minhan2.tistory.com)



✨ ***My Certificate***

<div>
<img src="https://tistory1.daumcdn.net/tistory/2920456/skin/images/hashicorp-certified-terraform-associate.png" width="140" height="140"/>
<img src="https://tistory1.daumcdn.net/tistory/2920456/skin/images/aws-certified-solutions-architect-associate.png" width="140" height="140"/>
<img src="https://tistory1.daumcdn.net/tistory/2920456/skin/images/cka-certified-kubernetes-administrator.png" width="150" height="150"/>
<div/>


- [HashiCorp Certified: Terraform Associate (002)](https://www.credly.com/badges/f7a6c791-502c-47ec-a33b-bb45c75b6dc6/public_url)
- [AWS Certified Solutions Architect – Associate](https://www.credly.com/badges/5e5b409a-fb97-4f97-b7fe-b19c659a54ee/public_url)
- [CKA: Certified Kubernetes Administrator](https://www.credly.com/badges/ca5ed398-930a-4a7b-8cb7-9189e911c77b/public_url)



🖋 ***Latest Blog Post***

"""

readme_text = f"{markdown_text}{latest_blog_post_list}"

with open("README.md", 'w', encoding='utf-8') as f:
    f.write(readme_text)
