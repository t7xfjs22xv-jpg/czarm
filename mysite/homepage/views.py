import random
from django.shortcuts import render, redirect
from .models import FreedomPost

SMART_VERSES = {
    "perspective": ["Proverbs 3:5 - Trust in the Lord with all your heart.", "Romans 12:2 - Do not be conformed to this world."],
    "comfort": ["Psalm 23:1 - The Lord is my shepherd; I shall not want.", "Matthew 11:28 - Come to me, all who labor."],
    "strength": ["Isaiah 40:31 - But they who wait for the Lord shall renew their strength.", "Philippians 4:13 - I can do all things."],
    "wisdom": ["James 1:5 - If any of you lacks wisdom, let him ask God.", "Proverbs 16:3 - Commit your work to the Lord."],
    "general": ["Jeremiah 29:11 - For I know the plans I have for you.", "Numbers 6:24 - The Lord bless you and keep you."]
}

def wall_view(request):
    if request.method == "POST":
        msg = request.POST.get("message", "").lower()
        author = request.POST.get("author_name") or "Anonymous"
        
        # Pick the right mood based on keywords
        verse_list = SMART_VERSES["general"]
        if any(word in msg for word in ["sad", "tired", "hard", "help"]): verse_list = SMART_VERSES["comfort"]
        elif any(word in msg for word in ["future", "plan", "how"]): verse_list = SMART_VERSES["perspective"]
        elif any(word in msg for word in ["study", "work", "school"]): verse_list = SMART_VERSES["wisdom"]
        elif any(word in msg for word in ["win", "strong", "goal"]): verse_list = SMART_VERSES["strength"]

        FreedomPost.objects.create(
            content=request.POST.get("message"), 
            name=author,
            bible_verse=random.choice(verse_list)
        )
        return redirect('wall')
    
    posts = FreedomPost.objects.all().order_by('-created_at')
    return render(request, 'wall.html', {'posts': posts})