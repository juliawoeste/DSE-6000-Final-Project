import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd
from diagrams.diagram2 import smoking_disparity_vs_income
from diagrams.diagram8 import top10_lowest_avg_disparity
from diagrams.diagram6 import facet_line_disparity_by_demographic
from diagrams.diagram1 import avg_disparity_by_demographic_bar


app = dash.Dash(__name__)
server = app.server

# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

df2 = pd.read_csv('data/data.csv')

fig2 = px.scatter(df2, x="gdp per capita", y="life expectancy",
                 size="population", color="continent", hover_name="country",
                 log_x=True, size_max=60)

app.layout = html.Div([

#Does income influence the average smoking disparity value? 
    dcc.Graph(
        id="income-disparity-graph",
        figure=smoking_disparity_vs_income()
    ),
    html.H4("Interpretation"),
     html.Div('''
        The Smoking Disparity by Income Over Time chart shows clear and consistent differences in average smoking disparity between income groups from 2011-2023.
        The lowest income group (<$20000) consistently had the highest average smoking disparity compared to the other two income groups with a large increase in 2020-2021 from 1.58 to 2.51. This sharp increase may reflect pandemic-related stressors or uneven health impacts during COVID-19.
        The middle income group ($20000 - $74999) had a consistent average disparity of 1.05 to 1.36, lower than the low income group by higher than the highest income group. With the middle income group staying consistent for the time period,
        there are no major increases or decreases except a small spike in 2020-2021 where the average disparty went from 1.10 to 1.36. 
        The highest income group (>=$75000) had the lowest smoking disparity throughout 2011 to 2023 remaining between 0.41 to 0.68. However unlike the other income groups, in 2020 there was a decrease in average smoking disparity value, which may indicate stronger resilience to pandemic-related pressures.
        Overall, the trend from 2011 to 2023 shows that adults with lower income had substantially higher smoking disparity values, while those with higher income had the lowest, suggesting smoking-related outcomes are strongly tied to socioeconomic status.
    '''),


#Which states, overall, have the smallest smoking disparity across all demographic groups and all years? 

    dcc.Graph(
        id="lowest-states-graph",
        figure=top10_lowest_avg_disparity()
    ),
    html.H4("Interpretation"),
     html.Div('''
        The chart, Top 10 States with Lowest Average Smoking Disparity, shows the ten U.S. states with the smallest differences in smoking rates between demographic groups from 2011–2023. 
        A disparity value above 1 indicates that adults in the focus group smoke cigarettes at a higher rate than the reference group, so values just slightly above 1 reflect only small differences in smoking prevalence. 
        Even though all of the values on this chart are slightly above 1, these are the ten states with the smallest disparities in the entire country. This indicates that gaps in smoking rates between demographic groups (Income, Race/Ethnicity, Age, Employment and Mental Health) are relatively small in these states.
        Nevada exhibits the lowest average disparity at approximately 1.14, suggesting that smoking behavior is more uniform across demographic groups in the state, meaning no demographic group smokes at dramatically higher rates than its comparison group. 
        Although all ten states still have disparity values above 1, the narrow range between them (approximately 1.14–1.18) suggests that demographic gaps in smoking behavior are modest compared with the rest of the United States.
        These lower disparity levels may reflect more uniform access to public health resources, fewer socioeconomic divides, or more consistent tobacco-related risk factors within these states.
        Overall, these states represent the top ten in the United States with the lowest average smoking disparity values, demonstrating more equitable smoking outcomes and smaller gaps between focus groups and reference groups across demographic categories.
    '''),


    # html.H1('Hello'),

    # html.Div('''
    #     Dash: A web application framework for your data. 
    # '''),

    # dcc.Graph(
    #     id='example-graph',
    #     figure=fig
    # ),

    # html.Div('''
    #     Dash: Another example for chart
    # '''),

    # dcc.Graph(
    #     id='example-graph2',
    #     figure=fig2
    # )

    html.H2("Smoking Disparities Across Demographic Groups"),

    # 1) Facet line chart: trends over time by demographic
    dcc.Graph(
        id="facet-demographic-trends",
        figure=facet_line_disparity_by_demographic()
    ),
    html.H4("Interpretation"),
    html.Div("""
        The facet line chart basically shows how smoking disparities have changed 
        from 2011 to 2023 across different demographic groups — things like Age, Income, 
        Employment status, Mental Health, and Race/Ethnicity.
        One thing that stands out right away is that the Employment group almost always has the 
        biggest gap. Its values mostly sit in the mid-1.3 range, so the people in the focus groups for
        employment-related categories tend to smoke quite a bit more than their comparison group. On the 
        other hand, Race and Ethnicity has the smallest disparities (usually around 1.06–1.09), so those gaps 
        are much smaller. Every line stays over 1, so that means there is some level of disparity in 
        every group, even if the size of the gap differs. Employment and Income have the strongest disparities,
        while Race/Ethnicity is consistently the lowest. There are a few little changes year to year, but nothing 
        big or dramatic — for the most part looks like these disparities have been hanging around rather than getting much 
        better or worse.
    """),

    # 2) Bar chart: overall average disparity by demographic
    dcc.Graph(
        id="avg-disparity-by-demographic",
        figure=avg_disparity_by_demographic_bar()
    ),
    html.H4("Interpretation"),
    html.Div("""
    This bar chart basically shows the average smoking gap for different groups
    across all the states and years, and a couple things stand out right away. The Employment group
    is easily the biggest one — it’s sitting around 1.40, which is noticeably higher than 
    everything else. Income and Age are next, somewhere in the low 1.20s. Mental Health drops a bit below that,
    and Race/Ethnicity is the smallest gap of the bunch, roughly around 1.08. 
    Since 1 means the two groups smoke at the same rate, anything above that means the focus group is smoking more. 
    So seeing Employment that high feels like there’s something more going on there than just random variation. Overall, 
    the biggest differences show up when you look at whether someone’s working, how much they make, or what age range they 
    fall into. The racial and ethnic differences exist, but they’re not nearly as big in this dataset. If anything, it makes one think 
    public health programs might get more traction by focusing on unemployed folks, lower-income groups, and some age categories where the gap is clearly wider.
    """)
])

if __name__ == '__main__':
    app.run_server(debug=True, port=8080)
