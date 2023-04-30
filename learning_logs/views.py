from django.shortcuts import render, redirect
from .models import Topic
from .forms import TopicForm, EntryForm

# Home page for the Learning Log
def index(request):
    return render(request, 'learning_logs/index.html')


# Show all topics
def topics(request):
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


# Show a single topic and all of its entries
def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


# Add a new topic
def new_topic(request):
    if request.method != 'POST':
        # No data submitted, create a blank form
        form = TopicForm()
    else:
        # POST data submitted, process data
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')
    
    # Display a blank or invalid form
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


# Add a new entry
def new_entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # No data submitted, create a blank form
        form = EntryForm()
    else:
        # POST data submitted, process data
        new_entry = form.save(commit=False)
        new_entry.topic = topic
        new_entry.save()
        redirect('learning_logs:topic', topic_id=topic_id)

    # Display a blank or invalid form
    context = {'form': form}
    return render(request, 'learning_logs/new_entry.html', context)