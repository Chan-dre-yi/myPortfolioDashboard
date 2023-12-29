import dash
from dash import dcc, html
import plotly.graph_objs as go

# Sample data for demonstration
skills_data = {
    'Programming': {'Java': 80, 'Python': 90, 'C': 75, 'C++': 75},
    'Big Data': {'Spark': 60, 'NiFi': 50, 'Hadoop': 60, 'Kubernetes': 50, 'AWS': 65},
    'Software Development': {'Github': 80, 'HTML': 95, 'CSS': 85, 'Javascript': 85, 'PHP': 90, 'CI/CD': 50},
    'Analytics & Visualization': {'R': 80, 'MATLAB': 70, 'SPSS': 70, 'PowerBI': 85, 'MS Excel': 85},
    'Machine Learning': {'Tensorflow': 70, 'Keras': 70, 'Scikit-Learn': 85, 'NLTK': 80}
}

projects_data = {
    'ChatNet': 75,
    'SenTube': 80,
    'PowerCast': 85,
    'DamageDetective': 70,
    'DataZip': 90,
    'StrateGenius': 60,
    'MyCV.web': 100,
    'Portfolio Dashboard': 100
}

# Define project details (you can customize this dictionary)
project_details = {
    'ChatNet': 'A chat application with advanced features.',
    'SenTube': 'A video sharing platform.',
    'PowerCast': 'A podcast hosting service.',
    'DamageDetective': 'An image analysis tool for damage detection.',
    'DataZip': 'A data compression utility.',
    'StrateGenius': 'A strategy planning application.',
    'MyCV.web': 'My personal website and CV.'
}

# Positions of Responsibility data (customize this according to your roles)
positions_data = {
    'General Enquiry Manager': 'for VIT’s cultural fest : RIVIERA’23',
    'Director of Events': 'for Deuchest Literary Association VIT — tenure: 2022-23'
}

# Internships data (customize this according to your roles)
internships_data = {
    'Software Development Intern': 'at Intel Corp., July 2023 - May 2024',
    'Data Analytics Intern': 'at Vindhya Infomedia Ltd., Feb 2023 - Mar 2023'
}

# Education data
education_data = {
    'Degree Education [Masters] (Vellore Institute of Technology, Vellore | Integrated MSc. Computational Statistics & Data Analytics | 2024)': {'score': 9.11, 'type': 'CGPA'},
    'Higher Secondary Education (Divine Child High School, Surat | CBSE - Physic, Chemistry, Mathematics | 2019)': {'score': 84.5, 'type': 'Percentage'},
    'Secondary Education (S. D. Jain Modern School, Surat | CBSE | 2017)': {'score': 9.6, 'type': 'CGPA'}
}

# Function to create a progress bar for each educational qualification
def create_progress_bar(title, score_info):
    score = score_info['score']
    score_type = score_info['type']

    # Normalize score for display
    normalized_score = (score / 10) * 100 if score_type == 'CGPA' else score

    # Split the title to separate the qualification name and college name
    qualification, college_name = title.split(' (')
    college_name = f'({college_name}'  # Re-add the opening bracket

    # Define the display text
    display_text = f'{score} CGPA' if score_type == 'CGPA' else f'{score} %'

    # Define hover text
    hover_text = f'{score}/{10 if score_type == "CGPA" else 100} {score_type}'  # Hover text

    # Define a fixed width for the progress bar container
    progress_bar_container_width = '300px'  # You can adjust this value as needed

    return html.Div([
        html.H4(qualification, style={'marginBottom': 0, 'fontFamily': 'Verdana, Geneva, sans-serif', 'fontSize': '10px'}),
        html.Div(college_name, style={'marginBottom': 5, 'fontFamily': 'Verdana, Geneva, sans-serif', 'fontSize': '8px', 'color': 'grey'}),
        html.Div(style={'width': progress_bar_container_width, 'backgroundColor': '#e0e0e0', 'borderRadius': '5px', 'margin': 'auto'},
            children=[
                html.Div(style={'width': f'{normalized_score}%', 'backgroundColor': '#b769df', 'height': '18px', 'borderRadius': '5px', 'textAlign': 'right', 'paddingRight': '5px', 'color': 'white', 'fontFamily': 'Verdana, Geneva, sans-serif', 'fontSize': '10px'},
                         children=display_text, title=hover_text)  # Add hover text
            ]
        )
    ], style={'marginBottom': '15px'})






