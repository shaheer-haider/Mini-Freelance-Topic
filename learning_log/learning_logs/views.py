from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.utils import timezone

from .models import Topic, Entry
from .forms import TopicForm, EntryForm

def index(request):
    context = {}

    if not request.user.is_anonymous:
        current_datetime = timezone.now()
        midnight_datetime = current_datetime.replace(hour=0, minute=0, second=0)
        topics = Topic.objects.filter(owner=request.user, date_added__gte=midnight_datetime).order_by('date_added')
        context['topics'] = topics

    return render(request, 'learning_logs/index.html', context)

@login_required
def profile(request):
    return render(request, 'learning_logs/profile.html')

@login_required
def update_profile(request):
    request.user.first_name = request.POST.get('first_name')
    request.user.last_name = request.POST.get('last_name')
    request.user.email = request.POST.get('email')
    request.user.save()
    profile_pic = request.FILES.get('profile_pic')
    if profile_pic:
        fs = FileSystemStorage()
        filename = fs.save(f'media/profile_pics/{profile_pic.name}', profile_pic)
        request.user.profile_pic = filename
    return redirect('learning_logs:profile')


@login_required
def topics(request):
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if topic.owner != request.user:
        raise Http404

    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):

    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
    if form.is_valid():
        new_topic = form.save(commit=False)
        new_topic.owner = request.user
        new_topic.save()
        return redirect('learning_logs:topics')

    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):

    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)

    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):

    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.owner:
        raise Http404

    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)
