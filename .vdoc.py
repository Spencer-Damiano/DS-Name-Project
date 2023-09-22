# type: ignore
# flake8: noqa
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#| label: libraries
#| include: false
import pandas as pd
import altair as alt
import numpy as np

from IPython.display import Markdown
from IPython.display import display
from tabulate import tabulate
#
#
#
#
#
#
#
#
#
#| label: project data
#| code-summary: Read and format project data
# Include and execute your code here
dat = pd.read_csv("https://github.com/byuidatascience/data4names/raw/master/data-raw/names_year/names_year.csv")
#
#
#
#
#
#
#
#
#
#
#
#| label: Q1
#| code-summary: Read and format data
# Include and execute your code here

spencer_over_time = dat[["name", "year", "Total"]].query("name == 'Spencer'")

#
#
#
#
#
#| label: Q1 chart
#| code-summary: plot example
#| fig-cap: "Spencer Over Time"
#| fig-align: center
# Include and execute your code here
chart = alt.Chart(
        spencer_over_time, 
        title=alt.Title("Spencers Over Time")
    )\
    .mark_line()\
    .encode(
        # x = "year:T",
        # y = "Total:Q",
        alt.X("year").axis(format="T").title("Year"),
        alt.Y("Total").axis(format="N").title("Total Spencers"),
        )\
    .properties(
        width=800,
        height=400
    )

line = alt.Chart(pd.DataFrame({"x": [1998], "Birth Year": ["Birth Year"]})).mark_rule().encode(
    alt.X("x").axis(format="T"),
    )

chart + line
    
#
#
#
#
#| label: Q1 table
#| code-summary: table example
#| tbl-cap: "Spencers as a Table"
#| tbl-cap-location: top
# Include and execute your code here

spencer_table = spencer_over_time.head(1000)\
    .groupby('year')\
    .sum()\
    .tail(10)\
    .filter(["year", "Total"])

display(spencer_table)

#
#
#
#
#
#
#
#
#
#
#| label: Q2
#| code-summary: Read and format data
# Include and execute your code here

dat = pd.read_csv('https://raw.githubusercontent.com/byuidatascience/data4names/master/data-raw/names_year/names_year.csv')

brit_popular = dat[['name', 'year', 'Total']].query('name == "Brittany"')

#
#
#
#
#
#| label: Q2 chart
#| code-summary: plot example
#| fig-cap: "Britneys Popularity"
#| fig-align: center
# Include and execute your code here
highest_ttl = brit_popular["Total"].max() / brit_popular["Total"].sum()


chart = alt.Chart(
        brit_popular,
        title = alt.Title("Percent of Total Britneys by Year")
    )\
    .transform_joinaggregate(
        total_time="sum(Total)"
    )\
    .transform_calculate(
        percent_of_total="datum.Total / datum.total_time"
    )\
    .mark_bar()\
    .encode(
    alt.X("year").axis(format="T").title("Year"),
    y = alt.Y("percent_of_total:Q").axis(format="%").title("Percent of all Britneys"),
    color = alt.condition(
        alt.datum.percent_of_total == highest_ttl,
        alt.value('red'),
        alt.value('lightGray')
    )
)

chart
#
#
#
#
#| label: Q2 table
#| code-summary: table example
#| tbl-cap: "Not much of a table"
#| tbl-cap-location: top
# Include and execute your code here

brit_unpopular = brit_unpopular.nsmallest(1000, 'Total')

display(brit_unpopular.nsmallest(1000, 'Total'))

# mydat = brit_popular.nsmallest(1000, ['Total', 'year'])\
#     .groupby('year')\
#     .sum()\
#     .tail(10)\
#     .filter(["year", "Total"])

# display(mydat)

#
#
#
#
#
#
#
#
#
#
#| label: Q3
#| code-summary: Read and format data
# Include and execute your code here


#
#
#
#
#
#| label: Q3 chart
#| code-summary: plot example
#| fig-cap: "My useless chart"
#| fig-align: center
# Include and execute your code here
alt.Chart(dat.head(200))\
    .encode(x = "name", y = "AK")\
    .mark_bar()
#
#
#
#
#| label: Q3 table
#| code-summary: table example
#| tbl-cap: "Not much of a table"
#| tbl-cap-location: top
# Include and execute your code here
mydat = dat.head(1000)\
    .groupby('year')\
    .sum()\
    .reset_index()\
    .tail(10)\
    .filter(["year", "AK","AR"])

display(mydat)

#
#
#
#
#
#
#
#
#
#
#
#
#
#
