from django.shortcuts import render
from .forms import TweetForm, UserRegistrationForm
from django.shortcuts import get_object_or_404,redirect
from .models import Tweet
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout
from django.db.models import Q


def tweet_list(req):
    query = req.GET.get('q') 
    if query:
        tweets = Tweet.objects.filter(
            Q(content__icontains=query) | Q(user__username__icontains=query)
        ).order_by('-created_at')
    else:
        tweets = Tweet.objects.all().order_by('-created_at')
        
    return render(req, "tweet/tweet_list.html", {"tweets": tweets, "query": query})

@login_required()
def tweet_add(req):
    if req.method == "POST":
        form = TweetForm(req.POST, req.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = req.user
            tweet.save()
            return redirect('tweet_list')  # Redirect to the tweet list after saving
    else:
        form = TweetForm()
    return render(req, "tweet/tweet_form.html", {"form": form})

@login_required()
def tweet_edit(req, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id)  # Only check ID

    if tweet.user != req.user:
        return render(req, "errors/errors.html", {
            "status":501,
            "message": "⛔ You are not allowed to edit this tweet."
        })

    if req.method == "POST":
        form = TweetForm(req.POST, req.FILES, instance=tweet)
        if form.is_valid():
            form.save()
            return redirect("tweet_list")
    else:
        form = TweetForm(instance=tweet)

    return render(req, "tweet/tweet_form.html", {"form": form, "tweet": tweet})


@login_required()
def tweet_delete(req, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id, user=req.user) or {}
    if req.method == "POST":
        tweet.delete()
        return redirect('tweet_list')  # Redirect to the tweet list after deletion
    return render(req, "tweet/tweet_delete_confirm.html", {"tweet": tweet})


def register(req):
    if req.method == "POST":
        form = UserRegistrationForm(req.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.changed_data['password1']) 
            user.save()
            login(req, user)
            return redirect("tweet_list")
    else:
        form = UserRegistrationForm()

    return render(req, 'registration/register.html', {"form":form})
