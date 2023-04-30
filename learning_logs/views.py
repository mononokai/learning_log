from django.shortcuts import render, redirect
from .models import Topic, Entry
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
        form = TopicForm(data=request.POST) # Instantiating TopicForm with the values in the POST request
        if form.is_valid(): # Checking that all required fields are filled
            form.save() # Writing the data from the form to the DB
            return redirect('learning_logs:topics') # Sending the user to the topics page
    
    # Display a blank or invalid form
    context = {'form': form} # Takes the value from the form variable
    return render(request, 'learning_logs/new_topic.html', context) # Render the new_topic page


# Add a new entry
def new_entry(request, topic_id):   # Including the topic_id param to store the value received from the URL
    topic = Topic.objects.get(id=topic_id)  # Getting the topic object where the id is equal to topic_id

    if request.method != 'POST':
        # No data submitted, create a blank form
        form = EntryForm()
    else:
        # POST data submitted, process data
        form = EntryForm(data=request.POST) # Instantiating EntryForm with the POST data from the request object
        if form.is_valid(): # Checking that all required fields are filled
            new_entry = form.save(commit=False) # Setting the commit to False will create a new entry object
                                                # then assign it to new_entry without saving to the DB yet
            new_entry.topic = topic # Set the topic attribute of the new_entry object to the topic value pulled
                                    # from the DB at the beginning of the function
            new_entry.save() # Call save with no arguments to commit the data to the DB with the correct topic
            return redirect('learning_logs:topic', topic_id=topic_id)   # Sending the user to the topic page
            # For this redirect, we provide two argument, with the first being the name of the view that
            # we are redirecting the user to. The second, 'topic_id=topic_id' is the argument that the view
            # itself requires. The topic() view function requires the topic_id argument. Therefore, we are providing
            # the topic_id so that the view renders the page of the topic that the user had just provided an entry for.

    # Display a blank or invalid form
    context = {'topic': topic, 'form': form} # Taking the value of the form and topic variables
    return render(request, 'learning_logs/new_entry.html', context) # Render the new_entry page 


# Edit an existing entry
def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id) # Get the id of the entry the user wants to edit
    topic = entry.topic # Get the relevant topic

    if request.method != 'POST':
        # Initial request, pre-fill with current entry data
        form = EntryForm(instance=entry) # Create a form pre-filled with data from this entry's instance
    else:
        # POST data submitted, process data
        form = EntryForm(instance=entry, data=request.POST) # Create a form using the data associated with the
                                                            # existing entry object and, then update it with data
                                                            # from the data from the POST request
        if form.is_valid(): # Check that form is valid
            form.save() # Because the entry is already associated with the correct topic, the database entry
                        # can be updated immediately
            return redirect('learning_logs:topic', topic_id=topic.id) # Sending the user to the relevant topic page
    
    context = {'entry': entry, 'topic': topic, 'form': form} # Taking the value of entry, topic and form variables
    return render(request, 'learning_logs/edit_entry.html', context) # Render the edit_entry page

