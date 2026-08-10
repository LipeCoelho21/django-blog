from django.http import Http404
from django.shortcuts import render
from datetime import date

# Create your views here.

# Dictionary containing all blog posts
# Key: post slug (URL-friendly name), Value: post content/description
POSTS = [
    {
        "slug": "skateboarding-is-fun",
        "image": "skateboarding.png",
        "author": "coelho",
        "date": date(2025, 7, 25),
        "title": "Skateboarding is fun!",
        "excerpt": "Learning the tricks and enjoying the thrill of skateboarding",
        "content": """
            Skateboarding is a thrilling and exciting sport that has captured the hearts of many enthusiasts around the world. It involves riding and performing tricks on a skateboard, which is a flat board with wheels. Skateboarding can be done in various environments, including skate parks, streets, and ramps.
            One of the most appealing aspects of skateboarding is the sense of freedom it provides. Riders can express themselves through their unique style and creativity while performing tricks and maneuvers. Additionally, skateboarding promotes physical fitness, balance, and coordination.
            Whether you're a beginner or an experienced skater, skateboarding offers endless opportunities for fun and adventure. So grab your skateboard, hit the streets or the park, and experience the joy of skateboarding!
        """
    },
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "coelho",
        "date": date(2021, 7, 21),
        "title": "Mountain Hiking",
        "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whilst I was enjoying the view!",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    },
    {
        "slug": "programming-is-fun",
        "image": "coding.jpg",
        "author": "coelho",
        "date": date(2018, 3, 10),
        "title": "Programming Is Great!",
        "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    },
    {
        "slug": "into-the-woods",
        "image": "woods.jpg",
        "author": "coelho",
        "date": date(2020, 8, 5),
        "title": "Nature At Its Best",
        "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    }
]

def get_date(post):
    return post["date"]

# View function: Display the starting/home page with all posts
def starting_page(request):
    sorted_posts = sorted(POSTS, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts,
    })

# View function: Display the posts page (same as starting_page)
def all_posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": POSTS
    })

# View function: Display a single post detail page
def post_detail(request, slug):
    # except KeyError:
    #     # If post doesn't exist, raise a 404 error
    #     raise Http404(f"Post '{slug}' not found.")
    identified_post = next(post for post in POSTS if post["slug"] == slug)
    return render(request, "blog/post-detail.html", {
        "post": identified_post
    })