# Style for the rounded rectangles
section_style = {
    'border': '1px solid #ddd',  # Solid border
    'borderRadius': '15px',      # Rounded corners
    'padding': '20px',           # Padding inside the rectangle
    'marginBottom': '30px',      # Margin at the bottom of each section
    'backgroundColor': '#f9f9f9' # Light background color for the section
}

# Dash app layout
app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Chandreyi Chowdhury : PORTFOLIO DASHBOARD', style={'textAlign': 'center', 'fontSize': 20, 'fontFamily': 'Verdana, Geneva, sans-serif', 'marginTop': '20px'}),
    
    # Wrap the links in a div with display style 'flex'
    html.Div([
        html.A('chandreyi.surat@gmail.com', href='https://chandreyi.surat@gmail.com', target='_blank', style={'fontSize': 6.5, 'margin': '0 10px', 'fontFamily': 'Verdana, Geneva, sans-serif', 'color': '#e7b7ff', 'fontWeight': 'bold'}),
        html.A('github.com/Chan-dre-yi', href='https://github.com/Chan-dre-yi', target='_blank', style={'fontSize': 6.5, 'margin': '0 10px', 'fontFamily': 'Verdana, Geneva, sans-serif', 'color': '#e7b7ff', 'fontWeight': 'bold'}),
        html.A('linkedin.com/in/chandreyic', href='https://linkedin.com/in/chandreyic', target='_blank', style={'fontSize': 6.5, 'margin': '0 10px', 'fontFamily': 'Verdana, Geneva, sans-serif', 'color': '#e7b7ff', 'fontWeight': 'bold'}),
        html.A('chan-dre-yi.github.io/my-CV-dot-web', href='https://chan-dre-yi.github.io/my-CV-dot-web', target='_blank', style={'fontSize': 6.5, 'margin': '0 10px', 'fontFamily': 'Verdana, Geneva, sans-serif', 'color': '#e7b7ff', 'fontWeight': 'bold', 'marginBottom': '60px'}),
    ], style={'display': 'flex', 'justifyContent': 'center', 'marginTop': '-11px'}),

    # Skills Section
    html.Div([
        html.H2('Proficiency of my Skills', style={'textAlign': 'center', 'fontSize': 14, 'fontFamily': 'Verdana, Geneva, sans-serif', 'marginBottom': '30px'}),
        html.Div([
            dcc.Graph(
                id=f'skill-chart-{category}',
                figure={
                    'data': [go.Bar(
                        y=list(skills.keys()),
                        x=list(skills.values()),
                        orientation='h',
                        name=category,
                        width=0.6,
                        marker=dict(color='#e7b7ff') 
                    )],
                    'layout': go.Layout(
                        title={'text': f'{category} Skills', 'font': {'size': 8}},
                        xaxis={'title': '', 'titlefont': {'size': 8}, 'tickfont': {'size': 6}},
                        yaxis={'title': '', 'titlefont': {'size': 8}, 'tickfont': {'size': 8}},
                        margin=dict(l=60, r=20, t=30, b=20),
                        height=120
                    )
                },
                style={'display': 'inline-block', 'width': '19%'}
            ) for category, skills in skills_data.items()
        ], style={'textAlign': 'center', 'display': 'flex', 'flexWrap': 'wrap'})
    ], style={**section_style, 'font-weight': 'bold'}),

    # Projects Section
    html.Div([
        html.H2('Contribution in my Projects', style={'textAlign': 'center', 'fontSize': 14, 'fontFamily': 'Verdana, Geneva, sans-serif', 'marginBottom': '30px'}),
        html.Div([
            dcc.Graph(
                id=f'project-chart-{project}',
                figure={
                    'data': [go.Pie(
                        labels=[f'Details: {project_details.get(project, "")}',''],
                        values=[percentage, 100 - percentage],
                        hole=.7,
                        textinfo='none',
                        hoverinfo=['percent','none'],
                        marker={
                            'colors': ['#f2d7ff', 'rgba(0,0,0,0)']  # Set the second segment to transparent
                        }
                    )],
                    'layout': go.Layout(
                        title={'text': f'<b>{project}</b>', 'font': {'size': 8}},
                        showlegend=False,
                        margin=dict(l=10, r=10, t=30, b=10),
                        height=100
                    )
                },
                style={'display': 'inline-block', 'width': '12.5%'}
            ) for project, percentage in projects_data.items()
        ], style={'textAlign': 'center', 'display': 'flex', 'flexWrap': 'wrap'})
    ], style=section_style),
    

    # Education Section with Progress Bars
    html.Div([
        html.H2('Education', style={'textAlign': 'center', 'fontSize': 14, 'fontFamily': 'Verdana, Geneva, sans-serif'}),
        html.Div([
            create_progress_bar(title, score_info) for title, score_info in education_data.items()
        ], style={'textAlign': 'center', 'display': 'flex', 'flexDirection': 'column', 'alignItems': 'center'})
    ], style=section_style),
    

    # Languages Section
    html.Div([
        html.H2('Languages Known', style={'textAlign': 'center', 'fontSize': 14, 'fontFamily': 'Verdana, Geneva, sans-serif'}),
        html.P('English, Hindi, Bengali, Gujarati, French', style={'textAlign': 'center', 'fontSize': 10, 'fontFamily': 'Verdana, Geneva, sans-serif'})
    ], style=section_style),
    
    # Positions of Responsibility Section
    html.Div([
        html.H2('Professional Responsibilities', style={'textAlign': 'center', 'fontSize': 14, 'fontFamily': 'Verdana, Geneva, sans-serif'}),
        
        # Centered heading and two cards side by side
        html.Div([
            html.Div([
                html.H4(title, style={'fontSize': 10, 'fontFamily': 'Verdana, Geneva, sans-serif', 'color': '#666666'}),
                html.P(description, style={'fontSize': 8, 'fontFamily': 'Verdana, Geneva, sans-serif', 'color': '#666666'})
            ], style={'border': '1px solid #ddd', 'borderRadius': '15px', 'padding': '15px', 'margin': '10px', 'backgroundColor': '#f2d7ff', 'width': '45%', 'display': 'inline-block'})
            for title, description in positions_data.items()
        ], style={'textAlign': 'center', 'display': 'flex', 'justifyContent': 'center'}),
        
    ], style={**section_style, 'display': 'flex', 'flexDirection': 'column', 'alignItems': 'center'}),
    
    
    # Internships Section
    html.Div([
        html.H2('Internship Experience', style={'textAlign': 'center', 'fontSize': 14, 'fontFamily': 'Verdana, Geneva, sans-serif'}),
        
        # Centered heading and two cards side by side
        html.Div([
            html.Div([
                html.H4(title, style={'fontSize': 10, 'fontFamily': 'Verdana, Geneva, sans-serif', 'color': '#ffffff'}),
                html.P(description, style={'fontSize': 8, 'fontFamily': 'Verdana, Geneva, sans-serif', 'color': '#ffffff'})
            ], style={'border': '1px solid #ddd', 'borderRadius': '15px', 'padding': '15px', 'margin': '10px', 'backgroundColor': '#b769df', 'width': '220px', 'display': 'inline-block'})
            for title, description in internships_data.items()
        ], style={'textAlign': 'center', 'display': 'flex', 'justifyContent': 'center'}),
        
    ], style={**section_style, 'display': 'flex', 'flexDirection': 'column', 'alignItems': 'center'})



], style={'margin': 'auto', 'width': '95%'})

# To run this app, use the following command
#app.run_server(debug=True)

# This is used by the WSGI server to run your app
#if __name__ == '__main__':
#    app.run_server(debug=True)

pip freeze > requirements.txt
