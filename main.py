import dash
from dash import dcc, html, Input, Output, State
import plotly.express as px
import pandas as pd
from diagrams.diagram2 import smoking_disparity_vs_income
from diagrams.diagram8 import top10_lowest_avg_disparity
from diagrams.diagram6 import facet_line_disparity_by_demographic
from diagrams.diagram1 import avg_disparity_by_demographic_bar
from diagrams.dezi_histogram import histogram_prevalence
from diagrams.dezi_choropleth import mental_disparity
from diagrams.ml import (best_model, focus_encoder, ref_encoder, focus_groups, reference_groups)


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
        The y-axis has been scaled to a narrower range to make the small differences between states more visually distinguishable.
        A disparity value above 1 indicates that adults in the focus group smoke cigarettes at a higher rate than the reference group, so values just slightly above 1 reflect only small differences in smoking prevalence. 
        Even though all of the values on this chart are slightly above 1, these are the ten states with the smallest disparities in the entire country. This indicates that gaps in smoking rates between demographic groups (Income, Race/Ethnicity, Age, Employment and Mental Health) are relatively small in these states.
        Nevada exhibits the lowest average disparity at approximately 1.14, suggesting that smoking behavior is more uniform across demographic groups in the state, meaning no demographic group smokes at dramatically higher rates than its comparison group. 
        Although all ten states still have disparity values above 1, the narrow range between them (approximately 1.14–1.18) suggests that demographic gaps in smoking behavior are modest compared with the rest of the United States.
        These lower disparity levels may reflect more uniform access to public health resources, fewer socioeconomic divides, or more consistent tobacco-related risk factors within these states.
        Overall, these states represent the top ten in the United States with the lowest average smoking disparity values, demonstrating more equitable smoking outcomes and smaller gaps between focus groups and reference groups across demographic categories.
    '''), 

# What is the distribution of smoker prevalence across all demographics from 2011–2023?

dcc.Graph(
    id="histogram-prevalence-graph",
    figure=histogram_prevalence()
),
html.H4("Interpretation"),
html.Div('''
    These graphs show the distribution of the percentages of smokers across all demographics from 2011–2023. 
    On average we can see that 15–19.9% of all demographics were smokers. The percentage bins larger than 15–19.9% 
    seem to be significantly lower. We begin to see change in the percentages from 2021–2023 where we see a large 
    increase in the percentages of 5–14.99%, and a decrease in the 15–19.9%. This would mean that within the past 
    few years we have seen an overall decrease in the amount of smokers across all of the focus groups.
'''),

# How has smoking disparity changed between 'High Distress' and 'No Distress' mental groups across states from 2011–2023?

dcc.Graph(
    id="mental-disparity-choropleth",
    figure=mental_disparity()
),
html.H4("Interpretation"),
html.Div('''
    This choropleth shows the smoking disparity between "High Distress" and "No Distress" mental groups across all 
    states from 2011–2023. The year slider allows one to compare the disparity rates between years. We see large 
    disparities between the years of 2013–2015 with a slight drop off after that. This then reaches the largest 
    disparity spread in the country in 2019, with a huge drop off in disparity during COVID/quarantine in 2020. 
    One could begin to theorize whether the time off from work during quarantine could have contributed to the 
    narrowing of disparity between these two mental-health groups.
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
    """),


    # 3) Bar chart: top ten groups by average disparity
    dcc.Graph(
        id="avg-disparity-top-ten-groups",
        figure=top_ten_groups()
    ),
    html.H4("Interpretation"),
    html.Div("""
    Employment has the highest average disparity among demographics, in large part, due to
    people unable to work or who are unemployed having the largest disparities across categories.
    Other factors like severe mental health and low socioeconomic status cause higher smoking disparities as well.
    """),

    # 4) Bar chart: bottom ten groups by average disparity
    dcc.Graph(
        id="avg-disparity-bottom-ten-groups",
        figure=bottom_ten_groups()
    ),
    html.H4("Interpretation"),
    html.Div("""
    People who are retired have the lowest smoking disparity, followed by above average
    income group (+$75K), people aged 65+, and Homemakers/students. This makes sense that these people have lower average smoking disparity
    given that people are who retired or are older tend to think more about their health than younger or poorer people.
    """),

    # 5) Correlation Matrix: which categories are strongly correlated with each other?
    dcc.Graph(
        id="strong-correlation-matrix",
        figure=corr_matrix()
    ),
    html.H4("Interpretation"),
    html.Div("""
    Employment:
        Categories like "Unable to work" and "Retired" in both focus and reference groups have high correlations with each other 
        and with disparity, which supports a previous finding that employment has high influence on disparity with respect to 
        other groups.
    Income Groups:
        Categories ref_20K-75K and ref_<20K and ref_<20000 are positively correlated with each other and the disparity value.
        On the other hand, the focus income group focus_>=75K show negative or weak correlation with disparity.
        Lower income groups in the reference population seem to be associated with smaller disparities, as a result of higher 
        smoking rates. In contrast, higher-income focus groups tend to have lower disparities.
    """),

    
html.H3('Predicting Smoking Disparity'),

html.Div([html.Label('Focus Group'), dcc.Dropdown(
    id='focus-group-input', 
    options=[{'label':g, 'value':g} for g in focus_groups],
    placeholder='Select Focus Group', 
    style={'width':'60%'}), 
]),


html.Div([html.Label('Reference Group'), dcc.Dropdown(
    id='ref-group-input',
    options=[{'label':g, 'value':g} for g in reference_groups],
    placeholder='Select Reference Group', 
    style={'width':'60%'}),
]), 

html.Div([html.Label('Focus Prevalence %'), dcc.Input(
    id='focus-prev-input', 
    type='number', 
    placeholder='ex: 15.5', 
    style={'width':'30%'}),

]),

html.Div([html.Label('Reference Prevalence %'), dcc.Input(
    id='ref-prev-input',
    type='number',
    placeholder='ex: 10.0', 
    style={'width': '30%'}), 

]), 

html.Button('Disparity Prediction', id='predict-button', n_clicks=0), 
html.H4('Prediction Results:'),
html.Div(id='prediction-output'), 

])
@app.callback(
    Output('prediction-output', 'children'),
    Input('predict-button', 'n_clicks'),
    State('focus-group-input', 'value'), 
    State('ref-group-input', 'value'), 
    State('focus-prev-input', 'value'), 
    State('ref-prev-input', 'value'), 
) 
def make_prediction(n_clicks, focus_group, ref_group, focus_prev, ref_prev): 
    if n_clicks == 0:
        return 'Please enter values and click the predict button'
    if (
        focus_group is None
        or ref_group is None
        or focus_prev is None
        or ref_prev is None
    ):
        return 'Please fill in the fields' 
    
    focus_encoded = float(focus_encoder.transform([[focus_group]])[0][0])
    ref_encoded = float(ref_encoder.transform([[ref_group]])[0][0])

    X_new = [[focus_encoded, ref_encoded, float(focus_prev), float(ref_prev)]]
    pred = best_model.predict(X_new)[0]
    return f"Predicted disparity value: {pred:.2f}"

if __name__ == '__main__':    
    app.run(debug=True, port=8080)
