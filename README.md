# Data Science Project - "What is in a name?"
## By Spencer Damiano, credit to BYU-Idaho Data Science departmentfor prompt

### Background
Early in prehistory, some descriptive names began to be used again and again until they formed a name pool for a particular culture. Parents would choose names from the pool of existing names rather than invent new ones for their children.

With the rise of Christianity, certain trends in naming practices manifested. Christians were encouraged to name their children after saints and martyrs of the church. These early Christian names can be found in many cultures today, in various forms. These were spread by early missionaries throughout the Mediterranean basin and Europe.

By the Middle Ages, the Christian influence on naming practices was pervasive. Each culture had its pool of names, which were a combination of native names and early Christian names that had been in the language long enough to be considered native. [ref](https://heraldry.sca.org/names/namehist.html)

### Data
* uses the [names_year data](https://github.com/byuidatascience/data4names/raw/master/data-raw/names_year/names_year.csv)
* [info](https://github.com/byuidatascience/data4names/blob/master/data.md)

### Questions and Tasks

1. How does your name at your birth year compare to its use historically?

2. If you talked to someone named Brittany on the phone, what is your guess of his or her age? What ages would you not guess?

3. Mary, Martha, Peter, and Paul are all Christian names. From 1920 - 2000, compare the name usage of each of the four names. What trends do you notice?

4. Think of a unique name from a famous movie. Plot the usage of that name and see how changes line up with the movie release. Does it look like the movie had an effect on usage?

### Helpful Recourses for Future Reference
- For general chart help [Customizing Visuals - Altair Docs](https://altair-viz.github.io/user_guide/customization.html)
- To filter data by the lowest values use [.nsmallest](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.nsmallest.html)
- To customize your index[.set_index](https://www.geeksforgeeks.org/reset-index-in-pandas-dataframe/#) 