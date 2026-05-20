# Assessment Task Part 1

## Identifying & Defining

### Mind Map

### HYPOTHESIS

GHS students spend more time on their screens daily then reading a book weekly.

### Functional Requirements

* The code would be able to load in files such as .csv files, and should be able to handle errors in file loading.

* The data system should be able to filter, sort, or group data if requested.

* The system should be able to find the mean and range of certain groups of data in the dataset.

* The data would be visualised as either a Pandas dataframe or a Matplotlib bar/line graph depending on the user's preference.

* The final dataset should be kept as a .csv file, and as previously mentioned, would be outputted as either a dataframe or bar graph per the user's preference.

### Non-Functional Requirements

* The user interface should be easy to navigate and it should be designed in a way so that a user can naviagate it without confusion from the start.

* The README file should explain clearly how the module works in case the user doesn't understand.

* The data presented by the system shouldn't be 100% relied on as there may be errors - the system should be able to inform the user about that.

### Use-Case

* Actor - the user

* Goal - to access and interact with existing data using the system's user interface.

#### Preconditions

* The dataset has already been preloaded into the data system by it's programmer (me). 

* User has access to the user interface.

#### How It Would Work

1. User opens the program and is presented with a text-based menu.

2. From this menu, the user chooses the following options:

    a. Display the data as either a written dataframe or a visual (bar graph).
    b. Filter through or search for data based on specific criteria.
    c. Exits the program.
    d. Transmits an error message (if the user inputs something other than what the program can do).

3. The system performs the requested action and either outputs to user or stops entirely (if the user requests to exit).

#### Postconditions

* User has viewed the data in the form they requested.

* Data remains available for future observation by other users via the program.

## Research and Planning

### Secondary Research

* Approximately 91% of teenagers between 14 and 17 owned a mobile phone in 2023 according to [Charles Sturt University](https://news.csu.edu.au/opinion/91-per-cent-of-australian-teens-have-a-phone-but-many-are-not-secure).

* In 2021/2022, over 90% of children had at least one hour of screen time weekly, with 24% of those children spending at least 20 hours per week on their screens, according to [the Australian Bureau of Statistics](https://www.abs.gov.au/statistics/people/people-and-communities/cultural-and-creative-activities/2021-22).

* 3 in 10 students in Years 7-12 don't read in their spare time, according to [Deakin University](https://www.deakin.edu.au/about-deakin/news-and-media-releases/articles/surprising-facts-about-aussie-teens-reading-habits-revealed)

* The proportion of children aged 6-17 who read for pleasure has dropped from 37% to 28%, according to [the University of Southern Queensland (USQ)](https://www.unisq.edu.au/news/2025/11/the-conversation-childrens-booker-prize)

### Discussion

Nationwide, my hypothesis is most likely correct, as phone usage by teenagers/children has grown while the amount of reading for pleasure has decreased. While correlation doesn't always mean causation, the high usages of phones by children has definitely contributed to the drop of reading rates in said children in recent years. For instance, Deakin University did a survey and recorded that 3 in 10 students in high school ages don't read in their spare time, while Charles Sturt University states that approximately 91% of teenagers aged between 14 and 17 owned a mobile phone in 2023. While these are surveys, meaning that there is a level of inaccuracy in representing ALL teenagers and children in Australia, it still is a good display of how phone usage is growing rapidly and book usage for pleasure has been dropping within these demographics. 

### Acquiraton of Data

I acquired the bulk of my data through a survey. This survey would allow me to collect data on:

* How much time subjects spend on their phone in a day

* How much time subjects spend on a book in a week for pleasure (not for schoolwork)

* The last time subjects read books

* Common reasons for subjects not reading books

All the survey data has been compiled into one large dataset, which I then seperated into several smaller datasets that cover specific data (e.g. Common reasons for subjects not reading books) that I could then display via the interface.

### Data Dictionary

Note that this dictionary is for the main dataset and not for the other smaller datasets

| Field | Datatype | Format for Display | Example | Validation |
| -------- | -------- | ---------- | ---------- | ---------- |
| How many hours do you spend on your phone daily? | str | XX...XX | > 1 hour | Can be any amount of characters, and can include letters and numbers |
| How many hours do you spend reading a book IN YOUR SPARE TIME weekly? | str | XX...XX | 1 - 2 hour | Can be any amount of characters, and can include letters and numbers |
| When was the last time you've read a book for pleasure (IN YOUR FREE TIME)? | str | XX...XX | 2 - 3 weeks ago | Can be any amount of characters, and can include letters and numbers |
| Is there a reason you haven't read a book in the past? | str | XX...XX | I've read every book | Can be any amount of characters, but can't include numbers |

## Testing and Evaluating

### Analysis and Conclusion

The data analysis interface works perfectly as far as I am concerned. In the interface, people can view data as either a pure, written dataset or a visual representation, as well as being able to edit data if such data is innacurate. There are a few problems with the interface, for instance when trying to exit the interface, you would have to press the key that allows you to exit the interface two or more times for it to actually exit, and the visualisations would often have the x-axis labels stamped on top of each other in a way that makes it hard to read the aforementioned values. Despite this, the overall functionability and usability of the interface still works extremely well.

The data analysis also clearly proves my hypothesis - that GHS students spend more time on their phones in a day than reading a book weekly. In fact, the results garnered concerning time spent reading books in free time weekly was extremely pitiful - with 21 of the 46 responses spending less than an hour a week reading a book, compared to the 31 subjects who spent 1 - 4 hours on their phone daily. The most common reasons subjects don't spend time reading books is easy to guess - people just use other forms of entertainment, thus strengthening the truthfullness of hypothesis.